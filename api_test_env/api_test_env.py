# Third Party Library
import requests
import uvicorn
from bs4 import BeautifulSoup
from fastapi import FastAPI

# http://localhost:8000
app = FastAPI()


@app.get("/")
def process_input(input_value: str):
    # 入力を加工して返す
    processed_value = input_value.upper()
    return {"original": input_value, "processed": processed_value}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
