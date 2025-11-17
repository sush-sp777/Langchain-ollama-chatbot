# Langchain-Ollama-Chatbot

This repository contains a simple chatbot application built using **LangChain**, **Streamlit**, and **Ollama** (local LLMs).  

---

## 🚀 Features

- Uses **Ollama** to run Gemma3:1b (or any local LLM)
- Built with **LangChain LCEL**
- Streamlit UI for user interaction
- Beginner-friendly structure

---

## 📂 Project Structure

```
Langchain-Ollama-Chatbot/
│
├── app.py              # Streamlit app
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

## 🧠 How it Works

1. **ChatPromptTemplate** creates prompt instructions  
2. **Ollama LLM** runs locally and generates responses  
3. **LCEL chain** connects prompt → LLM → output parser  
4. **Streamlit** displays input + output

This is **NOT a RAG pipeline**—it is a basic LLM chatbot using local models.

---

## 🖥️ Running the App Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Streamlit App
```bash
streamlit run app.py
```

### 3. Make sure Ollama is running
Download a model:
```bash
ollama pull gemma3:1b
```

Check installed models:
```bash
ollama list
```


