import streamlit as st
import os
import zipfile
import shutil

from prompt_builder import build_prompt
from bedrock_client import convert_cpp_to_python

st.set_page_config(page_title="AI Code Migration Tool", layout="wide")

st.title("AI C++ → Python Migration Platform")

st.write("Upload a C++ file or an entire repository to convert it into Python using AWS Bedrock")

UPLOAD_FOLDER = "uploaded_repo"

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# choose upload type
upload_type = st.radio(
    "Choose input type",
    ["Single C++ File", "C++ Repository (.zip)"]
)

cpp_code = ""

# ----------------------------------------------------
# SINGLE FILE UPLOAD
# ----------------------------------------------------

if upload_type == "Single C++ File":

    uploaded_file = st.file_uploader("Upload C++ File", type=["cpp", "h"])

    if uploaded_file:

        cpp_code = uploaded_file.read().decode("utf-8", errors="ignore")

        st.subheader("Uploaded C++ Code")

        st.code(cpp_code, language="cpp")


# ----------------------------------------------------
# REPOSITORY UPLOAD
# ----------------------------------------------------

if upload_type == "C++ Repository (.zip)":

    uploaded_repo = st.file_uploader("Upload ZIP Repository", type=["zip"])

    if uploaded_repo:

        # clean old repo
        if os.path.exists(UPLOAD_FOLDER):
            shutil.rmtree(UPLOAD_FOLDER)

        os.makedirs(UPLOAD_FOLDER)

        zip_path = os.path.join(UPLOAD_FOLDER, "repo.zip")

        with open(zip_path, "wb") as f:
            f.write(uploaded_repo.read())

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(UPLOAD_FOLDER)

        st.success("Repository extracted successfully")

        repo_code = ""

        for root, dirs, files in os.walk(UPLOAD_FOLDER):

            for file in files:

                if file.endswith(".cpp") or file.endswith(".h"):

                    path = os.path.join(root, file)

                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        code = f.read()

                    repo_code += f"\nFILE: {file}\n"
                    repo_code += code

        cpp_code = repo_code

        st.subheader("Detected Repository Code")

        st.code(repo_code[:3000], language="cpp")


# ----------------------------------------------------
# RUN MIGRATION
# ----------------------------------------------------

if cpp_code != "":

    with open("skill.md") as f:
        skill = f.read()

    prompt = build_prompt(cpp_code, skill)

    if st.button("Run AI Migration"):

        with st.spinner("Converting using AWS Bedrock Claude..."):

            python_code, input_tokens, output_tokens, latency = convert_cpp_to_python(prompt)

        # ------------------------------------------------
        # CLEAN MARKDOWN OUTPUT FROM LLM
        # ------------------------------------------------

        python_code = python_code.replace("```python", "")
        python_code = python_code.replace("```", "")
        python_code = python_code.strip()

        # ------------------------------------------------
        # DISPLAY OUTPUT
        # ------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("C++ Input")
            st.code(cpp_code[:3000], language="cpp")

        with col2:
            st.subheader("Python Output")
            st.code(python_code, language="python")

        # ------------------------------------------------
        # DOWNLOAD BUTTON
        # ------------------------------------------------

        st.download_button(
            label="Download Python Code",
            data=python_code,
            file_name="converted_code.py",
            mime="text/plain"
        )

        st.divider()

        # ------------------------------------------------
        # METRICS
        # ------------------------------------------------

        st.subheader("Migration Metrics")

        m1, m2, m3 = st.columns(3)

        m1.metric("Input Tokens", input_tokens)
        m2.metric("Output Tokens", output_tokens)
        m3.metric("Latency (seconds)", round(latency, 2))