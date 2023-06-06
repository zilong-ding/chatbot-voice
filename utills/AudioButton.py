import datetime
import os

from utills.all import *
from utills import translator

current_path = os.path.abspath(__file__)
parent_path = os.path.abspath(os.path.dirname(current_path))
parent_path = os.path.abspath(os.path.dirname(parent_path))

lstr = parent_path.split('\\')
parent_path = '/'.join(lstr)


def towinstyle(path: str):
    return '\\'.join(path.split('/'))


def tounixstyle(path: str):
    return '/'.join(path.split('\\'))


class random_file:
    def __init__(self):
        now = datetime.now()
        # 获取当前日期
        year = now.year
        month = now.month
        day = now.day

        # 获取当前时间
        hour = now.hour
        minute = now.minute
        second = now.second
        self.name = f'{year}-{month}-{day}-{hour}-{minute}-{second}'

    def get_name(self):
        # print(parent_path + '/temp/' + self.name + '.wav')
        return parent_path + '/temp/' + self.name + '.wav'

    def fresh(self):
        now = datetime.now()
        # 获取当前日期
        year = now.year
        month = now.month
        day = now.day

        # 获取当前时间
        hour = now.hour
        minute = now.minute
        second = now.second
        self.name = f'{year}-{month}-{day}-{hour}-{minute}-{second}'


class Audio:
    def __init__(self):
        # self.file_path = None
        self.file = None
        self.recorder = QAudioRecorder()
        self.translator = translator()
        self.wave_file = random_file()
        # self.file = '/temp/test.wav'
        settings = QAudioEncoderSettings()
        settings.setCodec("audio/x-wav")
        settings.setSampleRate(16000)
        settings.setChannelCount(1)
        settings.setQuality(QMultimedia.VeryHighQuality)
        settings.setEncodingMode(QMultimedia.ConstantQualityEncoding)
        # self.recorder.setOutputLocation(QtCore.QUrl.fromLocalFile(self.file))
        self.recorder.setAudioSettings(settings)
        self.player = QMediaPlayer()
        self.count = 0

    def record(self):
        self.player.stop()
        # self.player.
        if os.path.exists(parent_path + '/' + 'temp/answer' + str(self.count) + '.wav'):
            os.remove(parent_path + '/' + 'temp/answer' + str(self.count) + '.wav')
        self.wave_file.fresh()
        self.file = self.wave_file.get_name()
        # print("self.file", QtCore.QUrl.fromLocalFile(self.file))
        self.recorder.setOutputLocation(QtCore.QUrl.fromLocalFile(self.file))
        # print('failed')
        self.recorder.record()

    def stop(self):
        self.recorder.stop()
        # print('self.file', self.file)
        if not os.path.exists(self.file):
            # print('not find')
            return
        text = self.translator.voice2text(self.file)
        # print(text)
        return text

    def play(self, text):
        # content = None
        self.count += 1
        file_path = 'temp/answer' + str(self.count) + '.wav'
        file_path = parent_path + '/' + file_path
        self.translator.text2voice(text, file_path)
        # print(file_path)
        if not os.path.exists(file_path):
            print('not find')
            return
        print('find it')
        content = QMediaContent(QtCore.QUrl.fromLocalFile(file_path))
        self.player.setMedia(content)
        # self.player.s
        self.player.play()
        os.remove(self.file)


# class AudioButton(QPushButton):
#     def __init__(self, parent=None):
#         super(AudioButton, self).__init__(parent)
#         self.recorder = QAudioRecorder()
#         self.translator = translator()
#         settings = QAudioEncoderSettings()
#         settings.setCodec("audio/pcm")
#         settings.setSampleRate(16000)
#         settings.setChannelCount(1)
#         settings.setQuality(QMultimedia.VeryHighQuality)
#         settings.setEncodingMode(QMultimedia.ConstantQualityEncoding)
#         self.recorder.setAudioSettings(settings)
# self.recorder.setOutputFormat(QAudioRecorder.AudioRecorder.WavFormat)

#     self.recorder.setOutputLocation(
#         QtCore.QUrl.fromLocalFile("C:/Users/31136/PycharmProjects/pythonProject/temp/audio.wav"))
#     self.player = QMediaPlayer()
#     self.setGeometry(QtCore.QRect(310, 410, 93, 28))
#     self.setStyleSheet("font: 9pt \"微软雅黑\";\n"
#                        "background-color: rgb(0, 255, 127);")
#     self.setObjectName("pushButton")
#
#     self.pressed.connect(self.start_recording)
#     self.released.connect(self.play_audio)
#     self.count = 0
#
# def start_recording(self):
#     self.recorder.record()
#     # print(self.count)
#     # self.count += 1

# def stop_recording(self):
#     self.recorder.stop()
#     if not os.path.exists("C:/Users/31136/PycharmProjects/pythonProject/temp/audio.wav"):
#         return
#     print(self.translator.voice2text("C:/Users/31136/PycharmProjects/pythonProject/temp/audio.wav"))
#
# def play_audio(self):
#     self.stop_recording()
#     # self.recorder.stop()
#     if not os.path.exists("C:/Users/31136/PycharmProjects/pythonProject/temp/audio.wav"):
#         return
#     # print(self.translator.voice2text("C:/Users/31136/PycharmProjects/pythonProject/temp/audio.wav"))
#     content = QMediaContent(
#         QtCore.QUrl.fromLocalFile("C:/Users/31136/PycharmProjects/pythonProject/temp/audio.wav"))
#     # print(content)
#     self.player.setMedia(content)
#     self.player.play()
