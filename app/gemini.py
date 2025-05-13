import google.generativeai as genai
import os

# Set your Gemini API key here
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def get_fine_prints(full_text):
    prompt = f"""
You are a legal assistant. Extract the most important fine prints (rules, deadlines, restrictions) from the following document text:

Document:
{full_text}

Only extract useful legal and bidding information.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def chat_with_context(fine_prints, question):
    prompt = f"""
You are a helpful assistant. Use the following fine prints to answer the user's question:

Fine Prints:
{fine_prints}

Question: {question}
Answer:"""

    response = model.generate_content(prompt)
    return response.text.strip()
