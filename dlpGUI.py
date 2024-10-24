import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal
import yt_dlp

class DownloadThread(QThread):
    progress = pyqtSignal(float)
    finished = pyqtSignal()

    def __init__(self, url, output_format, output_path):
        super().__init__()
        self.url = url
        self.output_format = output_format
        self.output_path = output_path

    def run(self):
        ydl_opts = {
            'format': 'bestaudio/best' if self.output_format == 'mp3' else 'bestvideo+bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if self.output_format == 'mp3' else [],
            'outtmpl': f'{self.output_path}/%(title)s.%(ext)s',
            'progress_hooks': [self.progress_hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

        self.finished.emit()

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            p = d.get('_percent_str', '0%')
            # 使用正則表達式來提取數字
            p_clean = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', p)
            p_clean = re.sub(r'[^\d.]', '', p_clean)
            try:
                p_float = float(p_clean)
                self.progress.emit(p_float)
            except ValueError:
                # 如果轉換失敗，發送0作為進度
                self.progress.emit(0)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        url_layout = QHBoxLayout()
        url_label = QLabel('URL:')
        self.url_input = QLineEdit()
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_input)
        layout.addLayout(url_layout)

        format_layout = QHBoxLayout()
        format_label = QLabel('輸出格式:')
        self.format_combo = QComboBox()
        self.format_combo.addItems(['mp3', 'mp4'])
        format_layout.addWidget(format_label)
        format_layout.addWidget(self.format_combo)
        layout.addLayout(format_layout)

        output_layout = QHBoxLayout()
        self.output_path = QLineEdit()
        output_button = QPushButton('選擇輸出路徑')
        output_button.clicked.connect(self.choose_output_path)
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(output_button)
        layout.addLayout(output_layout)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        download_button = QPushButton('下載')
        download_button.clicked.connect(self.start_download)
        layout.addWidget(download_button)

        self.setLayout(layout)
        self.setWindowTitle('YT-DLP 下載器')
        self.setGeometry(300, 300, 400, 200)

    def choose_output_path(self):
        folder = QFileDialog.getExistingDirectory(self, "選擇輸出資料夾")
        if folder:
            self.output_path.setText(folder)

    def start_download(self):
        url = self.url_input.text()
        output_format = self.format_combo.currentText()
        output_path = self.output_path.text()

        if not url or not output_path:
            return

        self.download_thread = DownloadThread(url, output_format, output_path)
        self.download_thread.progress.connect(self.update_progress)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.start()

    def update_progress(self, percentage):
        self.progress_bar.setValue(int(percentage))

    def download_finished(self):
        self.progress_bar.setValue(100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())