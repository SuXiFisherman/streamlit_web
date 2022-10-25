import streamlit as st

st.title("2ed solution")

with st.form(key="form1"):
    name = st.text_input(label="Name: ")
    age = st.slider("Age", min_value=10, max_value=100)
    sex = st.selectbox("Select Sex", ['male', 'female'])
    height = st.text_input(label="Height(cm): ")
    weight = st.text_input(label="Weight(kg): ")
    submit = st.form_submit_button(label="Submit")

st.text(name)
st.text(age)
st.text(sex)
st.text(height)
st.text(weight)