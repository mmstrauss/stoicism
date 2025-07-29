import streamlit as st
from PyPDF2 import PdfReader
import os

# App title
st.title("📜 Stoicism Learning App")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select Option:", 
                          ["Home", "Read PDF", "Daily Stoic Exercise", "About"])

# Home page
if options == "Home":
    st.header("Welcome to the Stoicism Learning App")
    st.write("""
    This app helps you learn about Stoicism through curated PDF content, 
    daily exercises, and reflections.
    
    **Stoicism** is a philosophy that teaches the development of self-control 
    and fortitude as a means to overcome destructive emotions.
    """)
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Stoic_Triangle.svg/1200px-Stoic_Triangle.svg.png", 
             width=300, caption="The Stoic Virtues")
    
    st.markdown("""
    ### Key Principles of Stoicism:
    - Focus on what you can control
    - Accept what you cannot change
    - Practice virtue above all else
    - View obstacles as opportunities
    - Reflect on your day
    """)

# PDF Reader page
elif options == "Read PDF":
    st.header("Read Stoic Texts")
    
    # Upload PDF file
    uploaded_file = st.file_uploader("Upload a PDF file about Stoicism", type="pdf")
    
    if uploaded_file is not None:
        pdf_reader = PdfReader(uploaded_file)
        
        # Show PDF info
        st.write(f"**Document:** {uploaded_file.name}")
        st.write(f"**Number of pages:** {len(pdf_reader.pages)}")
        
        # Select page to display
        page_num = st.number_input("Select page number:", 
                                  min_value=1, 
                                  max_value=len(pdf_reader.pages),
                                  value=1)
        
        # Display selected page
        selected_page = pdf_reader.pages[page_num-1]
        st.write("### Page Content:")
        st.write(selected_page.extract_text())
        
        # Option to download the PDF
        st.download_button(
            label="Download PDF",
            data=uploaded_file.getvalue(),
            file_name=uploaded_file.name,
            mime="application/pdf"
        )

# Daily Exercise page
elif options == "Daily Stoic Exercise":
    st.header("Daily Stoic Exercise")
    
    st.write("""
    ### Today's Reflection:
    *"We suffer more often in imagination than in reality."* — Seneca
    """)
    
    # Exercise prompt
    with st.expander("Daily Writing Prompt"):
        st.write("""
        **Prompt:** Think about a recent situation where you imagined the worst outcome. 
        How did reality compare to your fears? What can you learn from this?
        """)
        user_response = st.text_area("Write your reflection here:", height=150)
        if st.button("Submit Reflection"):
            if user_response:
                st.success("Thank you for your reflection! Consider saving this in your journal.")
            else:
                st.warning("Please write something before submitting.")

# About page
elif options == "About":
    st.header("About This App")
    st.write("""
    This Stoicism Learning App was created to make philosophical teachings 
    more accessible and practical for daily life.
    
    **Features:**
    - Read Stoic texts from PDFs
    - Daily reflection exercises
    - Practical applications of Stoic philosophy
    
    Built with Python and Streamlit.
    """)
    
    st.markdown("""
    ### How to Use This App:
    1. Upload a PDF about Stoicism in the 'Read PDF' section
    2. Select pages to read
    3. Complete the daily exercise in 'Daily Stoic Exercise'
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("""
**GitHub Repository:**  
[Stoicism Learning App](https://github.com/yourusername/stoicism-app)
""")
