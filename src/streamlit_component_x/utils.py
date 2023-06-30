import streamlit as st
from transformers import AutoTokenizer, T5ForConditionalGeneration

@st.cache_resource
def load_model():
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    return model

def inference(msg, _model):
    tokenizer = AutoTokenizer.from_pretrained("t5-small")
    task = "Complete the sentence: " + msg
    enc_input = tokenizer(task, return_tensors='pt')
    outputs = _model.generate(input_ids=enc_input["input_ids"])
    completed = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return completed

