import uvicorn
import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from static.render import render
from starlette.responses import HTMLResponse

# --- Welcome to your Emily API! --- #
# See the README for guides on how to test it.

# Your API endpoints under http://yourdomain/api/...
# are accessible from any origin by default.
# Make sure to restrict access below to origins you
# trust before deploying your API to production.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GameItem(BaseModel):
    board: List[List[str]]
    player_symbol: str


@app.post('/api/nextMove')
def nextmove(game: GameItem):

    """
    # Example board:
    [['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', 'O', 'X', 'X', '-', '-']]

    Player symbol is 'O' or 'X' but can be found in game.player_symbol
    """

    # Select random column to drop piece into
    board_width = len(game.board[0])
    column = random.randint(0, board_width - 1)

    # TODO: Implement clever connect four agent here

    return {'response': column}


@app.get('/api/getAgentName')
def getname():
    # TODO: Set your agent's name here
    name = "MyAgentName"
    return {'response': name}


@app.get('/')
def index():
    return HTMLResponse(
        render(
            'static/index.html',
            host="127.0.0.1",
            port=5000
        )
    )


if __name__ == '__main__':
    uvicorn.run(
        'api:app',
        host="127.0.0.1",
        port=5000
    )
