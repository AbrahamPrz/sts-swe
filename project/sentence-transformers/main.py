from sentence_transformers import SentenceTransformer, SentencesDataset, InputExample, losses

def main(args=None):
    model = SentenceTransformer('symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli')
    train_examples = [InputExample(texts=['My first sentence', 'My second sentence'], label=0.8),
        InputExample(texts=['Another pair', 'Unrelated sentence'], label=0.3)]
    train_dataset = SentencesDataset(train_examples, model)
    print(train_dataset.__getitem__(0))

if __name__ == '__main__':
    main()