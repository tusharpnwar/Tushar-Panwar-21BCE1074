const ws = new WebSocket("ws://localhost:6789");

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    if (data.event === "update") {
        updateBoard(data.state);
    } else if (data.event === "invalid_move") {
        alert("Invalid Move!");
    } else if (data.event === "game_over") {
        alert("Game Over! Winner: " + data.winner);
    }
};

document.getElementById("start-game").onclick = function() {
    const characters = ["P1", "H1", "H2", "P2", "P3"];
    ws.send(JSON.stringify({
        event: "initialize",
        player_id: "A",
        characters: characters
    }));
};

function updateBoard(state) {
    const boardElement = document.getElementById("game-board");
    boardElement.innerHTML = "";
    for (let row = 0; row < state.length; row++) {
        for (let col = 0; col < state[row].length; col++) {
            const cell = document.createElement("div");
            cell.className = "cell";
            if (state[row][col]) {
                const [player, char] = state[row][col].split("-");
                cell.classList.add(`player-${player}`);
                cell.innerText = char;
            }
            boardElement.appendChild(cell);
        }
    }
}
