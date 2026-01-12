import streamlit as st
import requests

st.set_page_config(page_title="Prompt Refiner AI", layout="wide")

# ---------- Header ----------
st.markdown("## 🧠 Multi-Modal Prompt Refinement System")
st.markdown("Turn messy ideas, documents & images into clean AI-ready prompts.")
st.divider()

# ---------- INPUT ----------
st.subheader("📥 Input")

text = st.text_area(
    "Describe your idea",
    height=120,
    placeholder="E.g. i want an app for docter appoinment booking..."
)

file = st.file_uploader("Upload Image / PDF / DOCX")

if st.button("✨ Refine Prompt", use_container_width=True):
    with st.spinner("Refining your input..."):
        files = {}
        data = {"text": text}

        if file:
            files["file"] = (file.name, file.getvalue())

        try:
            response = requests.post(
                "http://127.0.0.1:8000/refine",
                data=data,
                files=files
            )

            if response.status_code == 200:
                st.session_state["result"] = response.json()
            else:
                st.error("Backend error.")
        except:
            st.error("Could not connect to backend.")

st.divider()

# ---------- OUTPUT ----------
if "result" in st.session_state:
    result = st.session_state["result"]

    if "status" in result and result["status"] == "rejected":
        st.error(result["reason"])
    else:
        # -------- AI READY PROMPT --------
        refined_prompt = f"""
Product: {result["product_intent"]}
Target Users: {result["target_user"]}

Features:
""" + "\n".join(f"- {f}" for f in result["core_features"]) + """

Constraints:
""" + "\n".join(f"- {c}" for c in result["technical_constraints"]) + """

Expected Outputs:
""" + "\n".join(f"- {o}" for o in result["expected_outputs"])

        st.subheader("🧠 AI-Ready Prompt")
        st.text_area("Copy this prompt into any AI", refined_prompt, height=600)

        st.divider()

        # -------- STRUCTURED JSON --------
        st.subheader("🧾 Structured JSON")
        st.json(result)
