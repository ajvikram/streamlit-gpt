#!/usr/bin/env python

import streamlit as st
from gpt4allj import Model
st.set_page_config(layout='wide')
from streamlit_option_menu import option_menu

model = Model('./model/ggml-gpt4all-j.bin')

def show_messages(text):
    messages_str = [
        f"{_['role']}: {_['content']}" for _ in st.session_state["messages"][1:]
    ]
    text.text_area("Messages", value=str("\n".join(messages_str)), height=400)

with st.sidebar:
    choose = option_menu("Streamlit GPT", [ "GPT Play Ground","About","Contact"],
                         icons=['kanban', 'book', 'person lines fill'],
                         menu_icon="cast", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "#262730"},
                             "icon": {"color": "#02ab21", "font-size": "25px"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                          "--hover-color": "#56755c"},
                             "nav-link-selected": {"background-color": "#2f5335"},
                         }
                         )
if choose == "About":
    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Cooper Black'; color: #02ab21;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About the Streamlit GPT </p>', unsafe_allow_html=True)

    st.write("This application uses GPT4ALL-J to generate answers for the questions.")

elif choose == "GPT Play Ground":
    st.markdown(""" <style> .font {
                font-size:30px ; font-family: 'Cooper Black'; color: #02ab21;} 
                </style> """, unsafe_allow_html=True)

    BASE_PROMPT = [{"role": "AI", "content": "You are a helpful assistant."}]

    if "messages" not in st.session_state:
        st.session_state["messages"] = BASE_PROMPT

    st.markdown(""" <style> .font {
                        font-size:30px ; font-family: 'Cooper Black'; color: #02ab21;} 
                        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">GPT4 Play Ground :</p>', unsafe_allow_html=True)

    text = st.empty()
    show_messages(text)

    prompt = st.text_input("Prompt:", value="Enter your message here...")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Send"):
            with st.spinner("Generating response..."):
                st.session_state["messages"] += [{"role": "You", "content": prompt}]
                print(st.session_state["messages"][-1]["content"])
                message_response = model.generate(st.session_state["messages"][-1]["content"])
                st.session_state["messages"] += [
                    {"role": "AI", "content": message_response}
                ]
                show_messages(text)
    with col2:
        if st.button("Clear"):
            st.session_state["messages"] = BASE_PROMPT
            show_messages(text)


elif choose == "Contact":
    st.markdown(""" <style> .font {
            font-size:30px ; font-family: 'Cooper Black'; color: #02ab21;} 
            </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact </p>', unsafe_allow_html=True)

    st.write("Contact to ....")


