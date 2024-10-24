import yt_dlp

def download_youtube(url):
    # MP3 下載設置
    ydl_opts_audio = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s_audio.%(ext)s'
    }

    # MP4 下載設置
    ydl_opts_video = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s_video.%(ext)s'
    }

    try:
        # 下載 MP3
        print("正在下載 MP3...")
        with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
            ydl.download([url])

        # 下載 MP4
        print("正在下載 MP4...")
        with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
            ydl.download([url])

        print("下載完成！檢查當前目錄以查看下載的文件。")
    except Exception as e:
        print(f"下載過程中發生錯誤: {str(e)}")

def main():
    while True:
        video_url = input("請輸入 YouTube 影片的 URL (輸入 'q' 退出): ")
        if video_url.lower() == 'q':
            print("程式結束。")
            break
        download_youtube(video_url)
        print("\n")  # 為了更好的可讀性，在每次下載後添加一個空行

if __name__ == "__main__":
    main()
