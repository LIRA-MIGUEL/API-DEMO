from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import shutil
from pathlib import Path

app = FastAPI()

# Ruta para guardar las imágenes cargadas
UPLOAD_DIR = "static/imagenes"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

@app.post("/upload/")
async def upload_files(
    files: list[UploadFile] = File(...),
):
    file_paths = []
    for uploaded_file in files:
        file_path = f"{UPLOAD_DIR}/{uploaded_file.filename}"
        with open(file_path, "wb") as file_object:
            shutil.copyfileobj(uploaded_file.file, file_object)
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
