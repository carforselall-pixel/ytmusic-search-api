from fastapi import FastAPI
from ytmusicapi import YTMusic

app = FastAPI()
yt = YTMusic()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/search")
def search(q: str):
    results = yt.search(q, filter="songs", limit=10)
    return {"results": results}
