# from . import all
import paddle

from utills.all import *

# paddle.set_device('gpu')
class translator():
    def __init__(self):
        self.asr = ASRExecutor()
        self.tts = TTSExecutor()
        self.text_punc = TextExecutor()

    def voice2text(self, file: str):
        return str(self.text_punc(text=self.asr(audio_file=file,force_yes=True)))

    def text2voice(self, text: str, file: str):
        self.tts(text=text, output=file)