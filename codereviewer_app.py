import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyBhTcKEi5DmBT4SQoBR9-hpW7f7VcL5yqg")

# Define the system prompt
system_prompt = """You are a professional code reviewer with expertise in multiple programming languages. Your task is to analyze the submitted code for potential bugs, errors, improvements, and readability issues. Perform the following steps:
1. **Identify Bugs and Errors**:
   - Carefully analyze the code for logical errors, syntax issues, and runtime problems.
2. Fixed Code Snippets
"""
# Initialize the Gemini model with the system instruction
gemini = genai.GenerativeModel(
    model_name="models/gemini-2.0-pro-exp-02-05",
    system_instruction=system_prompt
)

# Streamlit app title
st.title("🤖Code Reviewer App")
st.write("Paste your code below and get feedback on bugs, errors, and improvements!")


# Text area for user input
user_code = st.text_area("Enter your code here:", height=200)

# File uploader for .py files
uploaded_file = st.file_uploader("Drag and drop a `.py` file here", type=["py"])

# Button to generate feedback
if st.button("Review Code"):
    if uploaded_file is not None:
        user_code = uploaded_file.read().decode("utf-8")   # Read the uploaded file
        response = gemini.generate_content(user_code)
        st.subheader("Code Review Feedback:")
        st.write(response.text)
    elif user_code.strip() == "":
        st.warning("Please enter some code or upload a file to review.")
    else:
        with st.spinner("Analyzing code..."):              # Generate the response
            response = gemini.generate_content(user_code)
        
        # Display the response
            st.subheader("Code Review Feedback:")
            st.write(response.text)