import os  #access env variables
from dotenv import load_dotenv   
from langchain_community.llms import Ollama  #LLM wrapper for ollama models 
import streamlit as st   #creates web ui
load_dotenv()   #load .env files

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"  #helps to see chain execution logs

from langchain_core.prompts import ChatPromptTemplate  #format prompts
from langchain_core.output_parsers import StrOutputParser #extract plain text output

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ('system',"You are a helpful assistant. Please respond to the question asked"), #defines system role
        ('user',"Question:{Question}")   #user input
    ]
)

#streamlit framework
st.title("Langchain Demo with Gemma3:1b")
st.write("This app uses the Gemma3:1b model through ollama + langchain.")

input_text=st.text_input("what question you have in mind?")  #text box for user question

#ollama Gemma3:1b model 
llm=Ollama(model="Gemma3:1b")   #loading ollama model
output_parser=StrOutputParser() #convert model output into simple string, cleans metadata or formatting

chain=prompt|llm|output_parser  #check user input send prompt to llm and format output this is called LCEL pipeline

if input_text:
    st.write(chain.invoke({"Question":input_text})) 

#chain.invoke- runs the whole pipeline
