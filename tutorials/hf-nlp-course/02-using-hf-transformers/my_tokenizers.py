MODEL_CHOICE = 'symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli'


def main(args=None):
    from transformers import BertTokenizer

    tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

    sequence = "Using a Transformer network is simple"
    tokens = tokenizer.tokenize(sequence)

    print(tokens)


if __name__ == '__main__':
    main()