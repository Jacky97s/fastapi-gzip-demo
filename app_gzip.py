from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
import json
import uvicorn

# ===================== GZIP =====================
app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=500)

@app.get("/")
def gzip():
    with open("large-file.json", "r") as file:
        data = json.load(file)

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
