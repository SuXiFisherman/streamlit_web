import streamlit as st
from io import StringIO

st.title("Knee Ultrasonography")

#Left Leg
st.text("Left Leg")
CartilageThickness = st.text_input(label="Cartilage tickness: ")
OsteophyteGrade = st.text_input(label="Osteophyte Grade(0-5): ")
VM_Muscle_Volume = st.text_input(label="VM Muscle Volume(cm^2):")
RF_Muscle_Volume = st.text_input(label="RF Muscle Volume(cm^2):")

uploaded_files = st.file_uploader("Upload VM muscle image", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

uploaded_files2 = st.file_uploader("Upload RF muscle image", accept_multiple_files=True)
for uploaded_file in uploaded_files2:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

uploaded_files3 = st.file_uploader("Upload cartilage image", accept_multiple_files=True)
for uploaded_file in uploaded_files3:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

uploaded_files4 = st.file_uploader("Upload Osteophyte (medial TF-joint gap) image", accept_multiple_files=True)
for uploaded_file in uploaded_files4:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)


#Right Leg
st.text("Right Leg")
CartilageThickness2 = st.text_input(label="Cartilage Tickness: ")
OsteophyteGrade2 = st.text_input(label="Osteophyte grade(0-5): ")
VM_Muscle_Volume2 = st.text_input(label="VM Muscle volume(cm^2)2:")
RF_Muscle_Volume2 = st.text_input(label="RF Muscle volume(cm^2)2:")


uploaded_files5 = st.file_uploader("Upload VM muscle Image", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

uploaded_files6 = st.file_uploader("Upload RF muscle Image", accept_multiple_files=True)
for uploaded_file in uploaded_files2:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

uploaded_files7 = st.file_uploader("Upload cartilage Image", accept_multiple_files=True)
for uploaded_file in uploaded_files3:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)

uploaded_files8 = st.file_uploader("Upload Osteophyte (medial TF-joint gap) Image", accept_multiple_files=True)
for uploaded_file in uploaded_files4:
    st.write("filename:", uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)
