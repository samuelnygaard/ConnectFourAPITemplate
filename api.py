
import uvicorn
import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from utilities.utilities import get_uptime
from utilities.environment import Environment
from utilities.logging.config import initialize_logging, initialize_logging_middleware

from ml.emily import Emily
from static.render import render
from starlette.responses import HTMLResponse


emily = Emily()

# --- Welcome to your Emily API! --- #
# See the README for guides on how to test it.

# Your API endpoints under http://yourdomain/api/...
# are accessible from any origin by default.
# Make sure to restrict access below to origins you
# trust before deploying your API to production.

app = FastAPI()

initialize_logging()
initialize_logging_middleware(app)

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


@app.post('/api/nextmove')
def nextmove(game: GameItem):

    # Select random column to drop piece into
    board_width = len(game.board[0])
    column = random.randint(0, board_width-1)

    # TODO: Implement clever connect four agent here

    return {'response': column}


@app.get('/api/getname')
def getname():

    # TODO: Set your agent's name here
    name = "AgentName"
    return {'response': name}


if __name__ == '__main__':
    uvicorn.run(
        'api:app',
        host="127.0.0.1",
        port=5000
    )

