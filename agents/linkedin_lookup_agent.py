import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool

def lookup(name: str) -> str:
  return "https://www.linkedin.com/in/eden-marco/"