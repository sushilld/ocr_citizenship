import pandas as pd
import streamlit as st
from request_ocr import requestURL

def home_tab():
    st.title("OCR Citizenship")
    st.header("Welcome to the OCR Citizenship app!")
    uploaded_front = st.file_uploader("Upload Citizenship Front", type=["jpg", "jpeg", "png"])
    uploaded_back = st.file_uploader("Upload Citizenship Back", type=["jpg", "jpeg", "png"])
    if st.button("Submit"):
        if uploaded_front is not None and uploaded_back is not None:
            # Process the uploaded images here
            st.session_state['uploaded_front'] = uploaded_front
            st.session_state['uploaded_back'] = uploaded_back            
            st.write("Front and back of citizenship uploaded successfully!")
            st.image(uploaded_front)
            st.image(uploaded_back)
            st.warning("Please switch to other tabs.")
        else:
            st.error("Please upload both the citizenship front and back.")

def tab2(uploaded_front):
    st.header("Uploaded Front OCR")
    col1, col2 = st.columns(2, gap="large")

    # Add the image to the first column
    if st.session_state['front_ocr'] == None:
        with st.spinner('Wait for it...'):
            response_text = requestURL("http://192.168.41.111:6011/uploadDocument/front/", st.session_state['uploaded_front'])
            st.session_state['front_ocr']
        if response_text['CardValidation'] is False:
            st.error("Citizenship Front is not valid. Try again")
    else:
        response_text = st.session_state['front_ocr']
    citizenship_number = response_text['Info']['CitizenshipNumber']
    name = response_text['Info']['FullName']
    gender = response_text['Info']['Gender']
    birthdate = response_text['Info']['BirthDate']
    father_name = response_text['Info']['FatherName']
    mother_name = response_text['Info']['MotherName']
    birthplace = response_text['Info']['BirthPlace']
    permanent_address = response_text['Info']['PermanentAddress']
    with col1:
        st.subheader("Citizenship Front View")
        st.image(uploaded_front, use_column_width=True, width=500)

    # Add the description to the second column
    with col2:
        st.subheader("Citizenship OCR finding with :blue[fields]")
        
        with st.container():
            data = {
                "CitizenshipNumber": [citizenship_number],
                "FullName": [name],
                "Gender": [gender],
                "BirthDate": [birthdate],
                "FatherName": [father_name],
                "MotherName": [mother_name],
                "BirthPlace_District": [birthplace['District']],
                "BirthPlace_WardNumber": [birthplace['WardNumber']],
                "PermanentAddress_District": [permanent_address['District']],
                "PermanentAddress_WardNumber": [permanent_address['WardNumber']]
            }

            df = pd.DataFrame(data)
            df = df.reset_index(drop=True)
            df.index = ["Values"]
            st.table(df.transpose())
        
    st.write("---")
    # Full text extracted from image
    st.subheader("Extraced text from image")
    st.caption('The Full text extracted using OCR :red[without fields]')
    
    with st.container():
        st.write(response_text['Info']['ExtractedText'])

def tab3(uploaded_back):
    st.header("Uploaded Back OCR")
    col1, col2 = st.columns(2, gap="large")
    if st.session_state['back_ocr'] == None:
        with st.spinner('Wait for it...'):
            response_text = requestURL("http://192.168.41.111:6011/uploadDocument/back/")
        if response_text['CardValidation'] is False:
            st.error("Citizenship Front is not valid. Try again")
    else:
        response_text = st.session_state['back_ocr']
    # Add the image to the first column
    with col1:
        st.subheader("Citizenship Front View")
        st.image(uploaded_back, use_column_width=True)

    # Add the description to the second column
    with col2:
        st.subheader("Citizenship OCR finding with :blue[fields]")
        
        with st.container():
            st.write("This is a description of the image.")
        
    st.write("---")
    
    st.subheader("Extraced text from image")
    st.caption('The Full text extracted using OCR :red[without fields]')
    
    with st.container():
        st.write("This is a description of the image.")
    
    

