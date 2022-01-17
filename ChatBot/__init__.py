import pyttsx3, os, json, pyaudio
from vosk import Model, KaldiRecognizer
from ChatBot.utils import *

class Voz:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("volume", 2.5)
        rate = self.engine.getProperty("rate")
        self.engine.setProperty("rate", rate - 20)

        for voice in voices:
            if voice.name == "brazil":
                self.engine.setProperty("voice", voice.id)
                break

        model = Model("ChatBot/model")
        self.rec = KaldiRecognizer(model, 16000)

        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
        self.stream.start_stream()
    
    def escute(self):
        data = self.stream.read(2048)
        if self.rec.AcceptWaveform(data):
            result = self.rec.Result()
            result = json.loads(result)
            if result is not None:
                return result["text"].capitalize()
        else:
            return ""
    
    def fale(self, texto):
        self.engine.say(texto)
        self.engine.runAndWait()


class Interagir:
    def __init__(self):
        files = os.listdir("modules")
        self.modules = {file.strip(".py"):import_module_from_file(f"modules/{file}") for file in files if ".py" in file}
        with open("data/comandos.json", "r", encoding="utf8") as f:
            self.padroes = json.load(f)
    
    def process_semelhança(self, entrada):
        entrada = processText(entrada)
        result = {}
        for acao in self.padroes:
            for padrao in self.padroes[acao]:
                semelhanca = Semelhanca(entrada, padrao)
                if semelhanca >= 50:
                    result[acao] = semelhanca
                if 100 >= semelhanca >= 60:
                    break
        return result
    
    def process_max(self, semelhancas):
        if len(semelhancas) > 1:
            maior = False
            for acao in semelhancas:
                if not maior:
                    maior = acao
                elif semelhancas[acao] > semelhancas[maior]:
                    maior = acao
            return maior
        elif len(semelhancas) == 1:
            for acao in semelhancas:
                return acao
        else:
            return False
    
    def saida(self, entrada):
        semelhancas = self.process_semelhança(entrada)
        maior = self.process_max(semelhancas)
        if not maior:
            return "Não consegui processar nenhuma resposta para isto"
        else:
            print(entrada)
            return self.modules[maior].acoes.saida(self, entrada)