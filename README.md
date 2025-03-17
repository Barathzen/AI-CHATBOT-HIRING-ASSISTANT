# AI-CHATBOT-HIRING-ASSISTANT
Intelligent Hiring Assistant chatbot for "TalentScout," a fictional recruitment agency specializing in technology placements.

# TalentScout Hiring Assistant Chatbot

A Streamlit-based chatbot for initial candidate screening using Google’s Gemini 1.5 Flash model.

## Setup
1. Clone the repository:

   git clone <repo-url>
   cd TalentScoutChatbot

2. Install dependencies:

   pip install -r requirements.txt

3. Set up your Google API key:

   Add it to a .env file as GOOGLE_API_KEY=your_api_key.

4. streamlit run main.py



---

### How It Works
1. **Run the App**: Execute `streamlit run main.py` in your terminal.
2. **Interact**: Open the browser (usually at `http://localhost:8501`) and start chatting.
3. **Flow**:
   - The chatbot greets you and asks for your full name.
   - It collects all required info step-by-step.
   - After gathering the tech stack, it generates and asks technical questions.
   - Type "exit" to end the conversation.

---

### Notes
- **Gemini API**: Ensure you have a valid API key from Google Cloud. Replace `GOOGLE_API_KEY` in the `.env` file.
- **Data Privacy**: This demo stores data in memory (session state). For production, use a secure database and implement GDPR-compliant practices.
- **Deployment**: For a cloud demo, consider AWS Elastic Beanstalk or Google Cloud Run. Provide a live link if deployed.

This implementation meets all requirements and provides a solid foundation for further enhancements! Let me know if you need help with deployment or additional features.
