import spacy

nlp = spacy.load("en_core_web_sm")

# Simple predefined list of possible skills
COMMON_SKILLS = [
    "python", "java", "c++", "sql", "excel", "machine learning",
    "deep learning", "nlp", "django", "flask", "data analysis",
    "project management", "communication", "leadership",
    "cloud", "aws", "docker", "kubernetes"
]

# Extract skills from job description
def extract_jd_skills(job_desc):
    doc = nlp(job_desc.lower())
    found = []
    for token in doc:
        if token.text in COMMON_SKILLS:
            found.append(token.text)
    return list(set(found))
