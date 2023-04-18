MODEL_CHOICE = 'symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli'


def main(args=None):
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(MODEL_CHOICE)

    sequence = "Usar los tokenizers de Hugging Face es muy fácil."
    tokens = tokenizer.tokenize(sequence)

    print(tokens)


if __name__ == '__main__':
    main()