import google.generativeai as genai
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

def chat_with_gemini(prompt):
    # Create a model instance
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Generate content
    response = model.generate_content(prompt)
    
    # Return the text response
    return response.text

if __name__ == "__main__":
    while True:
        user_input = input("ME: ")
        if user_input.lower() in ["exit","quit","bye","see ya"]:
            break
        response = chat_with_gemini(user_input)
        print("Chatbot: ", response)

