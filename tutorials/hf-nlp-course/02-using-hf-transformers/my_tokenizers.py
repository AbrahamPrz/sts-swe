CHECKPOINT = 'symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli'


def main(args=None):
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)

    sequence = "Usar los tokenizers de Hugging Face es muy fácil."
    # tokenization
    tokens = tokenizer.tokenize(sequence)
    print(tokens)
    
    # conversion to IDs
    ids = tokenizer.convert_tokens_to_ids(tokens)
    print(ids)
    
    # converting IDs back to a string
    decoded_string = tokenizer.decode(ids)
    print(decoded_string)


if __name__ == '__main__':
    main()