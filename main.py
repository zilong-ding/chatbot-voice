from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QAudioRecorder, QAudioEncoderSettings

# 创建 QAudioRecorder 对象
audio_recorder = QAudioRecorder()

# 创建音频编码器设置对象
audio_settings = QAudioEncoderSettings()

# 设置音频编码器为 WAV 格式
audio_settings.setCodec("audio/x-wav")

# 设置音频采样率为 44100 Hz
audio_settings.setSampleRate(44100)

# 设置音频通道数为 2
audio_settings.setChannelCount(2)

# 设置音频比特率为 128 kbps
audio_settings.setBitRate(128000)

# 设置音频编码器设置
audio_recorder.setEncodingSettings(audio_settings)

# 定义要保存的文件路径和文件名
save_file_path = "C:/Users/31136/PycharmProjects/pythonProject/temp/file.wav"

# 定义音频文件保存的 URL
audio_file_url = QUrl.fromLocalFile(save_file_path)

# 设置音频文件保存的 URL
audio_recorder.setOutputLocation(audio_file_url)

# 开始录制音频
audio_recorder.record()
for i in range(10000):
    a = i
# 停止录制音频
audio_recorder.stop()
