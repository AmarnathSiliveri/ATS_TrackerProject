import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()
from streamlit_option_menu import option_menu

genai.configure(api_key=st.secrets['API_KEY'])
#streamlit app
st.set_page_config(page_title="RESume ATS", page_icon='💼')  # page title
# Define CSS styling
page_bg = """
<style>
[data-testid='stAppViewContainer'] {
    background-image: url("https://images.unsplash.com/photo-1617396900799-f4ec2b43c7ae?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
</style>
"""

# Apply the styling using st.markdown
st.markdown(page_bg, unsafe_allow_html=True)




selected = option_menu(
    menu_title=None,
    options=["INTRO","ATS_SCORE","CREDITS"],
    icons=['house',"list-task" ,'person'],
    default_index=0,
    menu_icon='user',
    orientation="horizontal",
    styles="""
    <style>
        .option-menu {
            width: 200px; /* Set the desired width */
            margin-right: 20px; /* Set the desired spacing */
        }
    </style>
"""
)

if selected =="INTRO":
    st.markdown("""# <span style='color:#FFFFFF'>Welcome to My Streamlit App *RESume ATS 💼*</span>""", unsafe_allow_html=True)

    st.markdown("""### <span style='color:#020C0C'> Based on Gemini-PRO LLM API FROM GOOGLE</span>""", unsafe_allow_html=True)
    
    st.markdown("""## <span style='color:#FFF5EE'>Introduction</span>""", unsafe_allow_html=True)

    st.markdown(""" > ##### <span style='color:#020C0C'>This is (A)pplicant(T)racking(S)ystem tool designed to optimize your recruitment process </span>""", unsafe_allow_html=True)

    st.markdown("""## <span style='color:#FFF5EE'>What is (A)pplicant(T)racking(S)ystem ? </span>""", unsafe_allow_html=True)

    st.markdown("""
    <div style='font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; font-size: 18px;'>
        An ATS is like your hiring assistant 🤵‍♂️, but in digital form! 
                <br>
        📝 It's software designed to manage the entire recruitment process for employers.
                <br>
        🖥️ From collecting and storing resumes to tracking candidate progress, it's your go-to tool for streamlining hiring tasks.
                <br>
        🚀 With features like resume parsing and keyword search, it helps sift through heaps of applications efficiently. 
                <br>
        💼 Plus, it keeps everything organized and accessible, making the hiring journey smoother for everyone involved. 🌟
    </div>
""", unsafe_allow_html=True)
    st.header(" ")
    st.success("Navigate to ATS_SCORE tab FOR insights")


if selected == "ATS_SCORE":
       

        ##gemini  response
        def get_gemini_response(input):
            model=genai.GenerativeModel('gemini-pro')
            response=model.generate_content(input)
            return response.text

        def input_pdf_text(uploaded_file):
            reader=pdf.PdfReader(uploaded_file)
            text=""
            for page in range(len(reader.pages)):
                page=reader.pages[page]
                text+=str(page.extract_text())
            return text

        #Prompt Template

        input_prompt="""
        Hey Act Like a skilled or very experience ATS(Application Tracking System)
        with a deep understanding of tech field,software engineering,data science ,data analyst
        and big data engineer. Your task is to evaluate the resume based on the given job description.
        You must consider the job market is very competitive and you should provide 
        best assistance for improving the resumes. Assign the percentage Matching based 
        on Jd and
        the missing keywords with high accuracy and classify the missing words in levels of impact in decreasing fashion  and also provide some course recommendations for the job description to reach include free and paid classify them based on current market trends
        resume:{text}
        description:{jd}

        I want the response in topic-subtopic formats having the structure
        {{"Job Description Match ✅":"%","MissingKeywords📊:[]","Profile Summary📝":"","Course Recommendations":""}}
        """
        st.title("ATS wizard 🤖")
        st.text("Improve YOU RESUME ATS SCORE")
        st.success("Please paste the job description, including company details, role specifics, and requirements. Your input helps us tailor our services. Thank you! 📋")

        jd=st.text_area("Paste the job description 🎯🔍🌐")
        uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="please upload the pdf")


        if st.button("submit"):
            with st.spinner("Processing..."):
                if uploaded_file is not None:
                    text=input_pdf_text(uploaded_file)
                    response=get_gemini_response(input_prompt)
                    st.write(response)
                    st.balloons()
        st.warning("clear the cache at the top left side by clicking --->  ⋮  ")

if selected == 'CREDITS':
    
    st.balloons()
    st.title("CRAFTED BY :")
    st.subheader("AMARNATH SILIVERI")

# Define your styles
    st.markdown("""
<style>
  .social-icons {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
  }

  .social-icon {
    text-align: center;
  }
</style>
""", unsafe_allow_html=True)

# Create a container for social icons
    st.markdown("""
<div class="social-icons">
  <div class="social-icon">
    <a href="https://www.github.com/SilverStark18" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github.svg" width="32" height="32" alt="GitHub" />
    </a>
    <p>GitHub</p>
  </div>

  <div class="social-icon">
    <a href="http://www.instagram.com/itz..amar." target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram.svg" width="32" height="32" alt="Instagram" />
    </a>
    <p>Instagram</p>
  </div>

  <div class="social-icon">
    <a href="http://www.linkedin.com/in/amarnath-siliveri18" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin.svg" width="32" height="32" alt="LinkedIn" />
    </a>
    <p>LinkedIn</p>
  </div>

  <div class="social-icon">
    <a href="https://medium.com/@amartalks25603" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/medium.svg" width="32" height="32" alt="Medium" />
    </a>
    <p>Medium</p>
  </div>

  <div class="social-icon">
    <a href="https://www.x.com/Amarsiliveri" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/twitter.svg" width="32" height="32" alt="Twitter" />
    </a>
    <p>Twitter</p>
  </div>

  <div class="social-icon">
    <a href="https://www.threads.net/@itz..amar." target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/threads.svg" width="32" height="32" alt="Threads" />
    </a>
    <p>Threads</p>
  </div>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.success(" Stay in the loop and level up your knowledge with every follow! ")
    st.success("Do you see icons , click to follow  on SOCIAL")







       
