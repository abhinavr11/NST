import streamlit as st
from streamlit_chat import message as st_message
import json, requests

st.title("Neural Style Transfer ")

url = 'http://47df-35-202-214-147.ngrok.io/' # needs to changed



if "history" not in st.session_state:
    st.session_state.history = []

def generate_answer():
    
    user_message = st.session_state.input_text
    msg = {'message': user_message }
    msg  = json.dumps(msg)
    x = requests.post(url, data = msg)
    
    message_bot = x.json()['results']

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})


st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat)  # unpacking