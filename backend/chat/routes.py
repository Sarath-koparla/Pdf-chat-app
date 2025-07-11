from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from auth.dependencies import get_current_user
from utils.blob import upload_pdf_to_blob

router = APIRouter(
    prefix="",  # optional
    tags=["PDF Upload"],
    dependencies=[Depends(get_current_user)]  # ✅ JWT auth required for all routes in this file
)

@router.post("/upload-pdf/")
async def upload_pdf(
    file: UploadFile = File(...)
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed.")

    blob_url = await upload_pdf_to_blob(file)

    return {
        "message": "PDF uploaded successfully",
        "file_url": blob_url,
        # 🔐 You can extract current user here too, but if you want email:
        # "uploaded_by": current_user["email"]
    }
