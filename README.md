# **AI Insight Engine 🧠✨**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-blue?style=for-the-badge)](https://huggingface.co/)


A dual-mode AI application built with Streamlit that provides two distinct perspectives on any topic. Choose between a factual **"Deep Dive"** for in-depth summaries or an **"AI Toolkit"** for relevant open-source models and resources.

---

# **🚀 Live Demo**

**[ai-insight-engine](https://ai-insight-engine.streamlit.app/)**

---

# **📸 Interface Highlights**

#### Home Screen
![Home Screen](/assets/home_screen.png)
Clean input panel where users enter prompts and kick off analysis.

#### Response Screen
![Response Screen](/assets/response_screen.png)
Displays AI-powered insights, charts, and context-aware results.

---

## **✨ Features**

* **Dual Response Modes:** Switch between a factual **Deep Dive** and a resourceful **AI Toolkit**.
* **Powered by Open Source:** Leverages powerful, free LLMs from the Hugging Face Hub.
* **Interactive UI:** Built with Streamlit for a fast and responsive user experience.
* **Custom Styling:** Features a custom dark theme with animated elements for a polished look.

---

## **🛠️ Tech Stack**

* **Python**: Core programming language.
* **Streamlit**: For building the interactive web UI.
* **Hugging Face Hub**: For accessing the free LLM via the `InferenceClient`.
* **HTML/CSS**: Injected for custom styling and animations.

---

## **⚙️ Setup and Local Installation**

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/OmKadane/ai-insight-engine.git](https://github.com/OmKadane/ai-insight-engine.git)
    cd ai-insight-engine
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For MacOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

---

## **🔑 Configuration**

Before running the app, you need to provide your Hugging Face Access Token.

1.  Create a file named `.env` in the root of the project folder.
2.  Add your API key to the file in the following format:
    ```
    HF_API_KEY="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```

---

## **▶️ How to Run**

Once the setup and configuration are complete, run the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

## **☁️ Deployment**

This app is deployed on [Streamlit Community Cloud](https://share.streamlit.io). To deploy your own version, simply fork this repository and link it in your Streamlit dashboard. Remember to add your `HF_API_KEY` to the app's secrets!

