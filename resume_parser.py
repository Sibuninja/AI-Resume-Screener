import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

# Extract raw text from resume
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Extract skills based on job description skills
def extract_skills(text, jd_skills):
    doc = nlp(text.lower())
    found_skills = []
    for token in doc:
        if token.text in jd_skills:
            found_skills.append(token.text)
    return list(set(found_skills))
