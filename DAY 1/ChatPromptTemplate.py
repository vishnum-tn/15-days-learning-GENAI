from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Your name is {name}."),
        ("human", "Hello, how are you doing today?"),
        ("ai", "I'm doing well, thank you!"),
        ("human", "{user_input}"),
    ]
)

# Example of how to format the prompt
formatted_prompt = chat_template.format_messages(name="Cline", user_input="What is your favorite programming language?")

for message in formatted_prompt:
    print(f"{message.type}: {message.content}")

formatted_prompt = chat_template.format_messages(name="Cline", user_input="Can you tell me a joke?")

for message in formatted_prompt:
    print(f"{message.type}: {message.content}")