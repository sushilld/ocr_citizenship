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

def tab2():
    st.write("This is the second tab.")

def tab3():
    st.write("This is the third tab.")

def tab4():
    st.write("This is the fourth tab.")

# Main app
def main():
    st.sidebar.title("Navigation")
    tabs = ["Home", "Tab 2", "Tab 3", "Tab 4"]
    selected_tab = st.sidebar.radio("Go to", tabs)

    if selected_tab == "Home":
        home_tab()
    elif selected_tab == "Tab 2":
        uploaded_front = st.session_state.get("uploaded_front")
        uploaded_back = st.session_state.get("uploaded_back")
        if uploaded_front is None or uploaded_back is None:
            st.error("Please upload both the citizenship front and back.")
        else:
            tab2()
    elif selected_tab == "Tab 3":
        uploaded_front = st.session_state.get("uploaded_front")
        uploaded_back = st.session_state.get("uploaded_back")
        if uploaded_front is None or uploaded_back is None:
            st.error("Please upload both the citizenship front and back.")
        else:
            tab3()
    elif selected_tab == "Tab 4":
        uploaded_front = st.session_state.get("uploaded_front")
        uploaded_back = st.session_state.get("uploaded_back")
        if uploaded_front is None or uploaded_back is None:
            st.error("Please upload both the citizenship front and back.")
        else:
            tab4()

if __name__ == "__main__":
    main()