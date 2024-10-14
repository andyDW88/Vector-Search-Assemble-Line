# Gradio app structure
with gr.Blocks(css=".gradio-container {background-color: AliceBlue}") as demo:
    gr.Markdown("Generative AI Chatbot - Upload your file and Ask questions")

    # Tab for uploading PDFs
    with gr.Tab("Upload PDF"):
        with gr.Row():
            pdf_input = gr.File()  # For uploading PDF
            pdf_output = gr.Textbox()  # To display output after processing
        pdf_button = gr.Button("Upload PDF")

    # Tab for asking questions to the chatbot
    with gr.Tab("Ask question"):
        question_input = gr.Textbox(label="Your Question")  # Input for user questions
        answer_output = gr.Textbox(label="LLM Response and Retrieved Documents", interactive=False)

    # Button click actions
    question_button = gr.Button("Ask")
    question_button.click(query_and_display, inputs=[question_input], outputs=answer_output)
    
    pdf_button.click(process_pdf, inputs=pdf_input, outputs=pdf_output)

# Launch the app
demo.launch()