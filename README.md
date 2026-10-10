Language Translation Tool

Project Overview

The **Language Translation Tool** is a Python-based web application developed using Streamlit that allows users to translate text from one language to another.

The application uses the MyMemory Translation API to process translation requests. Users can select their source and target languages, enter the text they want to translate, and view the translated output through a simple and interactive user interface.

This project was developed as **Task 1 of my Artificial Intelligence Internship at CodeAlpha**.

 Features

-  **Multiple Languages:** Supports language selection for English, Hindi, Spanish, French, German, Chinese, Japanese, Korean, Italian, and Turkish.
-  **Text Input:** Allows users to enter text using a text area.
-  **Text Translation:** Translates text between selected source and target languages.
-  **Interactive Interface:** Provides a simple and user-friendly interface using Streamlit.
-  **Input Validation:** Displays warnings if the input text is empty or the source and target languages are the same.
-  **Copy Support:** Provides guidance for copying the translated text.
-  **Centered Layout:** Uses Streamlit's centered layout for a clean interface.

##  Technologies Used

- **Python** – Programming language used to develop the application.
- **Streamlit** – Used to create the interactive web interface.
- **Requests** – Used to send HTTP requests to the translation API.
- **MyMemory Translation API** – Used to retrieve translated text.

##  Supported Languages

The application provides the following language options:

| Language | Language Code |
|---|---|
| English | en |
| Hindi | hi |
| Spanish | es |
| French | fr |
| German | de |
| Chinese | zh |
| Japanese | ja |
| Korean | ko |
| Italian | it |
| Turkish | tr |

**Note:** Translation availability and quality depend on the translation API.

##  Installation and Setup

Follow these steps to run the project on your local computer.

### Step 1: Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

Verify the installation by running:

```bash
python --version
```

### Step 2: Clone the Repository

Clone this repository to your local computer:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

Navigate to the project directory:

```bash
cd language-translation-tool
```

### Step 3: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Required Libraries

Install the required Python packages:

```bash
pip install streamlit requests
```

### Step 5: Run the Application

Run the following command in your terminal:

```bash
streamlit run app.py
```

Replace `app.py` with your Python filename if it is different.

The application will open in your default web browser.

##  How to Use

1. Open the Language Translation Tool.
2. Select the source language from the first dropdown menu.
3. Select the target language from the second dropdown menu.
4. Enter the text you want to translate.
5. Click the **Translate** button.
6. View the translated text displayed on the screen.
7. Copy the translated text manually when needed.

##  API Used

This project uses the MyMemory Translation API.

API endpoint:

https://api.mymemory.translated.net/get

The application sends the input text and selected language pair to the API and displays the translated result.

##  Learning Outcomes

Through this project, I gained practical experience in:

- Developing interactive web applications using Streamlit.
- Working with Python libraries and external APIs.
- Sending HTTP GET requests using the Requests library.
- Processing JSON responses received from an API.
- Implementing input validation and conditional statements.
- Building a simple language translation application.

##  Future Improvements

Possible future enhancements include:

- Adding more supported languages.
- Implementing a functional copy-to-clipboard button.
- Adding text-to-speech functionality.
- Improving error handling for API failures.
- Adding a translation history feature.
- Improving the interface with additional customization.
- Deploying the application online for public access.

##  Internship Information

**Internship Organization:** CodeAlpha  
**Role:** Artificial Intelligence Intern  
**Project:** Language Translation Tool  
**Task:** Task 1  
**Duration:** October 2026

This project was developed as part of my internship learning experience to strengthen my Python programming skills and gain practical experience in application development.

##  Author

**Vishakha Shukla**

GitHub: Add your GitHub profile URL here.

LinkedIn: Add your LinkedIn profile URL here.

---
If you find this project useful, feel free to explore the repository and share your feedback!

#CodeAlpha #Python #Streamlit #LanguageTranslation #ArtificialIntelligence
