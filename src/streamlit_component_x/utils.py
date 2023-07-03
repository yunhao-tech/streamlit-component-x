import streamlit as st
from transformers import AutoTokenizer, T5ForConditionalGeneration, GenerationConfig

@st.cache_resource
def load_model():
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    return model

def inference(cur_msg, _model):
    tokenizer = AutoTokenizer.from_pretrained("t5-base")
    task = "Complete the sentence: " + cur_msg
    generation_config = GenerationConfig.from_pretrained("t5-base")
    enc_input = tokenizer(task, return_tensors='pt')
    outputs = _model.generate(input_ids=enc_input["input_ids"], generation_config=generation_config)
    completed = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return completed

