import streamlit as st
from utils.embedding import get_embedding
from utils.similarity import rank_resumes
from utils.summarizer import generate_summary  # optional
import PyPDF2
import io

# --- Page Config ---
st.set_page_config(page_title="Candidate Matcher", page_icon="🔍", layout="wide")

# --- Title ---
st.title("🔍 AI-Powered Candidate Matcher")
st.markdown("Match resumes to your job description using semantic similarity.")

# --- Job Description Input ---
st.header(" Job Description")
job_desc = st.text_area("Paste the job description below", height=200)

# --- Resume Upload ---
st.header(" Upload Resumes")
uploaded_files = st.file_uploader(
    "Upload multiple resumes (PDF or TXT)", 
    accept_multiple_files=True, 
    type=["txt", "pdf"]
)

# --- Match Button ---
if st.button(" Match Candidates") and job_desc and uploaded_files:
    with st.spinner("Embedding and analyzing resumes..."):
        job_emb = get_embedding(job_desc)
        resumes = []

        for file in uploaded_files:
            filename = file.name

            if filename.endswith(".txt"):
                try:
                    content = file.read().decode("utf-8")
                except UnicodeDecodeError:
                    st.warning(f"⚠️ Could not decode {filename} as UTF-8.")
                    continue
            elif filename.endswith(".pdf"):
                try:
                    reader = PyPDF2.PdfReader(file)
                    content = ""
                    for page in reader.pages:
                        content += page.extract_text() or ""
                except Exception as e:
                    st.warning(f"⚠️ Could not read {filename} as PDF: {e}")
                    continue
            else:
                st.warning(f"⚠️ Unsupported file type: {filename}")
                continue

            resumes.append((filename, content))

        # --- Ranking & Display ---
        results = rank_resumes(job_emb, resumes)
        st.success(f" Top {len(results)} candidates matched successfully!")

        st.subheader("Top 10 Matched Candidates")
        for name, score, text in results:
            with st.expander(f" {name} — Cosine Similarity: `{score:.3f}`"):
                st.markdown("**Resume Preview:**")
                st.markdown("Candidate Fit Summary:")
                summary = generate_summary(job_desc, text)
                st.info(summary)
