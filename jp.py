import whisper
import torch
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

# 檢查是否有可用的 GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"使用設備: {device}")

# 載入 Whisper 模型
model = whisper.load_model("medium", device=device)

# 音頻文件路徑（這裡使用示例路徑，實際使用時請替換為您的音頻文件路徑）
audio_path = "Suno Truth Flame Trimmed.wav"

# 轉錄音頻
result = model.transcribe(audio_path, language="ja")

# 輸出帶有時間戳的逐字稿
for segment in result["segments"]:
    start_time = segment["start"]
    end_time = segment["end"]
    text = segment["text"]
    print(f"[{start_time:.2f} - {end_time:.2f}] {text}")

print("\n完整的轉錄文本：")
print(result["text"])