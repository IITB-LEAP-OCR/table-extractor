from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os
from tables.main import perform_tsr

app = FastAPI()

UPLOAD_DIR = "/app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload_file(upload_file: UploadFile) -> str:
    file_path = os.path.join(UPLOAD_DIR, upload_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path

@app.post("/tsr")
async def tsr_endpoint(
    file: UploadFile = File(...),
):
    image_path = save_upload_file(file)
    try:
        result, structured_cells = perform_tsr(
            img_file=image_path,
            x1=0,
            y1=0,
            struct_only=False,
            lang="eng"
        )
        print(str(result))
        return {
            "status": "success",
            "table_structure": str(result),
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "table_structure": ""})

@app.get("/health")
async def health_check():
    return {"status": "alive"}
