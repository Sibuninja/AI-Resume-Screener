from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def clean_text(text: str) -> str:
    """Lowercase and remove special characters."""
    return re.sub(r"[^a-zA-Z0-9\s]", " ", text.lower())

def match_resume_to_job(resume_text: str, job_desc: str, jd_skills: list[str] = None) -> float:
    """
    Hybrid scoring:
    1. Skill overlap (70%)
    2. Semantic TF-IDF similarity (30%)
    Returns a score between 0–100.
    """
    resume_text = clean_text(resume_text)
    job_desc = clean_text(job_desc)

    # --- Skill match ---
    skill_score = 0
    if jd_skills:
        matched = sum(1 for s in jd_skills if s.lower() in resume_text)
        skill_score = (matched / len(jd_skills)) * 70  # up to 70 points

    # --- Semantic similarity (TF-IDF cosine) ---
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    semantic_score = similarity * 30  # up to 30 points

    # Final score
    return round(min(skill_score + semantic_score, 100), 2)
