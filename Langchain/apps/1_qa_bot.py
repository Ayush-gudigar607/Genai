"""
System Design:
This application is a simple Question-Answering (QA) chatbot built using Streamlit for the user interface, Langchain for AI integration, and Google Generative AI (Gemini model) as the underlying language model. It maintains a chat history in Streamlit's session state and processes user queries by invoking the LLM to generate responses.

Steps Involved:
1. Load environment variables (e.g., API keys) using dotenv.
2. Initialize the ChatGoogleGenerativeAI model with the specified model name.
3. Set up the Streamlit app with a title and introductory markdown.
4. Initialize session state for storing chat messages if not already present.
5. Display the chat history by iterating through stored messages and rendering them in the chat interface.
6. Capture user input via a text input field.
7. If a query is provided, append it to session state and display it as a user message.
8. Invoke the LLM with the query to get a response.
9. Append the AI response to session state and display it in the chat interface.
"""


from dotenv import  load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

st.title("Ask Buddy 💬")
st.markdown("Ask anything to your AI buddy!")


#create a message variable which will store the message
if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)



query=st.text_input("Ask me anything:")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role":"ai","content":res.content})
    