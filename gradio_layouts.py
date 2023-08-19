# Gradio Interface
import gradio as gr


def demo_func(file_path: str, text: str) -> str:
    print(text)
    print(file_path)
    return text, file_path


demo = gr.Interface(
    fn=demo_func,
    inputs=[gr.components.Image(
        label='Input image', type='filepath'), gr.components.Textbox(label='Input')],
    outputs=[gr.components.Textbox(label='Output'), gr.components.Image(
        label='Output image', type='filepath')],
    allow_flagging='never'
)

if __name__ == '__main__':
    demo.launch()
