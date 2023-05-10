import re
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
    txt_files = [f for f in listdir(TXT_DIR) if f.lower().endswith('.txt') and not regex.search(f)]

    # # obtener el archivo txt en txt_files con el mayor numero de caracteres
    # max_file = max(txt_files, key=lambda x: len(open(path.join(TXT_DIR, x), 'r', encoding='utf-8').read()))
    # nlp.max_length = len(open(path.join(TXT_DIR, max_file), 'r', encoding='utf-8').read())

    batch_size = 10000  # Set the batch size to a reasonable value
    last_words = ""  # Initialize last_words to an empty string

    for file in tqdm(txt_files):
        with open(path.join(TXT_DIR, file), 'r', encoding='utf-8') as f:
            text = f.read()

        # Split the text into smaller chunks
        chunks = [text[i:i+batch_size] for i in range(0, len(text), batch_size)]

        # Process each chunk separately
        for i, chunk in enumerate(nlp.pipe(chunks)):
            # If this is not the first chunk, prepend the last_words to the current chunk
            if i > 0:
                chunk = nlp(last_words + chunk.text)

            # Update last_words to the last few words of the current chunk
            last_words = " ".join(chunk.text.split()[-10:])

            # Extract the sentences from the chunk
            sentences = [sent.text.strip() for sent in chunk.sents if sent.text.strip()]

            # Print the sentences for this chunk
            print(sentences)





if __name__ == '__main__':
    # main()
    # print(TXT_DIR)
    get_sentences()