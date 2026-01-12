# from fastapi import FastAPI

# app = FastAPI(title="Multi-Modal Prompt Refinement API")

# @app.get("/")
# def home():
#     return {"status": "System is running"}

from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os

from extractor import (
    extract_text_from_image,
    extract_text_from_pdf,
    extract_text_from_docx,
    extract_text_from_plain
)

from ai_engine import analyze_input
from refiner import refine
from validator import validate

app = FastAPI(title="Multi-Modal Prompt Refiner")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/refine")
async def refine_prompt(
    text: str = Form(""),
    file: UploadFile = File(None)
):
    input_sources = {"text": False, "image": False, "document": False}
    final_text = ""

    if text:
        final_text += text
        input_sources["text"] = True

    if file:
        path = os.path.join(UPLOAD_DIR, file.filename)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        if file.filename.endswith((".png", ".jpg", ".jpeg")):
            final_text += extract_text_from_image(path)
            input_sources["image"] = True

        elif file.filename.endswith(".pdf"):
            final_text += extract_text_from_pdf(path)
            input_sources["document"] = True

        elif file.filename.endswith(".docx"):
            final_text += extract_text_from_docx(path)
            input_sources["document"] = True

    ai_data = analyze_input(final_text)

    if "status" in ai_data and ai_data["status"] == "rejected":
        return ai_data

    refined = refine(ai_data, input_sources)

    valid, message = validate(refined)

    if not valid:
        return {"status": "rejected", "reason": message}

    return refined
