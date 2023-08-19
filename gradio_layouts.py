import gradio as gr

# # Gradio Interface
# def demo_func(file_path: str, text: str) -> str:
#     print(text)
#     print(file_path)
#     return text, file_path


# demo = gr.Interface(
#     fn=demo_func,
#     inputs=[gr.components.Image(
#         label='Input image', type='filepath'), gr.components.Textbox(label='Input')],
#     outputs=[gr.components.Textbox(label='Output'), gr.components.Image(
#         label='Output image', type='filepath')],
#     allow_flagging='never'
# )

def handle_clear() -> tuple:
    return '', None, '', None


def handle_submit(file_path: str, text: str) -> tuple:
    print(file_path)
    print(text)
    return file_path, text


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            input_image = gr.components.Image(
                label='Input image', type='filepath')
            input_text = gr.components.Textbox(label='Input text')
            with gr.Row():
                submit = gr.components.Button(
                    value='Submit', variant='primary')
                clear = gr.components.Button(value='Clear', variant='stop')
        with gr.Column():
            output_text = gr.components.Textbox(label='Output text')
            output_image = gr.components.Image(
                label='Output image', type='filepath', height=512, width=512)

    clear.click(handle_clear, [], [input_text,
                input_image, output_text, output_image])
    submit.click(handle_submit, [input_image, input_text], [
                 output_image, output_text])
