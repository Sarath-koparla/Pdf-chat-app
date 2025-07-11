# utils/blob.py

from azure.storage.blob.aio import BlobServiceClient
from azure.storage.blob import ContentSettings
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "pdf-files"

async def upload_pdf_to_blob(file):
    unique_filename = f"{uuid.uuid4()}.pdf"
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=unique_filename)
    file_data = await file.read()
    await blob_client.upload_blob(
        file_data,
        overwrite=True,
        content_settings=ContentSettings(content_type="application/pdf")
    )
    return blob_client.url
