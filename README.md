# 👨‍🍳 Chef Bot

Welcome to Chef Bot, your personal AI-powered kitchen assistant!  
This application uses LangGraph and Streamlit to help users cook dishes, find ingredients, and get helpful cooking advice — all through a conversational interface.

----------------------------------------

HOW IT WORKS

Chef Bot leverages:
- LangGraph: For managing multi-turn dialogue as a state machine
- LangChain tools: For defining cooking-related functions
- Streamlit: As the interactive user interface
- Groq LLaMA 3: As the large language model backend

----------------------------------------

FEATURES

- Ask how to cook any dish
- Get ingredient lists for recipes
- Get cooking advice or substitutions
- Memory-based conversations powered by LangGraph

----------------------------------------

GETTING STARTED

INSTALLATION

1. Clone the repository:

   git clone https://github.com/yourusername/chef-bot.git
   cd chef-bot

2. Create a virtual environment and activate it:

   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install dependencies:

   pip install -r requirements.txt

4. Set up environment variables:

   Create a .env file in the root directory and add:

   GROQ_API_KEY=your_groq_api_key_here

----------------------------------------

RUN THE APP

   streamlit run app.py

----------------------------------------

Happy cooking! 🍜
