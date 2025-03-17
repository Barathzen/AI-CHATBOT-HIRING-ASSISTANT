import google.generativeai as genai
from utils import generate_technical_questions
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")  # Replace with your API key or use .env
genai.configure(api_key=API_KEY)

class TalentScoutChatbot:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.state = "greeting"  # Tracks conversation state
        self.required_info = [
            "Full Name", "Email Address", "Phone Number", "Years of Experience",
            "Desired Position(s)", "Current Location", "Tech Stack"
        ]
        self.current_info_index = 0

    def process_input(self, user_input, candidate_info):
        # End conversation if user says goodbye
        if any(keyword in user_input.lower() for keyword in ["exit", "bye", "goodbye"]):
            if len(candidate_info) == len(self.required_info):
                return "Thank you for your time! A recruiter will review your information and get back to you soon."
            else:
                return "It seems we haven't finished collecting your info. Would you like to continue?"

        # Handle conversation based on state
        if self.state == "greeting":
            response = "Hello! I'm TalentScout's Hiring Assistant. I'm here to collect your details and assess your technical skills for tech placements. Let's start with your full name."
            self.state = "collecting_info"
            return response

        elif self.state == "collecting_info":
            if self.current_info_index < len(self.required_info):
                field = self.required_info[self.current_info_index]
                candidate_info[field] = user_input
                self.current_info_index += 1

                if self.current_info_index < len(self.required_info):
                    return f"Great, thanks! Now, please provide your {self.required_info[self.current_info_index].lower()}."
                else:
                    self.state = "tech_questions"
                    return "Thanks for providing your details! Now, let’s move on to some technical questions based on your tech stack. Please list your tech stack again for confirmation."

        elif self.state == "tech_questions":
            tech_stack = user_input.split(", ")
            questions = generate_technical_questions(tech_stack)
            self.state = "asking_questions"
            self.questions = questions
            self.current_question_index = 0
            return f"Based on your tech stack ({user_input}), here’s your first question:\n\n{questions[0]}"

        elif self.state == "asking_questions":
            self.current_question_index += 1
            if self.current_question_index < len(self.questions):
                return f"Next question:\n\n{self.questions[self.current_question_index]}"
            else:
                self.state = "done"
                return "That’s all for the technical questions! Thank you for your responses. Anything else you’d like to add before we wrap up?"

        elif self.state == "done":
            return "Thanks for the additional info! We’re all set. A recruiter will review your profile soon. Type 'exit' to end the conversation."

        return "I’m not sure how to proceed. Could you please clarify your input?"
