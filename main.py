import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

def init():
    load_dotenv()

    if os.getenv('OPENAI_API_KEY') is None or os.getenv("OPENAI_API_KEY") == "":
        print('OPENAI_API_KEY is not exist')
        exit(1)
    else:
        print('OPENAI_API_KEY is set')

    st.set_page_config(
        page_title="Your own ChatGPT 🤖",
        page_icon="🤖",
    )

    st.header('Your own ChatGPT 🤖')


def main():
    init()

    chat = ChatOpenAI(temperature=0)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    with st.sidebar:
        user_input = st.text_input('Your message: ', key="user_input")

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))  # append user's message into list
        with st.spinner():
            response = chat(st.session_state.messages)   # retrieving AI's answer

        st.session_state.messages.append(AIMessage(content=response.content))  # append AI's message into list

    messages = st.session_state.get('messages', [])

    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')

if __name__ == '__main__':
    main()