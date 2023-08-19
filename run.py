from fastapi import FastAPI
import gradio as gr

# from gradio_layouts import demo
from text_classification_ui import demo

app = FastAPI()

@app.get('/')
def home():
    return 'Gradio UI is running on /gradio', 200

app = gr.mount_gradio_app(app, demo, '/gradio')
