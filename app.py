import streamlit as st

def home_tab():
    st.title("OCR Citizenship")
    st.header("Welcome to the OCR Citizenship app!")
    uploaded_front = st.file_uploader("Upload Citizenship Front", type=["jpg", "jpeg", "png"])
    uploaded_back = st.file_uploader("Upload Citizenship Back", type=["jpg", "jpeg", "png"])

    if st.button("Submit"):
        if uploaded_front is not None and uploaded_back is not None:
            # Process the uploaded images here
            st.write("Front and back of citizenship uploaded successfully!")
            st.warning("Please switch to other tabs.")
        else:
            st.error("Please upload both the citizenship front and back.")

def tab2(uploaded_front):
    st.write("This is the second tab.")

def tab3(uploaded_back):
    st.write("This is the third tab.")

def tab4(uploaded_front):
    st.write("This is the fourth tab.")

def tab5(uploaded_back):
    st.write("This is the fourth tab.")

# Main app
def main():
    st.sidebar.title("Navigation")
    tabs = ["Home", "Front OCR", "Back OCR", "Front Google OCR", "Back Google OCR"]
    selected_tab = st.sidebar.radio("Go to", tabs)

    if selected_tab == "Home":
        home_tab()
    elif selected_tab == "Front OCR":
        uploaded_front = st.session_state.get("uploaded_front")
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
    main()
    