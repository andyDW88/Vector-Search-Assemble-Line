# Vector-Search-Assemble-Line (UNDER DEVELOPMENT)
PDF Vector Search App

This is a simple **Generative AI Chatbot** that allows users to:
- Upload a PDF file.
- Ask questions about the content of the PDF.
- Get relevant responses using vector embeddings for semantic search.

## Project Structure

```plaintext
/project_directory
│
├── userInterface.py      # Gradio interface
├── dataProcessor.py      # File for PDF processing logic
├── vectorSearch.py       # File for handling vector search and embeddings
├── responseGenerator.py  # File for generating responses based on search results
├── init.py               # File for initializing embeddings and MongoDB connection
├── requirements.txt      # Dependencies for the project (Gradio, LangChain, pymongo, etc.)
└── README.md             # Information about the project (this file)
