import streamlit as st
from PyPDF2 import PdfReader
from chains import app

st.title("📄 Job Application Helper")

url_input = st.text_input("Job Posting URL:")
resume_file = st.file_uploader("Upload your Resume (PDF):", type="pdf")
submit_button = st.button("Submit")

if submit_button and url_input and resume_file:
    resume_reader = PdfReader(resume_file)
    resume_text = "\n".join(page.extract_text() for page in resume_reader.pages if page.extract_text())
    print("resume",resume_text)
    inputs = {"url": url_input, "resume": resume_text}
    results = app.invoke(inputs)

    st.subheader("Tailored Resume")
    st.markdown(results['tailored_resume'])

    st.subheader("Interview Preparation")
    st.markdown(results['interview_materials'])

elif submit_button:
    st.error("Please provide both the job posting URL and your resume.")