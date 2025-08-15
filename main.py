from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# Rota que vai receber o POST do webhook
@app.post("/webhook")
async def receber_webhook(request: Request):
    try:
        dados = await request.json()  # Captura o corpo da requisição como JSON
    except Exception:
        dados = await request.body()  # Caso não seja JSON válido

    print("📩 Dados recebidos do webhook:")
    print(dados)

    # Aqui você pode tratar e salvar no banco, mandar para outra API, etc.
    
    return {"status": "ok", "mensagem": "Webhook recebido com sucesso!"}


# Rota para testar se a API está online
@app.get("/")
def home():
    return {"status": "online", "mensagem": "API FastAPI no Render funcionando!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
