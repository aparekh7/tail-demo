import asyncio
import websockets

from tail import Tail

HOST = "127.0.0.1"
PORT = 8000
connected = set()


async def on_connect(websocket):
    try:
        tail_gen = Tail("demo.log", num_of_lines=10, follow=True).tail()
        while True:
            try:
                line = next(tail_gen)
                await websocket.send(line)
            except StopIteration:
                pass
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected!")


# async def register(websocket):
#     print("Client Connected!")
#     connected.add(websocket)
#
#     try:
#         await websocket.wait_closed()
#     finally:
#         connected.remove(websocket)
#     # try:
    #     tail_gen = Tail("demo.log", num_of_lines=10, follow=True).tail()
    #     while True:
    #         try:
    #             line = next(tail_gen)
    #             for connection in connected:
    #                 await connection.send(line)
    #         except StopIteration:
    #             pass
    # except websockets.exceptions.ConnectionClosed:
    #     print("Client disconnected!")
    # finally:
    #     connected.remove(websocket)


async def main():
    async with websockets.serve(on_connect, HOST, PORT):
        print(f"Server running on port {PORT}!")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
