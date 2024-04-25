import streamlit as st
import pandas as pd

# Title for the Streamlit app
st.title('Welcome to the Simple Streamlit App')

# Create a form for user input
with st.form("user_info_form"):
    # User input for name inside the form
    name = st.text_input('Please enter your name:', '')

    # User input for age inside the form
    age = st.number_input('Please enter your age:', min_value=0, max_value=150, step=1)

    # Submit button for the form
    submitted = st.form_submit_button("Submit")

# Display the inputs if the form is submitted
if submitted:
    st.write(f'Hello, {name}! You are {age} years old.')

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

edited_df = st.data_editor(df) # 👈 An editable dataframe

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]