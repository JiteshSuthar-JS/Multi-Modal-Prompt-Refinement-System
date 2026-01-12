# Multi-Modal-Prompt-Refinement-System

📌 Overview

This project implements a Multi-Modal Prompt Refinement System that converts messy human inputs (text, images, PDFs, or a combination) into a clean, standardized, AI-ready prompt.

It acts as an intelligent bridge between:

unstructured user ideas

and structured instructions required by downstream AI systems.

The system is designed to be LLM-agnostic, modular, and suitable for real-world AI product workflows.

🎯 Problem Statement

Users often provide incomplete, ambiguous, or mixed-format inputs (text + screenshots + documents).
Directly sending such input to AI leads to poor or unreliable outputs.

This system solves that by:

extracting information from multiple formats

using an LLM to interpret meaning

applying deterministic logic to enforce structure, validation, and consistency

🧠 System Architecture
User Input (Text / Image / PDF / DOC)
                ↓
        Input Extractor
      (OCR + Document Readers)
                ↓
           Gemini LLM
     (Intent & Requirement Extraction)
                ↓
        Prompt Refiner
  (Template mapping, assumptions, scoring)
                ↓
            Validator
       (Rejects invalid input)
                ↓
     Final Structured Prompt (JSON)

🧩 Prompt Template

Each refined prompt follows this schema:

{
  "product_intent": "",
  "target_user": "",
  "core_features": [],
  "technical_constraints": [],
  "input_sources": {
    "text": false,
    "image": false,
    "document": false
  },
  "expected_outputs": [],
  "assumptions": [],
  "missing_information": [],
  "confidence_score": 0.0
}


This ensures every request is represented consistently, regardless of how messy the original input was.

🖥️ Frontend

A Streamlit UI is provided where users can:

enter text

upload files (images, PDFs, Word docs)

view the AI-ready prompt

view the structured JSON output

Run it using:

streamlit run frontend.py

🧪 Samples

The /samples folder contains:

5 diverse input files

Their corresponding refined outputs

These demonstrate the system working across:

web apps

mobile apps

AI tools

business software

invalid inputs

🛠 Tech Stack

Python

FastAPI (backend API)

Gemini API (LLM)

Tesseract OCR (image text extraction)

pdfplumber, python-docx (document parsing)

Streamlit (UI)

🚀 How to Run

Start backend:

cd src
uvicorn main:app --reload


Start frontend:

streamlit run frontend.py


Open:

http://localhost:8501

🧠 Key Design Philosophy

AI is used only for understanding content.
All structure, validation, consistency, and safety are enforced through deterministic system design.

This ensures reliability, traceability, and suitability for real AI products.
