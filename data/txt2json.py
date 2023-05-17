import re
from tqdm.auto import tqdm
from os import makedirs, listdir, path
import json
import spacy
import nltk

nlp = spacy.load("es_dep_news_trf")


BASE_DIR = path.dirname(path.realpath(__file__))
TXT_DIR = path.join(BASE_DIR, "txt")
JSON_DIR = path.join(BASE_DIR, "json")

# TODO:
# Encontrar mejor manera de separar las oraciones en lugar de usar el punto como separador.
# Tambien usar SpaCy y un modelo de STS de huggingface para encontrar oraciones con un contexto similar.
# El texto base para comparar el contexto de las oraciones podria estar formado de varias oraciones previamente seleccionadas para pertenecer al tema de ingenieria de software.
# 
# Considerar que HuggingFace permite categorizar oraciones en base a un tema.
# Tambien considerar que es recomendable analizar si una oracion esta completa o no segun el siguiente ejemplo:
# import spacy
# # Load the Spanish language model
# nlp = spacy.load('es_dep_news_trf')

# # Define a sample sentence
# text = "El rápido zorro marrón"

# # Process the text with spaCy
# doc = nlp(text)

# # Check if the last token in the sentence is a noun, verb, adjective, or adverb
# last_token = doc[-1]
# if last_token.pos_ in ['NOUN', 'VERB', 'ADJ', 'ADV']:
#     print("The sentence is complete.")
# else:
#     print("The sentence is incomplete.")
# 
# USAR GPT PARA OBTENER LAS ORACIONES A PARTIR DEL TEXTO? OPCION A TOMAR EN CUENTA.


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
    # usar una expresion regular para encontrar los archivos txt que no terminan con _{digito}.txt
    regex = re.compile(r'_[0-9]+.txt')
    sentences = []
    # Se usan los archivos de texto con los libros completos, no los que son pagina por pagina.
    txt_files = [f for f in listdir(TXT_DIR) if f.lower().endswith('.txt') and not regex.search(f)]
    
    for txt_file in txt_files:
        with open(TXT_DIR + "/" + txt_file, 'r') as file:
            texto = file.read()
        # nltk proporciona una funcion para separar un texto en oraciones.
        oraciones = nltk.sent_tokenize(texto) 

        for oracion in oraciones:
            sentences.append(oracion)
        
        return sentences


def clean_sentences(sentences):
    # Lista de las oraciones limpias.
    clear_sentences = []
    for sentence in tqdm(sentences):
        doc = nlp(sentence)
        tokens_limpios = []
        
        for token in doc:
            if not token.is_punct and not token.like_num:
                tokens_limpios.append(token.text.strip())

        clear_sentence = ' '.join(tokens_limpios)
        clear_sentences.append(clear_sentence) if clear_sentence.strip() != '' else None

    return clear_sentences


if __name__ == '__main__':
    sentences = get_sentences()
    clear_sentences = clean_sentences(sentences)
    for sentence in clear_sentences:
        print(sentence)