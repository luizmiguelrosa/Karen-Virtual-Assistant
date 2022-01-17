import wikipedia
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from threading import Thread

stopwords = set(stopwords.words("portuguese") + list(punctuation))

class acoes:
    def __init__(self):
        wikipedia.set_lang("pt")
        self.result_passwords = []
        self.out = {}
    
    def processText(self, text:str):
        palavras = [palavra for palavra in list(dict.fromkeys(word_tokenize(text.lower()))) if palavra not in stopwords and len(palavra) <= 25 and not "Lista de" in palavra]
        for p in palavras:
            self.result_passwords += [word for word in wikipedia.search(p) if not word in self.result_passwords]
    
    def searchWikipedia(self, search:str):
        try:
            result = wikipedia.summary(search, sentences=1)
            if self.writeInLibrary(search, result):
                return self.out
        except wikipedia.exceptions.DisambiguationError:
            pass
    
    def writeInLibrary(self, title:str, data:str):
        result = False
        if not title in self.out:
            self.out[title] = data
            result = True
        return result
    
    def saida(self, entrada):
        a = acoes()
        result = a.searchWikipedia(entrada)
        for r in result:
            return result[r]


class processPasswords(Thread):
    def __init__(self, wk, word):
        Thread.__init__(self)
        self.wk = wk()
        self.word = word

    def run(self):
        self.wk.searchWikipedia(self.word)