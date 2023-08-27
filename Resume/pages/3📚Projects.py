import streamlit as st

st.set_page_config(page_title="Projects", page_icon="📚")

PROJECTS = {
    "🏆 Unemployeement prediction - Predicting an high unemployeement rate using machine learning algorithm":"https://github.com/UMAMAHESHWARRAO302001/Oasis_Task2",
    "🏆 Sales prediction - Predicting the sales of electronic devices by using past data":"https://github.com/UMAMAHESHWARRAO302001/Oasis_Task4",
    "🏆 Olympic medal prediction - Predicting a olympic medals of a specific country using past data": "https://github.com/UMAMAHESHWARRAO302001/machine_learning_1st-project",
    "🏆 Voice Assistant - Using Python libraries, i had built a voice assistant for limited commands": "https://github.com/UMAMAHESHWARRAO302001/Voice_Assistant_using_Python",
}

# --- Projects & Accomplishments ---
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")