from faker import Faker
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random, os

fake = Faker()

# Skill pools by role
skills_ai_ml = [
    "Python", "TensorFlow", "PyTorch", "Scikit-learn", "Hugging Face", "NLP",
    "Computer Vision", "OpenCV", "Deep Learning", "RAG", "LLMs", "FastAPI", "SQL"
]

skills_web_dev = [
    "JavaScript", "HTML", "CSS", "React", "Node.js", "Express", "MongoDB",
    "Django", "Flask", "REST APIs", "GraphQL", "Docker", "AWS"
]

skills_data_analyst = [
    "SQL", "Excel", "PowerBI", "Tableau", "Python", "Pandas", "NumPy",
    "Statistics", "Data Visualization", "ETL", "Data Warehousing", "R"
]

# Ensure resumes folder exists
os.makedirs("resumes", exist_ok=True)

def make_resume(file_path, name, email, phone, address, summary, picked_skills, exp_lines, edu):
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, name)
    c.setFont("Helvetica", 10)
    c.drawString(100, 735, f"Email: {email} | Phone: {phone}")
    c.drawString(100, 720, f"Address: {address}")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 700, "Professional Summary:")
    c.setFont("Helvetica", 10)
    c.drawString(100, 685, summary)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 660, "Skills:")
    c.setFont("Helvetica", 10)
    c.drawString(100, 645, ", ".join(picked_skills))

    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 620, "Experience:")
    c.setFont("Helvetica", 10)
    text_object = c.beginText(100, 605)
    for line in exp_lines:
        text_object.textLine(line)
    c.drawText(text_object)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 570, "Education:")
    c.setFont("Helvetica", 10)
    c.drawString(100, 555, edu)

    c.save()


def generate_resumes(count, role, skills_pool, start_index):
    for i in range(start_index, start_index + count):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        address = fake.address().replace("\n", ", ")

        exp_years = random.randint(0, 5)
        picked_skills = random.sample(skills_pool, k=random.randint(6, 10))

        summary = f"{role} with {exp_years} years of experience in {', '.join(random.sample(skills_pool, 3))}."
        exp_lines = [
            f"- Developed projects using {random.choice(skills_pool)} and {random.choice(skills_pool)}.",
            f"- Improved efficiency by applying {random.choice(skills_pool)} techniques.",
            f"- Collaborated in teams using Agile practices."
        ]
        edu = "B.Tech in Computer Science"

        file_path = f"resumes/Resume_{i}.pdf"
        make_resume(file_path, name, email, phone, address, summary, picked_skills, exp_lines, edu)


# Generate resumes by category
generate_resumes(20, "AI/ML Engineer", skills_ai_ml, 1)
generate_resumes(15, "Web Developer", skills_web_dev, 21)
generate_resumes(15, "Data Analyst", skills_data_analyst, 36)

print("✅ 50 diverse resumes generated inside 'resumes/' folder!")
