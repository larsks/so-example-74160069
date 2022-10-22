import fastapi
import redis
import socket
import sys
import time

app = fastapi.FastAPI()

while True:
    try:
        db = redis.Redis(host="redisdb", port=6379, db=0)
        db.set("color", "blue")
    except (redis.exceptions.ConnectionError, socket.gaierror):
        print('waiting for redis', file=sys.stderr)
        time.sleep(1)
    else:
        break


@app.get("/")
async def root():
    color = db.get("color")
    return {"color": color}
