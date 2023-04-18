CHECKPOINT = 'symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli'


def main(args=None):
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)

    sequences = [
        "Estoy avanzando en el curso de Hugging Face.",
        "Usar los tokenizers de Hugging Face es muy fácil gracias al curso."
    ]

    model_inputs = tokenizer(sequences, padding=True) # True == 'longest'?
    # model_inputs = tokenizer(sequences, truncation=True, max_length=5)
    # model_inputs = tokenizer(sequences, padding=True, return_tensors='pt')
    print(model_inputs)
    
    
    model_inputs = tokenizer(sequences[0])
    print(model_inputs['input_ids'])
    
    tokens = tokenizer.tokenize(sequences[0])
    ids = tokenizer.convert_tokens_to_ids(tokens)
    print(ids)
    
    
    print(tokenizer.decode(model_inputs["input_ids"]))
    print(tokenizer.decode(ids))
    

def from_tokenizer_to_model(args=None):
    import torch
    from transformers import AutoTokenizer, AutoModelForSequenceClassification

    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)
    model = AutoModelForSequenceClassification.from_pretrained(CHECKPOINT)
    sequences = [
        "Estoy avanzando en el curso de Hugging Face.",
        "Usar los tokenizers de Hugging Face es muy fácil gracias al curso."
    ]

    tokens = tokenizer(sequences, padding=True, truncation=True, return_tensors="pt")
    output = model(**tokens)
    
    print(output)


if __name__ == '__main__':
    # main()
    from_tokenizer_to_model()