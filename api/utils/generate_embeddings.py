from transformers import pipeline

embedder = pipeline('feature-extraction',model='bert-base-uncased')

def generate_embedding(text):
    embedding = embedder(text)
    return [item for sublist in embedding for item in sublist]