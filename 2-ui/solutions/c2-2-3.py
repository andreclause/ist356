import streamlit as st 

st.title("order Processor")

# Initialize variables
total =0.0
count= 0.0

# Input
file = st.file_uploader("Upload Text File:", type=["txt"])

# Process

# Output
st.write(f"Total Amount: ${total}")
st.write(f"Total Orders: {count}")