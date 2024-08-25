# websocket_server.py

import asyncio
import websockets
import json
from game_logic import Game

# Initialize game logic
game = Game()

connected_users = set()

async def handler(websocket, path):
    # Add new connection
    connected_users.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            if data['type'] == 'initialize':
                game.initialize_game(data['playerId'], data['characters'])
                await broadcast_game_state()
            elif data['type'] == 'move':
                if game.is_valid_turn(data['playerId']):
                    if game.validate_move(data['playerId'], data['charName'], data['move']):
                        game.process_move(data['playerId'], data['charName'], data['move'])
                        await broadcast_game_state()
                        if game.is_game_over():
                            await notify_game_over()
                    else:
                        await websocket.send(json.dumps({'type': 'invalid_move'}))
                else:
                    await websocket.send(json.dumps({'type': 'not_your_turn'}))
    finally:
        # Remove connection
        connected_users.remove(websocket)

async def broadcast_game_state():
    game_state = game.get_game_state()
    message = json.dumps({'type': 'game_state', 'state': game_state})
    # Create a list of tasks to send messages to all connected clients
    tasks = [asyncio.create_task(user.send(message)) for user in connected_users]
    await asyncio.gather(*tasks)

async def notify_game_over():
    message = json.dumps({'type': 'game_over'})
    tasks = [asyncio.create_task(user.send(message)) for user in connected_users]
    await asyncio.gather(*tasks)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
