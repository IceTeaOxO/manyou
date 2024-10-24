import whisper
import torch
from pyannote.audio import Pipeline
from moviepy.editor import VideoFileClip
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

def extract_audio(file_path):
    """從視頻文件中提取音頻"""
    video = VideoFileClip(file_path)
    audio_path = "extracted_audio.wav"
    video.audio.write_audiofile(audio_path)
    return audio_path

def transcribe_with_whisper(audio_path):
    """使用 Whisper 生成帶時間戳的逐字稿"""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result

def format_transcript(segments, with_timestamps=True):
    """格式化逐字稿"""
    transcript = ""
    for segment in segments:
        if with_timestamps:
            start = f"{segment['start']:.2f}"
            end = f"{segment['end']:.2f}"
            transcript += f"[{start} - {end}] {segment['text']}\n"
        else:
            transcript += f"{segment['text']} "
    return transcript.strip()

def main(file_path):
    # 如果輸入是視頻文件，先提取音頻
    if file_path.endswith(('.mp4', '.avi', '.mov')):
        audio_path = extract_audio(file_path)
    else:
        audio_path = file_path

    # 使用 Whisper 生成逐字稿
    result = transcribe_with_whisper(audio_path)

    # 生成兩種版本的逐字稿
    transcript_with_timestamps = format_transcript(result["segments"], with_timestamps=True)
    transcript_without_timestamps = format_transcript(result["segments"], with_timestamps=False)

    # 將結果寫入文件
    with open("transcript_with_timestamps.txt", "w", encoding="utf-8") as f:
        f.write(transcript_with_timestamps)
    
    with open("transcript_without_timestamps.txt", "w", encoding="utf-8") as f:
        f.write(transcript_without_timestamps)

    print("逐字稿已生成完成。")
    print("帶時間戳的逐字稿保存在：/mnt/data/transcript_with_timestamps.txt")
    print("不帶時間戳的逐字稿保存在：/mnt/data/transcript_without_timestamps.txt")

# 假設我們有一個示例音頻文件
sample_audio = "Suno Truth Flame Trimmed.wav"

# 如果文件存在，則運行主程序
if os.path.exists(sample_audio):
    main(sample_audio)
else:
    print(f"示例音頻文件 {sample_audio} 不存在。請確保文件路徑正確。")