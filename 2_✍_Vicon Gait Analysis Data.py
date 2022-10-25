from io import StringIO
import streamlit as st

st.title("Vicon gait analysis data")

uploaded_files = st.file_uploader("Upload Gait Data", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

uploaded_files2 = st.file_uploader("Upload Sit-to-stand Data", accept_multiple_files=True)
for uploaded_file in uploaded_files2:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)