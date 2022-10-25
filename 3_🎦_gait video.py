import streamlit as st
from io import StringIO

st.title("Gait Video")

uploaded_files3 = st.file_uploader("Upload Frontal View Video", accept_multiple_files=True)
for uploaded_file in uploaded_files3:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

uploaded_files4 = st.file_uploader("Upload Lateral View Video", accept_multiple_files=True)
for uploaded_file in uploaded_files4:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)