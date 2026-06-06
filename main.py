import os
from dotenv import load_dotenv
from fastapi import FastAPI
from google import genai
from fastapi.middleware.cors import CORSMiddleware
# from openai import OpenAI
# AI=OpenAI()
# response=AI.chat.completions.create(model=genai.GenerativeModel("gemini-2.5-flash"),messages=messages)
load_dotenv()
AI=genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# genai.configure(api_key=api)
# message="Hello, chat gpt can we start a project"
# messages= [{"user":"AI", "content":"message"},{"user":"Human"}]
# model = genai.GenerativeModel("gemini-2.5-flash")
# response = model.generate_content(message)
# print(response.text)
message="You are an advanced stock market analyst AI. " \
"Analyze the given stock in this exact order: " \
"first explain PE ratio and PB ratio and whether the stock is " \
"fundamentally strong or weak, second explain ROE, ROCE " \
"and debt level of the company, third analyze promoter holding, " \
"shareholding pattern and balance sheet strength, fourth explain " \
"stock performance, growth, risks and future potential, " \
"fifth give a long term investment score out of 10, and finally conclude " \
"in one sentence whether investors should consider or not consider the " \
"stock for long term investment. Keep the response concise, professional and " \
"point-wise without long paragraphs."

@app.get("/")
def home():
    return{"message":"Stock Analyzer"}

@app.get("/analyse")
def analyser(stock: str):
    response=AI.models.generate_content(model="gemini-2.5-flash",contents=f"{message} stock name:{stock}")
    return{"Stock":stock,"analysis":response.text}





