import json
import pandas as pd
import streamlit as st
from request_ocr import requestURL

import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit.components.v1 as components

from hasher import Hasher
from authenticate import Authenticate

_RELEASE = False


def login():
    if not _RELEASE:
        with open('config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)

        # Creating the authenticator object
        authenticator = Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['preauthorized']
        )

        # creating a login widget
        name, authentication_status, username = authenticator.login(
            'Login', 'main')

        if authentication_status:
            authenticator.logout('Logout', 'main')
            st.write(f'Welcome *{name}*')
            return True
        elif authentication_status is False:
            st.error('Username/password is incorrect')
        elif authentication_status is None:
            st.warning('Please enter your username and password')


def home_tab():
    st.title("OCR Citizenship")
    st.header("Welcome to the OCR Citizenship app!")
    uploaded_front = st.file_uploader(
        "Upload Citizenship Front", type=["jpg", "jpeg", "png"])
    uploaded_back = st.file_uploader(
        "Upload Citizenship Back", type=["jpg", "jpeg", "png"])
    if st.button("Submit"):
        if uploaded_front is not None and uploaded_back is not None:
            # Process the uploaded images here
            st.session_state['uploaded_front'] = uploaded_front
            st.session_state['uploaded_back'] = uploaded_back
            st.write("Front and back of citizenship uploaded successfully!")
            st.image(uploaded_front)
            st.image(uploaded_back)
            try:
                del st.session_state['front_ocr']
                del st.session_state['back_ocr']
            except:
                pass
            st.warning("Please switch to other tabs.")
        else:
            st.error("Please upload both the citizenship front and back.")


def tab2(uploaded_front):
    st.header("Uploaded Front OCR")
    col1, col2 = st.columns(2, gap="large")
    if 'front_ocr' in st.session_state and st.session_state['front_ocr']['CardValidation'] is False:
        st.error("Citizenship Front is not valid. Try again")
        st.image('./imgngif/fake-ids-v7tzde.jpg', width=800)
        return
    if 'front_ocr' not in st.session_state:
        with st.spinner('Wait for it...'):
            response_text = requestURL(
                f"http://{ip_address}:{ip_port}/uploadDocument/front/", st.session_state['uploaded_front'])
            if 'status' in response_text:
                st.error(response_text['message'], icon='🚨')
                st.image('./imgngif/not-sure-if-50a6308be8.jpg', width=800)
                return
            st.session_state['front_ocr'] = response_text
        if response_text['CardValidation'] is False:
            st.error("Citizenship Front is not valid. Try again")
            st.image("./imgngif/fake-ids-v7tzde.jpg")
            return
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
            if 'District' not in birthplace:
                birthplace['District'] = ''
            if 'WardNumber' not in birthplace:
                birthplace['WardNumber'] = ''
            if 'District' not in permanent_address:
                permanent_address['District'] = ''
            if 'WardNumber' not in permanent_address:
                permanent_address['WardNumber'] = ''
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
                "PermanentAddress_WardNumber": [permanent_address['WardNumber']],
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
    # if st.session_state['back_ocr'] == None:
    if 'back_ocr' not in st.session_state:
        with st.spinner('Wait for it...'):
            response_text = requestURL(
                f"http://{ip_address}:{ip_port}/uploadDocument/back/", st.session_state['uploaded_back'])
            if 'status' in response_text:
                st.error(response_text['message'])
                st.image('./imgngif/not-sure-if-50a6308be8.jpg', width=800)
                return
            st.session_state['back_ocr'] = response_text
        if response_text['CardValidation'] is False:
            st.error("Citizenship Back is not valid. Try again")
            st.image('./imgngif/not-sure-if-50a6308be8.jpg', width=800)
            return
    else:
        response_text = st.session_state['back_ocr']
    # Add the image to the first column
    citizenship_number = response_text['Info']['CitizenshipNumber']
    name = response_text['Info']['FullName']
    gender = response_text['Info']['Gender']
    birthdate = response_text['Info']['BirthDate']
    birthplace = response_text['Info']['BirthPlace']
    permanent_address = response_text['Info']['PermanentAddress']
    issue_d = response_text['Info']['IssueDate']
    finger_print = str(response_text['FingerPrintStatus'])
    with col1:
        st.subheader("Citizenship Back View")
        st.image(uploaded_back, use_column_width=True)

    # Add the description to the second column
    with col2:
        st.subheader("Citizenship OCR finding with :blue[fields]")

        with st.container():
            if 'District' not in birthplace:
                birthplace['District'] = ''
            if 'WardNumber' not in birthplace:
                birthplace['WardNumber'] = ''
            if 'District' not in permanent_address:
                permanent_address['District'] = ''
            if 'WardNumber' not in permanent_address:
                permanent_address['WardNumber'] = ''
            data = {
                "CitizenshipNumber": [citizenship_number],
                "FullName": [name],
                "Gender": [gender],
                "BirthDate": [birthdate],
                "BirthPlace_District": [birthplace['District']],
                "BirthPlace_WardNumber": [birthplace['WardNumber']],
                "PermanentAddress_District": [permanent_address['District']],
                "PermanentAddress_WardNumber": [permanent_address['WardNumber']],
                "IssueDate": [issue_d],
                "FingerPrint": [finger_print]
            }

            df = pd.DataFrame(data)
            df = df.reset_index(drop=True)
            df.index = ["Values"]
            st.table(df.transpose())

    st.write("---")

    st.subheader("Extraced text from image")
    st.caption('The Full text extracted using OCR :red[without fields]')

    with st.container():
        st.write(response_text['Info']['ExtractedText'])


