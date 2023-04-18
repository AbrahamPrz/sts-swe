def main(args=None):
    import torch
    from transformers import AutoTokenizer, AutoModelForSequenceClassification

    checkpoint = "symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

    sequence = "He estado esperando por un curso de Hugging Face desde hace mucho tiempo."

    tokens = tokenizer.tokenize(sequence)
    ids = tokenizer.convert_tokens_to_ids(tokens)

    input_ids = torch.tensor([ids])
    print("Input IDs:", input_ids)

    output = model(input_ids)
    print("Logits:", output.logits)
    
    
    batched_ids = [ids, ids]
    print(batched_ids)
    
    
    sequence1_ids = [[200, 200, 200]]
    sequence2_ids = [[200, 200]]
    batched_ids = [
        [200, 200, 200],
        [200, 200, tokenizer.pad_token_id],
    ]

    print(model(torch.tensor(sequence1_ids)).logits)
    print(model(torch.tensor(sequence2_ids)).logits)
    print(model(torch.tensor(batched_ids)).logits)
    
    
    attention_mask = [
        [1, 1, 1],
        [1, 1, 0],
    ]

    outputs = model(torch.tensor(batched_ids), attention_mask=torch.tensor(attention_mask))
    print(outputs.logits)


if __name__ == '__main__':
    main()