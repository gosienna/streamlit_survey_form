import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("Google Sheets as a DataBase")

# Function to create a sample Orders dataframe
def create_dataframe():
    return pd.DataFrame({
        'Date': ["3/1", "3/2", "3/3", "3/4", "3/5"],
        'Water intake': [2000, 1750, 1500, 1000, 2000],
        'Bath': ['yes', 'no', 'yes', 'no', 'yes'],
        'Urine':  [2200, 1000, 1500, 800, 2000],
    })

# Create the Orders dataframe
df = create_dataframe()

# Display the current DataFrame with an editor)
placeholder = st.empty()
placeholder.data_editor(df)
if st.button("Update I/O"):
    placeholder.empty()
    updated_df = df.copy()
    updated_df['I/O'] = updated_df['Water intake'] - updated_df['Urine']
    placeholder.data_editor(updated_df)

st.divider() #---------------------------------------------------------

st.write("CRUD Operations:")
# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Taking actions based on user input
if st.button("New Worksheet"):
    conn.create(worksheet="Kewei", data=df)
    st.success("Worksheet Created 🎉")

if st.button("Update Worksheet"):
    conn.update(worksheet="Kewei", data=updated_df)
    st.success("Worksheet Updated 🤓")

if st.button("Clear Worksheet"):
    conn.clear(worksheet="Kewei")
    st.success("Worksheet Cleared 🧹")