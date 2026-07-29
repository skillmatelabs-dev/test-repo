"""Test file with OpenAI API usage that has breaking changes."""
import openai

openai.api_key = "sk-123"

# Old OpenAI API - Completion.create (v0 style)
def get_completion_old(prompt):
    response = openai.client.completions.create(  # BREAKING: Completion.create deprecated, use chat.completions.create
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text

# Old OpenAI API - ChatCompletion.create (v0 style)
def get_chat_old(messages):
    response = openai.client.chat.completions.create(  # BREAKING: ChatCompletion.create deprecated
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

# Old OpenAI API - Embedding.create
def get_embedding_old(text):
    response = openai.client.embeddings.create(  # BREAKING: Embedding.create deprecated
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding