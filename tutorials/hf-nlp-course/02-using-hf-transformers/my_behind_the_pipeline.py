def main(args=None):
    from transformers import AutoTokenizer

    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)

    raw_inputs = [
        "First example",
        "Another example with more words",
    ]
    inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")
    print(f'Inputs tokenized: \n {inputs}')


    from transformers import AutoModel

    model = AutoModel.from_pretrained(checkpoint)
    outputs = model(**inputs)
    # Muestra un vector que contiene tres dimensiones: [Batch size, Sequence length, Hidden size]
    print(f'Last hidden state shape: \n{outputs.last_hidden_state.shape}')


    from transformers import AutoModelForSequenceClassification

    model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
    outputs = model(**inputs)
    print(f'Logits shape: \n{outputs.logits.shape}')
    # Los logts son los valores de salida de la capa de clasificación que necesitan ser transformados en probabilidades
    print(f'Logits: \n{outputs.logits}')


    import torch

    predictions = torch.softmax(outputs.logits, dim=-1)
    print(f'Predictions: \n{predictions}')


    # Se inspeccionan los labels del modelo
    print(f'ID labels: {model.config.id2label}')

    # Segun los ID labels, el primer resultado se clasifica como positivo (2% negativo y 98% positivo) y el segundo como negativo (75% negativo y 25% positivo)


if __name__ == '__main__':
    main()