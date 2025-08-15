from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# Webhook de saída do Bitrix24
@app.post("/bitrix-webhook/")
async def webhook(request: Request):
    try:
        data = await request.json()
        print("📩 Dados recebidos do Bitrix:", data)
        return {"status": "ok", "received": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Rota simples só para teste de vida
@app.get("/")
async def root():
    return {"message": "API do Webhook Bitrix24 está ativa"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