def tab4(uploaded_front):
    st.header("Uploaded Front OCR")
    col1, col2 = st.columns(2, gap="large")
    # if st.session_state['google_front_ocr'] == None:
    if 'front_ocr' in st.session_state and st.session_state['front_ocr']['CardValidation'] is False:
        st.error("Citizenship Front is not valid. Try again")
        st.image('./imgngif/fake-ids-v7tzde.jpg', width=800)
        return
    if 'google_front_ocr' not in st.session_state:
        with st.spinner('Wait for it...'):
            response_text = requestURL(
                f"http://{ip_address}:{ip_port}/uploadDocument-Google/front/", st.session_state['uploaded_front'])
            if 'status' in response_text:
                st.error(response_text['message'])
                st.image('./imgngif/not-sure-if-50a6308be8.jpg', width=800)
                return
            st.session_state['google_front_ocr'] = response_text
        if response_text['CardValidation'] is False:
            st.error("Citizenship Front is not valid. Try again")
            st.image('./imgngif/fake-ids-v7tzde.jpg', width=800)
            return
    else:
        response_text = st.session_state['google_front_ocr']
    citizenship_number = response_text['Info']['CitizenshipNumber']
    name = response_text['Info']['FullName']
    gender = response_text['Info']['Gender']
    birthdate = response_text['Info']['BirthDate']
    father_name = response_text['Info']['FatherName']
    mother_name = response_text['Info']['MotherName']
    birthplace = response_text['Info']['BirthPlace']
    permanent_address = response_text['Info']['PermanentAddress']
    # Add the image to the first column
    with col1:
        st.subheader("Citizenship Front View")
        st.image(uploaded_front, use_column_width=True)

    # Add the description to the second column
    with col2:
        st.subheader("Citizenship OCR finding with :blue[fields]")

        with st.container():
            if 'District' not in birthplace:
                birthplace['District'] = ''
            if 'WardNumber' not in birthplace:
                birthplace['WardNumber'] = ''
            if 'District' not in permanent_address:
                permanent_address['District'] = ''
            if 'WardNumber' not in permanent_address:
                permanent_address['WardNumber'] = ''
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
                "PermanentAddress_WardNumber": [permanent_address['WardNumber']],
            }

            df = pd.DataFrame(data)
            df = df.reset_index(drop=True)
            df.index = ["Values"]
            st.table(df.transpose())

    st.write("---")

    st.subheader("Extraced text from image")
    st.caption('The Full text extracted using OCR :red[without fields]')

    with st.container():
        st.write(response_text['Info']['ExtractedText'])


