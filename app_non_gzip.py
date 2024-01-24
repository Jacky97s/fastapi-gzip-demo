from fastapi import FastAPI
import json
import uvicorn

# ===================== NON GZIP =====================
app = FastAPI()

@app.get("/")
def non_gzip():
    with open("large-file.json", "r") as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
