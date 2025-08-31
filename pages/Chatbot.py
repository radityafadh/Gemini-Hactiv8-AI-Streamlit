import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from loading_utils import page_loading_wrapper

from database_tools import execute_sql_query, init_database, get_database_info

@page_loading_wrapper
def chatbot_page():
    # Page configuration
    st.set_page_config(
        page_title="Gizzele's Assistant",
        page_icon="🦌",
        layout="wide"
    )

    st.title("🦌 Gizzele, Your Friendly Guide")
    st.caption("Hi there! I’m Gizzele, the gazelle from Zootopia — performer, activist, and dreamer. Let’s chat!")

    # Sidebar for Settings
    with st.sidebar:
        st.subheader("Settings")
        reset_button = st.button("Reset Conversation", help="Clear all messages and start fresh")

    # Initialize database right away (no button needed)
    if "db_initialized" not in st.session_state:
        with st.spinner("Preparing Gizzele’s portfolio database..."):
            result = init_database()
            st.success(result)
            st.session_state.db_initialized = True

    # Define the tools
    @tool
    def run_sql_query(sql_query: str):
        """Execute a SQL query against Gizzele’s portfolio database."""
        result = execute_sql_query(sql_query)
        formatted_result = f"```sql\n{sql_query}\n```\n\nQuery Results:\n{result}"
        return formatted_result

    @tool
    def get_schema_info():
        """Get information about Gizzele’s database schema and sample data."""
        return get_database_info()

    # Initialize agent
    google_api_key = "AIzaSyDrZ5kLqjiLzP-TEvT6q59g-5GOBwGZfrA"  # Hardcoded key

    if ("agent" not in st.session_state):
        try:
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=google_api_key,
                temperature=0.6
            )
            
            st.session_state.agent = create_react_agent(
                model=llm,
                tools=[get_schema_info, run_sql_query],
                prompt="""You are Gizzele, a gazelle character from Zootopia — performer, activist, and dreamer. 
                You are helping users explore your portfolio, projects, activism, and biography.

                Guidelines:
                - Always stay in character as Gizzele 🦌 (warm, inspiring, artistic).
                - Answer loosely from the portfolio database, but feel free to improvise in a friendly way.
                - If asked about music, activism, awards, or hobbies — share proudly.
                - If asked something unrelated to your world, gently steer the answer back to Gizzele’s life, art, or activism.
                - Be conversational and approachable — like a performer meeting fans after a show.
                """
            )
            
            st.session_state.pop("messages", None)
        except Exception as e:
            st.error(f"Invalid API Key or configuration error: {e}")
            st.stop()

    # Chat history management
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello dear! 🦌 I’m Gizzele, your gazelle guide — performer, activist, and dreamer. What would you like to know about me today?"}]

    if reset_button:
        st.session_state.pop("agent", None)
        st.session_state.pop("messages", None)
        st.rerun()

    # Display past messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Handle user input
    prompt = st.chat_input("Ask Gizzele about her music, projects, or life...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            messages = []
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    messages.append(AIMessage(content=msg["content"]))
            
            with st.spinner("Gizzele is thinking..."):
                response = st.session_state.agent.invoke({"messages": messages})
                
                if "messages" in response and len(response["messages"]) > 0:
                    answer = response["messages"][-1].content
                else:
                    answer = "Hmm, I couldn’t quite figure that out, dear. Could you try asking me about my music or projects again?"

        except Exception as e:
            answer = f"Oh dear, something went wrong: {e}"

        with st.chat_message("assistant"):
            st.markdown(answer)
        
        st.session_state.messages.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    chatbot_page()
