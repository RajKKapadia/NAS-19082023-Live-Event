import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
model.to(DEVICE)

def predict(query: str) -> dict:
    inputs = tokenizer(query, return_tensors='pt')
    inputs.to(DEVICE)
    outputs = model(**inputs)
    outputs = torch.sigmoid(outputs.logits)
    outputs = outputs.detach().cpu().numpy()
    label2ids = model.config.label2id
    for i, k in enumerate(label2ids.keys()):
        label2ids[k] = outputs[0][i]
    label2ids = {k: float(v) for k, v in sorted(label2ids.items(), key=lambda item: item[1], reverse=True)}
    return label2ids

demo = gr.Interface(
    fn=predict,
    inputs=gr.components.Textbox(label='Input query'),
    outputs=gr.components.Label(label='Predictions', num_top_classes=5),
    allow_flagging='never'
)