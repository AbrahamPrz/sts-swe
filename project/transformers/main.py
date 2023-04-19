# Cargar dataset
# Cargar modelo de HF a utilizar (symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli)
# Usar tokenizer para tokenizar el dataset
# ...

from transformers import AutoTokenizer
from os import path, listdir


BASE_DIR = path.dirname(path.realpath(__file__))
# get the base project path
INITIAL_PATH = path.dirname(path.dirname(BASE_DIR))
DATA_DIR = path.join(INITIAL_PATH, 'data')
TXT_DIR = path.join(DATA_DIR, 'txt')
EXAMPLE_FILE = path.join(BASE_DIR, 'example.txt')
CHECKPOINT = 'symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli'


def main(args=None):
    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)
    for file in listdir(TXT_DIR):
        if file.endswith('.txt'):
            text = open(path.join(TXT_DIR, file), 'r').read()
            tokens = tokenizer.tokenize(text)
            print(tokens)
    

if __name__ == '__main__':
    main()