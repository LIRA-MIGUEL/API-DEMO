from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Monta la carpeta "static" para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/upload/")
async def upload_files(files: list[UploadFile] = File(...)):
    file_paths = []
    upload_directory = "static/imagenes"  # Directorio donde se guardarán los archivos

    for uploaded_file in files:
        file_path = os.path.join(upload_directory, uploaded_file.filename)
        with open(file_path, "wb") as file_object:
            file_object.write(uploaded_file.file.read())
        file_paths.append(file_path)

    return {"file_paths": file_paths}

@app.get("/")
async def main():
    content = """
    <body>
    <form action="/upload/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)
