import asyncio
import websockets


async def handle_connection(websocket):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)


async def main():
    server = await websockets.serve(
        handle_connection,
        "localhost",
        8765
    )

    print("WebSocket сервер запущен на ws://localhost:8765")

    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())