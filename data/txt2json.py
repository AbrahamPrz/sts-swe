from tqdm.auto import tqdm
from os import makedirs, listdir, path
import json
import spacy

nlp = spacy.load("es_dep_news_trf")


BASE_DIR = path.dirname(path.realpath(__file__))
TXT_DIR = path.join(BASE_DIR, "txt")
JSON_DIR = path.join(BASE_DIR, "json")

# TODO:
# Encontrar mejor manera de separar las oraciones en lugar de usar el punto como separador.
# 
def main(args=None):
    makedirs(JSON_DIR, exist_ok=True)
    # leer cada archivo txt en el directorio txt
    for file in tqdm(listdir(TXT_DIR)):
        oraciones = []
        texto = open(path.join(TXT_DIR, file), 'r').read()
        for oracion in texto.split('.'):
            oraciones.append(oracion)
        json_file = f'{file[:-4]}.json'
        with open(path.join(JSON_DIR, json_file), 'w', encoding='utf-8') as f:
            json.dump(oraciones, f)


def get_sentences(args=None):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp('This is the first sentence. This is the second sentence.')
    for sent in doc.sents:
        print(sent)

if __name__ == '__main__':
    main()
    # print(TXT_DIR)