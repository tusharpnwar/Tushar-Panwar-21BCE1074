# Turn-Based Chess-Like Game with WebSocket Communication

**Author:** Tushar Panwar 21BCE1074

## Project Overview

The Turn-Based Chess-Like Game is a real-time strategy game implemented with WebSocket communication. Players control characters on a 5x5 grid, taking turns to move and interact based on predefined rules. The project includes both server and client components, enabling real-time updates and gameplay through WebSocket protocols.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technical Details](#technical-details)
6. [Troubleshooting](#troubleshooting)
7. [Future Enhancements](#future-enhancements)
8. [License](#license)
9. [Contact](#contact)

## Introduction

This game simulates a chess-like environment where players move characters on a grid and attempt to outmaneuver their opponent. The game state and moves are communicated in real-time using WebSocket technology, ensuring a seamless multiplayer experience.

## Features

- **Real-Time Communication:** WebSocket-based updates for game state and player actions.
- **Game Logic:** Implementation of move validation, turn-based mechanics, and game state management.
- **Client Interface:** Interactive web-based UI to start the game, make moves, and view the game board.
- **Turn-Based Gameplay:** Alternates turns between players, with real-time updates on moves and game state.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/tusharpnwar/turn_based_game.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd turn_based_game
    ```
3. **Install the required Python packages:**
    ```bash
    pip install websockets
    ```
4. **Navigate to the server directory:**
    ```bash
    cd server
    ```
5. **Start the WebSocket server:**
    ```bash
    python websocket_server.py
    ```

## Usage

1. **Open the Client:**
    - Open `index.html` in a web browser. You can use a local server or open it directly from your file system. For a local server:
    ```bash
    npx http-server client
    ```

2. **Start the Game:**
    - Click the "Start Game" button in the client interface to initialize the game with predefined characters.

3. **Play the Game:**
    - Use the client interface to make moves and view updates on the game board.

## Technical Details

1. **Server-Side:** Implements game logic, handles WebSocket connections, and manages real-time updates.
2. **Client-Side:** Provides the user interface for interacting with the game, including sending moves and displaying the game board.
3. **WebSocket Communication:** Handles real-time bidirectional communication between the client and server.

## Troubleshooting

- **WebSocket Connection Issues:** Ensure the server is running on port 6789. Update the WebSocket URL in `app.js` if the port is different.
- **Client Not Updating:** Verify the server is active and check the browser console for errors.

## Future Enhancements

- Implement additional character types with unique abilities.
- Add AI opponents or a spectator mode.
- Develop a chat feature and move history tracking.
- Introduce ranking and replay functionalities.


## Contact

For any questions or feedback, please contact **Tushar Panwar** at **[tusharpanwar01872@gmail.com]**.
