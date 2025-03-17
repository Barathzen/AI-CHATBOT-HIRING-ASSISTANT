import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

def generate_technical_questions(tech_stack):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    Generate 3-5 technical questions to assess a candidate’s proficiency in the following tech stack: {', '.join(tech_stack)}.
    Ensure the questions are specific, relevant, and appropriately challenging for an intermediate-level candidate.
    Return the questions as a numbered list.
    """
    response = model.generate_content(prompt)
    questions = response.text.strip().split("\n")
    return [q.strip() for q in questions if q.strip()]