# 📄 AI Resume Screener

An **AI-powered Resume Screening System** built with **Python + Streamlit**.  
It parses resumes, extracts key details, compares them with a **Job Description (JD)**, and ranks candidates with **transparent explanations**.  

---

## 🚀 Features
- ✅ Bulk-parse resumes from the `resumes/` folder  
- ✅ Supports **PDF** and **DOCX** resumes  
- ✅ Extracts **Name, Email, Phone, Skills, Education, Years of Experience**  
- ✅ Uses **Hybrid Scoring** → (Skills Overlap + TF-IDF semantic similarity)  
- ✅ Shows **Matched Skills** (green) and **Missing Skills** (red)  
- ✅ Shortlists candidates with a **threshold slider**  
- ✅ Export shortlisted results to **CSV**  
- ✅ (Optional) OCR for scanned resumes  

---

## 🏗 Project Structure

AI-Resume-Screener/
│
├── backend/
│ ├── parsers.py # Resume parsing (PyResParser + fallback)
│ ├── embeddings.py # Sentence-transformers embeddings
│ ├── scoring.py # Candidate scoring logic
│ ├── jd_parser.py # Extract skills from JD
│ └── requirements.txt # Dependencies
│
├── frontend/
│ └── app.py # Streamlit web UI
│
├── resumes/ # Place resumes here
├── sample_job_desc.txt # Paste your JD here
├── run.bat / run.sh # Quick start scripts
└── README.md # Project documentation

yaml
Copy
Edit

---

📊 Output (Screenshots)
🔹 Dashboard Home


🔹 Candidate Screening


🔹 Shortlist Export


---
## ⚙️ Installation

1. **Clone repo & setup venv**
   ```bash
   git clone https://github.com/your-username/AI-Resume-Screener.git
   cd AI-Resume-Screener
   python -m venv venv
   venv\Scripts\activate   # (Windows)
   source venv/bin/activate # (Mac/Linux)
Install dependencies

bash
Copy
Edit
pip install -r backend/requirements.txt
(Optional) For OCR support

bash
Copy
Edit
pip install pytesseract pdf2image pillow
▶️ Usage
Place resumes in the resumes/ folder (PDF or DOCX).

Paste a job description in sample_job_desc.txt.

Run the app:

bash
Copy
Edit
streamlit run frontend/app.py
Open browser at http://localhost:8501

📊 Output
Ranks resumes against the JD (0–100%)

Displays each candidate with:

Name & File

Match %

✅ Matched Skills (green)

❌ Missing Skills (red)

Shortlisted candidates can be downloaded as CSV

🔮 Future Improvements
Use transformer embeddings (e.g. BERT) for deeper semantic match

Add charts & analytics (leaderboard of top candidates)

Integrate with ATS / HR platforms

Fine-tune a custom Resume → JD relevance mode
