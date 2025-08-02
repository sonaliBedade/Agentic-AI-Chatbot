from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self,llm):
        '''
        Initialize the AI News Node with API Keys for Tavily and GROQ
        '''
        self.tavily = TavilyClient()
        self.llm = llm
        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        '''
        Fetch AI news on the specified frequency
        Args:
            state(dict): The state dictionary containing frequency
        Returns
            dict: Updated state with 'news_data' key containing fetched news
        '''