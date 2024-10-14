from langchain.llms import OpenAI
# Initialize the OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)
# Function to generate a response from the LLM
def generate_response(query, parent_docs, child_docs):
    response_content = " ".join([doc['content'] for doc in parent_docs if doc])
    chat_completion = openai_client.chat.completions.create(
        messages=[{"role": "user", "content": query}],
        model="gpt-3.5-turbo"
    )
    return chat_completion.choices[0].message.content
