from ChatBot import os
import importlib.util
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

stopwords = set(stopwords.words("portuguese") + list(punctuation))

def import_module_from_file(directory:str):
    module = None
    try:
        module_file = os.path.split(directory)[1]
        module_name = os.path.splitext(module_file)[0]
        spec = importlib.util.spec_from_file_location(module_name, directory)
        module = spec.loader.load_module()
    except Exception as error:
        print(error)
    finally:
        return module

def processText(text:str):
    palavras = {palavra for palavra in word_tokenize(text.lower()) if not palavra in punctuation}
    return palavras

Semelhanca = lambda entrada, padrao: (len(entrada.intersection(padrao)) * 100) // len(padrao)

detectar_karen = lambda entrada: "Karen" in entrada[0:5] #or "karen" in entrada[-5]

process_entrada = lambda entrada: entrada.strip("Karen")[1:].capitalize()