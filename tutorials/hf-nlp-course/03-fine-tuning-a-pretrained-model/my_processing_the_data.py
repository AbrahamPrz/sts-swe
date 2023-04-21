def main(args=None):
    import torch
    from transformers import AdamW, AutoTokenizer, AutoModelForSequenceClassification

    # Same as before
    checkpoint = "symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
    sequences = [
        "Estoy avanzando en el curso de Hugging Face.",
        "Usar los tokenizers de Hugging Face es muy fácil gracias al curso."
    ]
    batch = tokenizer(sequences, padding=True, truncation=True, return_tensors="pt")
    
    # This is new
    batch["labels"] = torch.tensor([1, 1])

    optimizer = AdamW(model.parameters())
    loss = model(**batch).loss
    loss.backward()
    optimizer.step()


def loading_dataset(args=None):
    from datasets import load_dataset

    raw_datasets = load_dataset("glue", "mrpc")
    print(raw_datasets)    
    
    raw_train_dataset = raw_datasets["train"]
    print(raw_train_dataset[0])
    
    
    print(raw_datasets["train"]["sentence1"]) # Todas las oraciones de un archiv txt


def tokenize_function(example):
    pass
    # return tokenizer(example["sentence1"], example["sentence2"], truncation=True)


if __name__ == '__main__':
    # main()
    loading_dataset()