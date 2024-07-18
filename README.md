# RESume ATS 💼

## Introduction

Welcome to the **RESume ATS** app, a powerful tool designed to optimize your recruitment process using the **Gemini-PRO LLM API** from Google. This Streamlit app serves as an Applicant Tracking System (ATS) to evaluate resumes against job descriptions, provide feedback on missing keywords, and suggest course recommendations for improvement.

## Features

- **Interactive Interface**: Simple and user-friendly interface with three main sections - **INTRO**, **ATS_SCORE**, and **CREDITS**.
- **Job Description Analysis**: Allows users to paste job descriptions for a detailed analysis.
- **Resume Evaluation**: Users can upload their resume in PDF format for evaluation.
- **Keyword Matching**: Provides percentage match based on job description and identifies missing keywords.
- **Course Recommendations**: Suggests courses (both free and paid) to improve the resume based on current market trends.
- **Visual Appeal**: Customizable background and theme for a visually appealing experience.


## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SilverStark18/Resume-ATS.git
    cd Resume-ATS
    ```


2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file**:
    - Add your Google Gemini-PRO API key in the `.env` file:
      ```
      API_KEY=your_api_key_here
      get one for yourself from google maker studio
      ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

### Sections

- **INTRO**: Provides an introduction to the application and the concept of Applicant Tracking Systems.
- **ATS_SCORE**: The main section where users can input the job description and upload their resume for evaluation. The system provides feedback on the percentage match, missing keywords, and course recommendations.
- **CREDITS**: Information about the developer and social media links for connection.

### Job Description and Resume Evaluation

1. Navigate to the **ATS_SCORE** tab.
2. Paste the job description in the provided text area.
3. Upload your resume in PDF format.
4. Click the **Submit** button to receive the evaluation.

### Social Media Links

In the **CREDITS** section, you can find links to connect with the developer on various social media platforms, including **GitHub**, **Instagram**, **LinkedIn**, **Medium**, **Twitter**, and **Threads**.

Credits
Developed by Amarnath Siliveri. Connect with me on:

<p align="center">
  <a href="https://www.github.com/SilverStark18" target="_blank" rel="noreferrer">
    <img src="https://cdn-icons-png.flaticon.com/128/270/270798.png" width="32" height="32" alt="GitHub" />
  </a>
  &nbsp;
  <a href="http://www.instagram.com/itz..amar." target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram.svg" width="32" height="32" alt="Instagram" />
  </a>
  &nbsp;
  <a href="http://www.linkedin.com/in/amarnath-siliveri18" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin.svg" width="32" height="32" alt="LinkedIn" />
  </a>
  &nbsp;
  <a href="https://medium.com/@amartalks25603" target="_blank" rel="noreferrer">
    <img src="https://cdn-icons-png.flaticon.com/128/5968/5968933.png" width="32" height="32" alt="Medium" />
  </a>
  &nbsp;
  <a href="https://www.x.com/Amarsiliveri" target="_blank" rel="noreferrer">
    <img src="https://cdn-icons-png.flaticon.com/128/5969/5969020.png" width="32" height="32" alt="Twitter" />
  </a>
  &nbsp;
  <a href="https://www.threads.net/@itz..amar." target="_blank" rel="noreferrer">
    <img src="https://cdn-icons-png.flaticon.com/128/12105/12105338.png" width="32" height="32" alt="Threads" />
  </a>
</p>
