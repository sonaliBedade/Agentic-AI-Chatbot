import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 "+self.config.get_page_title(), layout="wide")
        st.header("🤖 " +self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API_key", type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API key to proceed. Refer https://console.groq.com/keys ")

            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Web" or self.user_controls["selected_usecase"] == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY", type ="password")

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your Tavily API Key to login. Refer: https://app.tavily.com/home")
            
            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("News Explorer Chattr")
                with st.sidebar:
                    time_frame = st.selectbox("Select Time frame", ["Daily", "Weekly", "Monthly"], index=0)
                if st.button("Fetch News", use_container_width=True):
                    st.session_state.timeframe = time_frame

        return self.user_controls
