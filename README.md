# Rag_I
🧠 Hobglobin RAG System (FastAPI + Gemini)
This project is a simple Retrieval-Augmented Generation (RAG) system. It extracts "fine prints" (important clauses) from a PDF document and then uses Google's Gemini API to answer user questions based on that extracted content.
____________________________________________________________________________________________
🚀 Features
📄 Extracts key information from PDFs in the data/ folder.

💬 Accepts user questions from sample_questions.txt.

🧠 Uses Google Gemini (gemini-2.0-flash) for generating answers.

🔁 Saves extracted fine prints and chat responses to .txt files.
___________________________________________________________________________________________
## 📁 Project Structure
.
├── app/
│ ├── gemini.py # Functions to call Gemini API
│ └── utils.py # PDF text extraction logic
├── data/
│ └── your_files.pdf # Place IFB/IFPQ PDFs here
├── main.py # FastAPI app with /fine-prints and /chat routes
├── sample_questions.txt # List of questions (one per line)
├── fine_prints.txt # Generated summary from PDF
├── chat_response.txt # Q&A responses saved here
├── requirements.txt
└── README.md
____________________________________________________________________________________________
⚙️ Setup Instructions
1. ✅ Clone the repository

git clone https://github.com/Amol027/Rag_I.git

cd hobglobin-rag
2. 📦 Install dependencies
pip install -r requirements.txt (git bash)
3. 🔑 Set up Gemini API
Create a .env file or set your environment variable manually:

export GEMINI_API_KEY="your_api_key_here"

Or include it directly in gemini.py as:
genai.configure(api_key="your_api_key_here")
_______________________________________________________________________________________________
▶️ Running the App
### open the terminal and copy and paste the following command:
uvicorn main:app --reload

## This will start the app at: http://127.0.0.1:8000

📌 Endpoints
✅ 1. Visit /fine-prints
This extracts and summarizes fine print details from the PDFs.
🔗 Open:

http://127.0.0.1:8000/fine-prints
This will:

Read and extract text from PDF(s) in the data/ folder

Use Gemini to summarize them

Save the result to fine_prints.txt

Return the summary in the browser

✅ 2. Visit /docs (Swagger UI) to test /chat
🔗 Open:

http://127.0.0.1:8000/docs
Then:

Find the /chat endpoint (method: POST)

Click "Try it out"

Enter this body (you must submit some JSON, even if it’s dummy):

{
  "question": "dummy"
}
Even though you're submitting "dummy", the app will actually ignore that and instead read all real questions from sample_questions.txt.
###
Click "Execute"  

It will:

Read the questions from sample_questions.txt

Use Gemini + the fine prints to answer them

Return the results

Save the answers to chat_response.txt
________________________________________________________________________________________


📝 File Format Guide
sample_questions.txt
Example format:

What is the deadline for bid submission?
Who is the contact person for the IFPQ?
What licenses are required to submit a bid for the IFB?
Is small business certification required for the IFPQ?
✅ Output Files
fine_prints.txt: Gemini-generated key points from the PDF.

chat_response.txt: Q&A result for all sample questions.

🙌 Acknowledgements
Google Gemini API

FastAPI

PyMuPDF

