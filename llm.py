from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from retriever import carregar_chunks
import torch

# Modelo
model_name = "declare-lab/flan-alpaca-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
device = torch.device("cpu")
model.to(device)

def gerar_resposta(pergunta, contexto):
    prompt = f"Responda com base no contexto abaixo:\n\n{contexto}\n\nPergunta: {pergunta}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    output = model.generate(
        input_ids=inputs["input_ids"].to("cpu"),
        attention_mask=inputs["attention_mask"].to("cpu"),
        max_new_tokens=300,
        temperature=0,
    )
    resposta = tokenizer.decode(output[0], skip_special_tokens=True)
    return resposta
