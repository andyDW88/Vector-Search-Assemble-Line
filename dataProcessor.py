from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Initialize the text splitters for parent and child documents
parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=200)
# Function to process PDF document and split it into chunks
def process_pdf(file):
    loader = PyPDFLoader(file.name)
    docs = loader.load()
    parent_docs = parent_splitter.split_documents(docs)
    
    # Process parent documents
    for parent_doc in parent_docs:
        parent_doc_content = parent_doc.page_content.replace('\n', ' ')
        parent_id = collection.insert_one({
            'document_type': 'parent',
            'content': parent_doc_content
        }).inserted_id
        
        # Process child documents
        child_docs = child_splitter.split_documents([parent_doc])
        for child_doc in child_docs:
            child_doc_content = child_doc.page_content.replace('\n', ' ')
            child_embedding = embeddings.embed_documents([child_doc_content])[0]
            collection.insert_one({
                'document_type': 'child',
                'content': child_doc_content,
                'embedding': child_embedding,
                'parent_ref': parent_id
            })
    return "PDF processing complete"