# 🎙 音声ファイルからSRT字幕を作成するツール / Speech-to-SRT Tool (Faster-Whisper + Tkinter)

---

## 🇯🇵 日本語

このツールは **[Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)** を使って  
音声ファイル（.wav, .mp3, .m4a, .flac）を **SRT字幕ファイル** に変換します。  
コマンドライン不要で、ファイル選択ダイアログから操作できます。

### ✨ 特徴
- GUI（Tkinter）でファイル選択・保存
- SRT形式で正確なタイムスタンプ
- CPU環境でも動作（デフォルト`base`モデル）
- `.wav` / `.mp3` / `.m4a` / `.flac` に対応

### 📦 必要環境
- Python **3.9+**
- [ffmpeg](https://ffmpeg.org/)（MP3/M4A対応用）

インストール:
```bash
pip install faster-whisper tk
# ffmpeg が必要な場合:
# macOS: brew install ffmpeg
# Windows: choco install ffmpeg
```

### 🚀 使い方
```bash
python transcribe_srt.py
```
1. 音声ファイルを選択  
2. 保存先とファイル名を指定  
3. 自動でSRTが生成されます  

---

## 🇺🇸 English

This tool uses **[Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)**  
to transcribe audio files (`.wav`, `.mp3`, `.m4a`, `.flac`) into **SRT subtitle files**.  
No command-line arguments required — fully operated via file dialogs.

### ✨ Features
- GUI (Tkinter) file picker for input/output
- Accurate timestamps in SRT format
- Runs on CPU by default (`base` model)
- Supports `.wav`, `.mp3`, `.m4a`, `.flac`

### 📦 Requirements
- Python **3.9+**
- [ffmpeg](https://ffmpeg.org/) (for MP3/M4A support)

Install:
```bash
pip install faster-whisper tk
# ffmpeg installation:
# macOS: brew install ffmpeg
# Windows: choco install ffmpeg
```

### 🚀 Usage
```bash
python transcribe_srt.py
```
1. Select your audio file  
2. Choose where to save the `.srt` file  
3. Subtitles will be generated automatically
