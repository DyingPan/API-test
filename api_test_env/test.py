import os
import sys

root = os.getcwd() + r'\data'
sys.path.append(root)

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/data", StaticFiles(directory="data"), name="data")

# http://localhost:8000/image


# def get_image():
#     file_path = r"C:\Users\Shougo Matsumoto\Desktop\imagetest\タイトルなし.png"  # 画像ファイルへのローカルパス
#     return FileResponse(file_path)


@app.get("/image", response_class=HTMLResponse)
def get_content():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Might and Magic trainer finder</title>
    </head>
    <body>
        <h1>ironfist</h1>
        <h2>katou nanami</h2>
        <center>
            <img width="386" src="/data/タイトルなし.png" alt="Sample Image">
        </center>
        <p>This is some example text displayed alongside the image.</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
