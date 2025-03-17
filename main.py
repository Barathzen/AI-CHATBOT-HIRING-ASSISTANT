import streamlit as st
from chatbot import TalentScoutChatbot

# Custom CSS for RDR2 theme
def load_css():
    return """
    <style>
        /* RDR2-inspired Western theme */
        @import url('https://fonts.googleapis.com/css2?family=IM+Fell+English+SC&family=Rye&display=swap');
        
        /* Main background and container */
        .main {
            background: linear-gradient(rgba(30, 20, 10, 0.95), rgba(20, 15, 5, 0.9)), 
                        repeating-linear-gradient(45deg, rgba(139, 69, 19, 0.05), rgba(139, 69, 19, 0.05) 10px, 
                        rgba(160, 82, 45, 0.05) 10px, rgba(160, 82, 45, 0.05) 20px);
            color: #e6ccb3;
        }
        
        /* Header styling */
        h1, h2, h3 {
            font-family: 'Rye', cursive !important;
            color: #d4af37 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            border-bottom: 2px solid rgba(139, 69, 19, 0.5);
            padding-bottom: 10px;
            letter-spacing: 1px;
        }
        
        /* Button styling */
        .stButton>button {
            font-family: 'IM Fell English SC', serif !important;
            background-color: #8b4513 !important;
            color: #f5f5dc !important;
            border: 2px solid #d4af37 !important;
            border-radius: 0 !important;
            transition: all 0.3s ease-in-out !important;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }
        
        .stButton>button:hover {
            background-color: #654321 !important;
            border-color: #ffd700 !important;
            transform: scale(1.03);
        }
        
        /* Chat message styling */
        .stChatMessage {
            border: 1px solid rgba(139, 69, 19, 0.6) !important;
            background-color: rgba(30, 20, 10, 0.6) !important;
            backdrop-filter: blur(5px) !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3) !important;
            transition: all 0.3s ease-out;
            transform-style: preserve-3d;
            animation: messageAppear 0.7s ease-out forwards;
        }
        
        /* Chat input styling */
        .stChatInput input {
            background-color: rgba(61, 43, 31, 0.7) !important;
            color: #e6ccb3 !important;
            border: 1px solid #8b4513 !important;
            padding: 10px !important;
            font-family: 'IM Fell English SC', serif !important;
        }
        
        /* 3D animations */
        @keyframes messageAppear {
            0% {
                opacity: 0;
                transform: translateY(10px) rotateX(-10deg);
            }
            100% {
                opacity: 1;
                transform: translateY(0) rotateX(0);
            }
        }
        
        /* Additional decorative elements */
        .main::before {
            content: "";
            position: fixed;
            top: 20px;
            left: 20px;
            right: 20px;
            bottom: 20px;
            border: 8px double rgba(139, 69, 19, 0.4);
            pointer-events: none;
            z-index: 1000;
        }
        
        p, div, span {
            font-family: 'IM Fell English SC', serif !important;
            color: #ddc9a9 !important;
        }
        
        /* Wanted poster style for final message */
        .wanted-poster {
            background-color: rgba(244, 223, 184, 0.9);
            border: 6px double #8b4513;
            padding: 15px;
            text-align: center;
            color: #332211 !important;
            font-family: 'Rye', cursive !important;
            margin: 20px auto;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
            transform-style: preserve-3d;
            animation: paperFloat 3s ease-in-out infinite;
            max-width: 80%;
        }
        
        .wanted-poster p {
            color: #332211 !important;
        }
        
        @keyframes paperFloat {
            0%, 100% { transform: translateY(0) rotate(-1deg); }
            50% { transform: translateY(-5px) rotate(1deg); }
        }
    </style>
    
    <script>
        // Add 3D tilt effect to chat messages
        document.addEventListener('DOMContentLoaded', function() {
            const messages = document.querySelectorAll('.stChatMessage');
            
            messages.forEach(message => {
                message.addEventListener('mousemove', function(e) {
                    const rect = this.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    
                    const xRotation = ((y - rect.height / 2) / rect.height) * 8;
                    const yRotation = ((x - rect.width / 2) / rect.width) * -8;
                    
                    this.style.transform = `perspective(1000px) rotateX(${xRotation}deg) rotateY(${yRotation}deg)`;
                });
                
                message.addEventListener('mouseleave', function() {
                    this.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
                });
            });
        });
    </script>
    """

# Initialize session state for chat history and chatbot instance
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chatbot" not in st.session_state:
    st.session_state.chatbot = TalentScoutChatbot()
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}

# Apply RDR2 theme
st.markdown(load_css(), unsafe_allow_html=True)

# Streamlit UI with themed header
st.markdown('<h1 style="text-align:center;">TalentScout Hiring</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:18px;">Welcome, ! I\'m here to assist with your initial screening. Let\'s get started.</p>', unsafe_allow_html=True)

# Display chat history with animations
for i, message in enumerate(st.session_state.chat_history):
    with st.chat_message(message["role"]):
        animation_delay = i * 0.2
        st.markdown(f"""
        <div style="animation-delay: {animation_delay}s;">{message["content"]}</div>
        """, unsafe_allow_html=True)

# User input
user_input = st.chat_input("Type your response here, comrade...")

if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get chatbot response
    response = st.session_state.chatbot.process_input(user_input, st.session_state.candidate_info)
    
    # Add chatbot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Refresh the page to show the new message
    st.rerun()

# Check for conversation end
if user_input and any(keyword in user_input.lower() for keyword in ["exit", "bye", "goodbye"]) and st.session_state.candidate_info:
    st.markdown("""
    <div class="wanted-poster">
        <h2>MUCH OBLIGED!</h2>
        <p>Your information has been recorded.</p>
        <p>A recruiter will review your qualifications and send word soon.</p>
    </div>
    """, unsafe_allow_html=True)