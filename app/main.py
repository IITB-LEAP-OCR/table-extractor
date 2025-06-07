from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os
from tables.main import perform_tsr

app = FastAPI()

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload_file(upload_file: UploadFile) -> str:
    file_path = os.path.join(UPLOAD_DIR, upload_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path

@app.post("/tsr")
async def tsr_endpoint(
    file: UploadFile = File(...),
    structure_only: bool = Form(True)
):
    image_path = save_upload_file(file)
    try:
        result, structured_cells = perform_tsr(
            image_path=image_path,
            table_id=0,
            page_id=0,
            structure_only=False,
            lang="eng"
        )
        return {
            "status": "success",
            "table_structure": result,
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})
