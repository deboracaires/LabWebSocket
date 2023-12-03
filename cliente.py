import asyncio
import websockets

async def cliente():
    uri = "ws://localhost:8765"

    # Solicita ao usuário que forneça um nome de usuário único
    nome_usuario = input("Digite seu nome de usuário: ")

    async with websockets.connect(uri) as websocket:
        # Envia o nome de usuário para o servidor
        await websocket.send(nome_usuario)

        # Loop para enviar mensagens
        while True:
            mensagem = input("Digite sua mensagem: ")
            await websocket.send(mensagem)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(cliente())