def tab5(uploaded_back):
    st.header("Uploaded back OCR")
    col1, col2 = st.columns(2, gap="large")
    # if st.session_state['google_back_ocr'] == None:
    if 'google_back_ocr' not in st.session_state:
        with st.spinner('Wait for it...'):
            response_text = requestURL(
                f"http://{ip_address}:{ip_port}/uploadDocument-Google/back/", st.session_state['uploaded_back'])
            if 'status' in response_text:
                st.error(response_text['message'])
                st.image('./imgngif/not-sure-if-50a6308be8.jpg', width=800)
                return
            st.session_state['google_back_ocr'] = response_text
        if response_text['CardValidation'] is False:
            st.error("Citizenship Front is not valid. Try again")
            st.image('./imgngif/not-sure-if-50a6308be8.jpg', width=800)
            return
    else:
        response_text = st.session_state['google_back_ocr']
    # Add the image to the first column
    citizenship_number = response_text['Info']['CitizenshipNumber']
    name = response_text['Info']['FullName']
    gender = response_text['Info']['Gender']
    birthdate = response_text['Info']['BirthDate']
    birthplace = response_text['Info']['BirthPlace']
    permanent_address = response_text['Info']['PermanentAddress']
    issue_d = response_text['Info']['IssueDate']
    finger_print = response_text['FingerPrintStatus']

    with col1:
        st.subheader("Citizenship Front View")
        st.image(uploaded_back, use_column_width=True)

    # Add the description to the second column
    with col2:
        st.subheader("Citizenship OCR finding with :blue[fields]")

        with st.container():
            data = {
                "CitizenshipNumber": [citizenship_number],
                "FullName": [name],
                "Gender": [gender],
                "BirthDate": [birthdate],
                "BirthPlace_District": [birthplace['District']],
                "BirthPlace_WardNumber": [birthplace['WardNumber']],
                "PermanentAddress_District": [permanent_address['District']],
                "PermanentAddress_WardNumber": [permanent_address['WardNumber']],
                "IssueDate": [issue_d],
                "FingerPrint": [finger_print]
            }

            df = pd.DataFrame(data)
            df = df.reset_index(drop=True)
            df.index = ["Values"]
            st.table(df.transpose())

    st.write("---")

    st.subheader("Extraced text from image")
    st.caption('The Full text extracted using OCR :red[without fields]')

    with st.container():
        st.write(response_text['Info']['ExtractedText'])

# Main app


def main(show_google):
    st.set_page_config(page_title="OCR Citizenship", layout="wide")
    if login():
        st.sidebar.title("Navigation")
        if show_google == 'true':
            tabs = ["Home", "Front OCR", "Back OCR",
                    "Front Google OCR", "Back Google OCR"]
        else:
            tabs = ["Home", "Front OCR", "Back OCR"]
        selected_tab = st.sidebar.radio("Go to", tabs)

        if selected_tab == "Home":
            home_tab()
        elif selected_tab == "Front OCR":
            uploaded_front = st.session_state.get("uploaded_front")
            if uploaded_front is None:
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
    try:
        global ip_address
        global ip_port
        with open('./config.json') as f:
            data = json.load(f)
        ip_address = data['ip_address']
        ip_port = data['ip_port']
        show_google = data['show_google']
        print(ip_address, ip_port)
        main(show_google)
    except Exception as e:
        st.error("Something went wrong. Please try again.")
        try:
            del st.session_state['uploaded_front']
        except:
            pass
        try:
            del st.session_state['uploaded_back']
        except:
            pass
        try:
            del st.session_state['google_front_ocr']
        except:
            pass
        try:
            del st.session_state['google_back_ocr']
        except:
            pass
        try:
            del st.session_state['front_ocr']
        except:
            pass
        try:
            del st.session_state['back_ocr']
        except:
            pass
        print(e)
