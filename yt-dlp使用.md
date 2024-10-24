當然，我很樂意為您介紹如何使用 yt-dlp 的命令行界面（CLI）來快速、客製化下載 YouTube 資源。yt-dlp 是一個非常強大的工具，有許多選項可以讓您根據需求進行客製化下載。以下是一些常用的命令和選項：

1. 基本下載：
   ```
   yt-dlp https://www.youtube.com/watch?v=VIDEO_ID
   ```
   這會下載最佳品質的視頻。

2. 只下載音頻（MP3格式）：
   ```
   yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=VIDEO_ID
   ```

3. 下載特定品質的視頻：
   ```
   yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" https://www.youtube.com/watch?v=VIDEO_ID
   ```
   這會下載最高 1080p 的視頻。

4. 下載整個播放列表：
   ```
   yt-dlp https://www.youtube.com/playlist?list=PLAYLIST_ID
   ```

5. 下載字幕：
   ```
   yt-dlp --write-sub --sub-lang en https://www.youtube.com/watch?v=VIDEO_ID
   ```
   這會下載英文字幕（如果有的話）。

6. 自定義輸出文件名：
   ```
   yt-dlp -o "%(title)s-%(id)s.%(ext)s" https://www.youtube.com/watch?v=VIDEO_ID
   ```

7. 限制下載速度：
   ```
   yt-dlp --limit-rate 1M https://www.youtube.com/watch?v=VIDEO_ID
   ```
   這會將下載速度限制在 1 MB/s。

8. 下載縮圖：
   ```
   yt-dlp --write-thumbnail https://www.youtube.com/watch?v=VIDEO_ID
   ```

9. 下載特定時間範圍的視頻片段：
   ```
   yt-dlp --download-sections "*00:00:30-00:02:00" https://www.youtube.com/watch?v=VIDEO_ID
   ```
   這會下載從 30 秒到 2 分鐘的視頻片段。

10. 使用代理伺服器：
    ```
    yt-dlp --proxy socks5://127.0.0.1:9150/ https://www.youtube.com/watch?v=VIDEO_ID
    ```

11. 顯示所有可用的格式：
    ```
    yt-dlp -F https://www.youtube.com/watch?v=VIDEO_ID
    ```
    然後您可以選擇特定的格式：
    ```
    yt-dlp -f FORMAT_CODE https://www.youtube.com/watch?v=VIDEO_ID
    ```

12. 下載並嵌入字幕：
    ```
    yt-dlp --write-sub --write-auto-sub --embed-subs https://www.youtube.com/watch?v=VIDEO_ID
    ```

13. 批量下載（從文件中讀取 URL）：
    ```
    yt-dlp -a urls.txt
    ```
    其中 urls.txt 是包含多個 YouTube URL 的文本文件。

14. 更新 yt-dlp：
    ```
    yt-dlp -U
    ```

使用這些命令時，您可以組合多個選項來滿足特定需求。例如，如果您想下載 720p 的視頻，轉換為 mp4 格式，並下載英文字幕，您可以使用：

```
yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" --merge-output-format mp4 --write-sub --sub-lang en https://www.youtube.com/watch?v=VIDEO_ID
```

記住，yt-dlp 有非常豐富的選項和功能。您可以通過運行 `yt-dlp --help` 來查看所有可用的選項。此外，yt-dlp 的官方文檔也提供了更詳細的信息和使用示例。

最後，請記住遵守 YouTube 的服務條款和版權法。確保您有權下載和使用這些內容。