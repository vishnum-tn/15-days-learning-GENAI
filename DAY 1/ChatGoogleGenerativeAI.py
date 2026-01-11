import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
google_api_key = os.getenv("GOOGLE_API_KEY")

# Ensure the API key is available
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in a .env file or directly.")

# Initialize the ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

# Create a chat prompt template
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a  assistant."),
        ("human", "{user_input}"),
    ]
)

# Chain the prompt and the model
chain = chat_template | llm

# Invoke the chain with a user input
response = chain.invoke({"user_input": "Tell me a funny story about a programmer."})

print(response.content)

response = chain.invoke({"user_input": "What is the capital of France?"})

print(response.content)
