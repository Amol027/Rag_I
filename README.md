# Rag_I
## 🧠 Hobglobin RAG System (FastAPI + Gemini)
1.This project is a simple Retrieval-Augmented Generation (RAG) system.  
2.It extracts "fine prints" (important clauses) from a PDF document and then uses Google's Gemini API to answer user questions based on that extracted content.

### 🚀 Features 
📄 Extracts key information from PDFs in the data/ folder.

💬 Accepts user questions from sample_questions.txt.

🧠 Uses Google Gemini (gemini-2.0-flash) for generating answers.

🔁 Saves extracted fine prints and chat responses to .txt files.

### 📁 Project Structure
```
.
├── app/
│ ├── gemini.py            # Functions to call Gemini API
│ └── utils.py             # PDF text extraction logic
├── data/
│ └── your_files.pdf       # Place IFB/IFPQ PDFs here
├── main.py                # FastAPI app 
├── sample_questions.txt   # List of questions 
├── fine_prints.txt        # Generated summary from PDF
├── chat_response.txt      # Q&A responses saved here
├── requirements.txt
└── README.md
```
### ⚙️ Setup Instructions

✅ Clone the repository

``` git clone https://github.com/Amol027/Rag_I.git ```

📦 Install dependencies 

```pip install -r requirements.txt``` (git bash)

🔑 Set up Gemini API Create a .env file or set your environment variable manually:

export GEMINI_API_KEY="your_api_key_here"

Or include it directly in gemini.py as: genai.configure(api_key="your_api_key_here")

### ▶️ Running the App

open the terminal and copy and paste the following command:
``` uvicorn main:app --reload ```

This will start the app at: http://127.0.0.1:8000

📌 Endpoints 

✅ 1. Visit /fine-prints This extracts and summarizes fine print details from the PDFs.
 🔗 Open:

http://127.0.0.1:8000/fine-prints This will:

Read and extract text from PDF(s) in the data/ folder

Use Gemini to summarize them

Save the result to fine_prints.txt

Return the summary in the browser

✅ 2. Visit /docs (Swagger UI) to test /chat 
🔗 Open:

http://127.0.0.1:8000/docs Then:

Find the /chat endpoint (method: POST)

Click "Try it out"

Click "Execute"

It will:

Read the questions from sample_questions.txt

Use Gemini + the fine prints to answer them

Return the results

Save the answers to chat_response.txt

### 📝 File Format Guide sample_questions.txt 

Example format:

What is the deadline for bid submission?

Who is the contact person for the IFPQ? 

What licenses are required to submit a bid for the IFB? 

### ✅ Output Files
 
  fine_prints.txt: Gemini-generated key points from the PDF.

chat_response.txt: Q&A result for all sample questions.

### 🙌 Acknowledgements 

Google Gemini API

FastAPI

PyMuPDF

