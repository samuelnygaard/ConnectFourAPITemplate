import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from utilities.environment import Environment
from utilities.logging.config import (initialize_logging,
                                      initialize_logging_middleware)

from static.render import render
from starlette.responses import HTMLResponse
from .agent import Agent

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


@app.post('/api/nextMove')
def nextmove(game: GameItem):
    depth = 5
    return {'response': Agent(game.board, game.player_symbol, depth).next_move(True)}


@app.get('/api/getAgentName')
def getname():
    # TODO: Set your agent's name here
    name = "Team 1: Gudik + Kyrke + Sam"
    return {'response': name}


@app.get('/')
def index():
    return HTMLResponse(
        render(
            'static/index.html',
            host=Environment().HOST_IP,
            port=Environment().CONTAINER_PORT
        )
    )


if __name__ == '__main__':

    uvicorn.run(
        'api:app',
        host=Environment().HOST_IP,
        port=Environment().CONTAINER_PORT
    )