def tab4(uploaded_front):
    st.header("Uploaded Front OCR")
    col1, col2 = st.columns(2, gap="large")
    if st.session_state['google_front_ocr'] == None:
        with st.spinner('Wait for it...'):
            response_text = requestURL("http://192.168.50.177:6011/uploadDocument-Google/front/")
        if response_text['CardValidation'] is False:
            st.error("Citizenship Front is not valid. Try again")
    else:
        response_text = st.session_state['google_front_ocr']
    citizenship_number = response_text['CitizenshipNumber']
    name = response_text['FullName']
    gender = response_text['Gender']
    birthdate = response_text['BirthDate']
    father_name = response_text['FatherName']
    mother_name = response_text['MotherName']
    birthplace = response_text['BirthPlace']
    permanent_address = response_text['PermanentAddress']
    # Add the image to the first column
    with col1:
        st.subheader("Citizenship Front View")
        st.image(uploaded_front, use_column_width=True)

    # Add the description to the second column
    with col2:
        st.subheader("Citizenship OCR finding with :blue[fields]")
        
        with st.container():
            st.write("This is a description of the image.")
        
    st.write("---")
    
    st.subheader("Extraced text from image")
    st.caption('The Full text extracted using OCR :red[without fields]')
    
    with st.container():
        st.write("This is a description of the image.")
        
        
def tab5(uploaded_back):
    st.header("Uploaded back OCR")
    col1, col2 = st.columns(2, gap="large")
    if st.session_state['google_back_ocr'] == None:
        with st.spinner('Wait for it...'):
            response_text = requestURL("http://192.168.50.177:6011/uploadDocument-Google/back/")
        if response_text['CardValidation'] is False:
            st.error("Citizenship Front is not valid. Try again")
    else:
        response_text = st.session_state['google_back_ocr']
    # Add the image to the first column
    with col1:
        st.subheader("Citizenship Front View")
        st.image(uploaded_back, use_column_width=True)

    # Add the description to the second column
    with col2:
        st.subheader("Citizenship OCR finding with :blue[fields]")
        
        with st.container():
            st.write("This is a description of the image.")
        
    st.write("---")
    
    st.subheader("Extraced text from image")
    st.caption('The Full text extracted using OCR :red[without fields]')
    
    with st.container():
        st.write("This is a description of the image.")

# Main app
def main():
    st.set_page_config(page_title="OCR Citizenship", layout="wide")
    st.sidebar.title("Navigation")
    tabs = ["Home", "Front OCR", "Back OCR", "Front Google OCR", "Back Google OCR"]
    selected_tab = st.sidebar.radio("Go to", tabs)
    
    if selected_tab == "Home":
        home_tab()
    elif selected_tab == "Front OCR":
        uploaded_front = st.session_state.get("uploaded_front")
        print(uploaded_front)
        if uploaded_front is None :
            st.error("Please upload both the citizenship front and back.")
        else:
            tab2(uploaded_front)
    elif selected_tab == "Back OCR":
        uploaded_back = st.session_state.get("uploaded_back")
        if uploaded_back is None:
            st.error("Please upload both the citizenship front and back.")
        else:
            tab3(uploaded_back)
    elif selected_tab == "Front Google OCR":
        uploaded_front = st.session_state.get("uploaded_front")
        if uploaded_front is None:
            st.error("Please upload both the citizenship front and back.")
        else:
            tab4(uploaded_front)
    elif selected_tab == "Back Google OCR":
        uploaded_back = st.session_state.get("uploaded_back")
        if uploaded_back is None:
            st.error("Please upload both the citizenship front and back.")
        else:
            tab5(uploaded_back)

if __name__ == "__main__":
    st.session_state['front_ocr'] = None
    st.session_state['back_ocr'] = None
    st.session_state['google_front_ocr'] = None
    st.session_state['google_back_ocr'] = None
    main()
    