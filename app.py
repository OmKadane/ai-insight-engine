import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env file
load_dotenv()
HF_API_KEY = os.getenv('HF_API_KEY')

# Initialize the Hugging Face client
if HF_API_KEY:
    client = InferenceClient(token=HF_API_KEY)
else:
    client = None

def set_custom_style():
    """Inject custom CSS to style the Streamlit app."""
    # This part injects the CSS for styling and animations
    st.markdown("""
        <style>
            /* Define a glowing animation for button borders/shadows */
            @keyframes rgb-border-glow {
                0% { box-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000; }
                16% { box-shadow: 0 0 5px #ff7f00, 0 0 10px #ff7f00; }
                33% { box-shadow: 0 0 5px #ffff00, 0 0 10px #ffff00; }
                50% { box-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00; }
                66% { box-shadow: 0 0 5px #0000ff, 0 0 10px #0000ff; }
                83% { box-shadow: 0 0 5px #4b0082, 0 0 10px #4b0082; }
                100% { box-shadow: 0 0 5px #ee82ee, 0 0 10px #ee82ee; }
            }

            /* Main app background */
            .stApp {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            /* Main title (Static Color) */
            h1 {
                color: #4CAF50; /* A vibrant green */
                text-align: center;
                font-family: 'Verdana', sans-serif;
                margin-bottom: 2rem;
            }
            /* Text area */
            .stTextArea textarea {
                background-color: #2E2E2E;
                color: #FFFFFF;
                border-radius: 10px;
            }
            /* Radio button labels */
            .stRadio > label {
                font-size: 1.1em;
                font-weight: bold;
                color: #00BFFF; /* Deep sky blue */
            }
            /* Buttons with glowing animation */
            .stButton>button {
                background-color: #2E2E2E;
                color: white;
                border-radius: 10px;
                border: 1px solid #4CAF50;
                padding: 10px 24px;
                font-size: 16px;
                /* Apply the border-glowing animation */
                animation: rgb-border-glow 6s linear infinite;
                cursor: pointer;
            }
            /* Info box for the response */
            .stAlert {
                background-color: #2E2E2E;
                border-radius: 10px;
                border: 1px solid #4CAF50;
            }
        </style>
    """, unsafe_allow_html=True)

def initialize_page():
    """Initialize the Streamlit page configuration and layout"""
    st.set_page_config(
        page_icon="🧠",
        layout="centered"
    )
    st.title("AI Insight Engine")
    return st.columns(1)[0]

def get_user_input(column):
    """Handle user input text area"""
    user_text = column.text_area(
        "Please enter the topics you’re interested in:",
        height=100,
        placeholder="e.g., Natural Language Processing, React state management..."
    )
    return user_text

def create_mcp_server_dropdown():
    """Create a radio button for selecting the response mode"""
    response_modes = {
        "Deep Dive": "technical_summary",
        "AI Toolkit": "ai_resources"
    }
    selected_mode = st.radio(
        "Select Response Mode",
        options=list(response_modes.keys()),
        help="Choose the kind of answer you want"
    )
    return selected_mode

def generate_response(user_text, selected_mode):
    """Generate response using the official Hugging Face InferenceClient"""
    
    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
    
    if selected_mode == 'AI Toolkit':
        prompt_text = f"You are an expert AI assistant. A user is interested in the topic: '{user_text}'. List some popular open-source AI models and datasets from Hugging Face relevant to this topic."
    else: # Deep Dive
        prompt_text = f"You are an expert AI assistant. A user is interested in the topic: '{user_text}'. Provide a clear, technical summary of this concept, as if you were summarizing a codebase or technical documentation."

    try:
        if not client:
            st.error("Hugging Face Access Token not found! Please check your .env file.")
            return

        response = client.chat_completion(
            messages=[{"role": "user", "content": prompt_text}],
            model=model_id,
            max_tokens=1024,
        )
        
        output_text = response.choices[0].message.content
        
        st.info(f"**Response:**\n\n{output_text}")

    except Exception as e:
        st.error(f"An error occurred with the Hugging Face API: {str(e)}")


def main():
    """Main function to run the Streamlit app"""
    set_custom_style()
    
    main_column = initialize_page()
    user_text = get_user_input(main_column)

    with main_column:
        selected_mode = create_mcp_server_dropdown()

    if st.button("Generate Response", key="generate_button"):
        if user_text:
            with st.spinner("Generating response... (This may take a moment)"):
                generate_response(user_text, selected_mode)
        else:
            st.warning("Please enter a topic first.")

if __name__ == "__main__":
    main()