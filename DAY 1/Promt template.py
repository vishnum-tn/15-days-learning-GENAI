from langchain_core.prompts import PromptTemplate

# Define a PromptTemplate
prompt = PromptTemplate.from_template(
    "Tell me a {adjective} story about a {noun}."
)

# Format the prompt with dynamic input
formatted_prompt = prompt.format(adjective="funny", noun="rabbit")

print(formatted_prompt)

# Another example with multiple inputs
prompt2 = PromptTemplate(
    input_variables=["tool", "language"],
    template="What is the best way to learn {language} using {tool}?"
)

formatted_prompt2 = prompt2.format(language="Python", tool="Langchain")
print(formatted_prompt2)