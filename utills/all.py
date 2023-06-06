from PyQt5.QtMultimedia import QAudioRecorder, QMediaPlayer, QMediaContent,QMultimedia,QAudioEncoderSettings
from PyQt5.QtWidgets import QPushButton,QTextEdit,QFileDialog
from paddlespeech.cli.text.infer import TextExecutor
from paddlespeech.cli.tts.infer import TTSExecutor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QIODevice, QFile, QBuffer, QByteArray
import pyaudio
import wave
import sys
import os
from PyQt5.QtMultimedia import QAudioFormat, QAudioInput, QAudioOutput
from datetime import datetime
from paddlespeech.cli.asr.infer import ASRExecutor






