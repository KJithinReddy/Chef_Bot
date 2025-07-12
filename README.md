# 👨‍🍳 Chef Bot

Welcome to Chef Bot — your personal AI-powered kitchen assistant!  
Chef Bot helps you cook any dish, get ingredients, find substitutions, and answer all your culinary questions via an intuitive chat interface.

------------------------------------------------------------

🧠 HOW IT WORKS

Chef Bot is powered by:
- LangChain Tools: For defining cooking-related functions like recipes and ingredient help
- LangGraph: To manage chat as a state machine with memory
- Groq LLaMA 3: As the backend language model
- Streamlit: For a clean, interactive user interface
- dotenv: For secure key management

------------------------------------------------------------

🍴 FEATURES

- Ask how to cook any dish
- Get detailed ingredient lists
- Get cooking advice or ingredient substitutions
- Memory-based conversation using LangGraph’s StateGraph
- Fast response using Groq’s blazing-fast inference

------------------------------------------------------------

🔧 INSTALLATION

1. Clone the repository:

   git clone https://github.com/yourusername/chef-bot.git
   cd chef-bot

2. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate

3. Install dependencies:

   pip install -r requirements.txt

4. Create a `.env` file and add your Groq API key:

   GROQ_API_KEY=your_groq_api_key_here

------------------------------------------------------------

▶️ RUN THE APP

   streamlit run app.py

------------------------------------------------------------

📂 FILE STRUCTURE

- `chef_bot.py` → LangGraph agent definition, state setup, cooking tools
- `app.py` → Streamlit frontend and user interface
- `.env` → Environment variable file (not tracked in Git)
- `requirements.txt` → Python dependencies

------------------------------------------------------------

📦 requirements.txt

streamlit  
langchain  
langchain-community  
langchain-groq  
langgraph  
python-dotenv

------------------------------------------------------------

💡 FUTURE IMPROVEMENTS

- Add image-based recipe generation  
- Include step timers or voice mode  
- Store favorite recipes in local cache  
- Extend memory to multi-day conversations  
- Add nutritional info per dish

------------------------------------------------------------

Built using LangGraph, LangChain, Groq, and Streamlit.
