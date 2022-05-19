
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
    board_width: int


@app.post('/api/nextmove')
def nextmove(game: GameItem):
    print(game.board)
    nextMove = random.randint(0, game.board_width-1)
    return {'response': nextMove}


@app.get('/api/getname')
def getname():
    name = "MyName"
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

