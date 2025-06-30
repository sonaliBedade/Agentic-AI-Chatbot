# 🤖 Agentic AI Chatbot

Welcome to Agentic AI Chatbot! It's lightweight chatbot framework built with LangGraph and Streamlit, designed to explore the basics of agentic workflows and LLM routing graphs. 
Check it out here [Chattr](https://chatttr.streamlit.app/#lang-graph-build-stateful-agentic-ai-graph)!

---

##  What is this project?

This chatbot was built to demonstrate how **graph-based agent execution** can be integrated with modern LLMs to create controlled message routing and basic interaction logic.

You can choose which model to use, and interact with the chatbot through a clean Streamlit interface. Under the hood, the system builds a minimal graph structure to send your input to the selected model and return a response.

---

##  Key Features

-  **Agentic Graph Routing**: Uses LangGraph to organize LLM calls via a simple graph node structure
-  **Model Selection**: Easily switch between Groq and OpenAI models from the sidebar
-  **Streamlit UI**: Simple and responsive interface for real-time chat with your selected model
-  **Clean Starter Template**: Modular structure makes it easy to extend later

---

##  Use Case

This chatbot is currently designed as a **basic conversational bot** using LLMs. It allows users to:

- Select a model 
- Enter a message in the chat interface
- Get a direct LLM-generated response

This serves as a foundation for more advanced agentic or multi-step workflows, but at this stage it is focused on a **single-message, single-response loop** to keep things lightweight and easy to understand.

---

##  Technologies Used

| Area           | Tools/Frameworks                             |
|----------------|----------------------------------------------|
| LLMs           | `langchain_groq`         |
| Agent Graphs   | `langgraph`                                  |
| Core Logic     | `langchain`, `langchain_core`                |
| UI             | `Streamlit`                                  |

---



