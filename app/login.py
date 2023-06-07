import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit.components.v1 as components

from hasher import Hasher
from authenticate import Authenticate


with open('../config.yaml') as file:
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
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

# # Creating a password reset widget
# if authentication_status:
#     try:
#         if authenticator.reset_password(username, 'Reset password'):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)

