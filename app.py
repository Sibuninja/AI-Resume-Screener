import streamlit as st
import os
import pandas as pd
from resume_parser import extract_text_from_pdf, extract_skills
from job_matcher import match_resume_to_job
from jd_parser import extract_jd_skills

# Load job description
with open("sample_job_desc.txt", "r") as f:
    job_desc = f.read()

jd_skills = extract_jd_skills(job_desc)

st.title("📄 AI Resume Screener")
st.write("Screen resumes in the `resumes/` folder against the job description.")

st.subheader("Job Description Skills Extracted:")
st.write(", ".join(jd_skills))

# User sets match threshold
threshold = st.slider("Set minimum match % to shortlist candidates", 0, 100, 50)

if st.button("Run Screening"):
    results = []
    resumes_path = "resumes"

    for file_name in os.listdir(resumes_path):
        if file_name.lower().endswith(".pdf"):
            file_path = os.path.join(resumes_path, file_name)

            resume_text = extract_text_from_pdf(file_path)
            resume_skills = extract_skills(resume_text, jd_skills)

            # Calculate score with skills passed
            match_score = match_resume_to_job(resume_text, job_desc, jd_skills)

            # Skill matching breakdown
            matched = [s for s in jd_skills if s.lower() in resume_text.lower()]
            missing = [s for s in jd_skills if s.lower() not in resume_text.lower()]

            results.append({
                "Candidate": file_name,
                "Match %": round(match_score, 2),
                "Matched Skills": ", ".join(matched) if matched else "None",
                "Missing Skills": ", ".join(missing) if missing else "None"
            })

    # Sort by best match
    results = sorted(results, key=lambda x: x["Match %"], reverse=True)

    # Convert to DataFrame
    df = pd.DataFrame(results)

    # Apply threshold filter
    df_filtered = df[df["Match %"] >= threshold]

    st.subheader("📊 Shortlisted Candidates")
    st.dataframe(df_filtered)

    csv = df_filtered.to_csv(index=False).encode("utf-8")
    st.download_button("Download Results", csv, "results.csv", "text/csv")

    st.subheader("📋 All Candidates (for reference)")
    st.dataframe(df)
