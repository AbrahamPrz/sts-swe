# Este código toma todos los archivos .pdf en un directorio pdf y los convierte en archivos .txt en un directorio txt.
# El texto de cada página en cada pdf se guarda en un archivo .txt separado. El nombre del archivo .txt es el
# nombre del pdf, seguido de un guión bajo y el número de página. El código utiliza la biblioteca PyPDF2 para
# leer en los pdf y extraer el texto de cada página.

from PyPDF2 import PdfReader
from tqdm.auto import tqdm
from os import makedirs, listdir, path

BASE_DIR = path.dirname(path.realpath(__file__))
PDF_DIR = path.join(BASE_DIR, "pdf")
TXT_DIR = path.join(BASE_DIR, "txt")


def main(args=None):
    makedirs(TXT_DIR, exist_ok=True)
    # obtener todos los archivos pdf dentro de PDF_DIR
    pdf_files = [f for f in listdir(PDF_DIR) if f.lower().endswith('.pdf')]
    for pdf in pdf_files:
        # leer el archivo pdf
        with open(path.join(PDF_DIR, pdf), 'rb') as f:
            pdf_reader = PdfReader(f)
            # leer el número de páginas en el archivo pdf
            pbar = tqdm(range(len(pdf_reader.pages)))
            # iterar sobre las páginas en el archivo pdf
            page_num = 0
            for page in pbar:
                pbar.set_description(f'Processing {pdf}')
                # obtener el texto de la página eliminando los saltos de línea
                text = pdf_reader.pages[page].extract_text().replace('\n', ' ')
                # escribir el texto en un archivo txt
                txt_file = f'{pdf[:-4]}_{page_num}.txt'
                # generar un archivo txt que contenga el texto de todos los archivos txt de un mismo pdf
                main_txt_file = f'{pdf[:-4]}.txt'
                with open(path.join(TXT_DIR, txt_file), 'w', encoding='utf-8') as f, open(path.join(TXT_DIR, main_txt_file), 'a', encoding='utf-8') as mwf:
                    # formatear el texto para normalizarlo
                    formatted_text = text.replace('\n', ' ').lower().replace('  ', ' ')
                    f.write(formatted_text)
                    mwf.write(formatted_text)
                    page_num += 1


if __name__=='__main__':
    main()
    