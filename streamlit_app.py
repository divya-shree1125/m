import streamlit as st
import pandas as pd
# import plotly.express as px
st.set_page_config(page_title='fitness',layout="wide")

def page0():
    st.title(":orange[My fitness Center]")
    # st.image("GM.jpg",width=950,channels="BGR")
    left, middle, right,a,b,c,d,e= st.columns(8)
    if d.button("sign up"):
        st.session_state.page="page3"
    if e.button("login"):
        st.session_state.page="page1"   
    st.image("GM.jpg",use_container_width=True,channels="BGR")    


def page1():
    st.title("My account")
    email=st.text_input('Enter the Email Address')
    password=st.text_input('password',type='password')
    if st.button("login"):
        st.session_state.page = "page2"
    if st.button("cancel"):
        st.session_state.page = "page0"

def page3():
    st.title("create account")
    email=st.text_input('Enter the Email Address')
    password=st.text_input('password',type='password')
    username=st.text_input('Enter the unique username')

    if st.button('Create My Account'):
        # user = auth.create_user(email = email,password=password,uid=username)
        # st.success("Account created successfully!")
        st.markdown('Please Login using your email and password')
        st.balloons()
    if st.button("login"):
        st.session_state.page="page1"    

def page2():
    st.title("welocoom")
    tab1, tab2, tab3, tab4 = st.tabs([" Home   ","   tacker   ","   plan   ","   food   "])
    with tab1:
        st.title("Home")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.title("Tacker")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.title("Plan")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    if st.button("Go to Page 1"):
        st.session_state.page = "page1"


if "page" not in st.session_state:
    st.session_state.page = "page0"

if st.session_state.page == "page0":
    page0()
elif st.session_state.page == "page1":
    page1()    
elif st.session_state.page == "page3":
    page3()    
elif st.session_state.page == "page2":
    page2()  
    


