from faster_whisper import WhisperModel
import os
import ssl
from tkinter import Tk, filedialog

# SSL証明書エラーを回避（必要な場合）
ssl._create_default_https_context = ssl._create_unverified_context

def format_timestamp(seconds: float) -> str:
    """秒をSRT形式に変換"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"

def transcribe_with_faster_whisper(audio_path, srt_path):
    model = WhisperModel("base", device="cpu")
    print("\n🎙️ Transcribing with Faster-Whisper...")
    segments, info = model.transcribe(audio_path, language="en")

    # SRTファイル作成
    srt_entries = []
    for i, segment in enumerate(segments, start=1):
        start = format_timestamp(segment.start)
        end = format_timestamp(segment.end)
        text = segment.text.strip()

        srt_entries.append(f"{i}")
        srt_entries.append(f"{start} --> {end}")
        srt_entries.append(text)
        srt_entries.append("")

    # 選択された場所に保存
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_entries))

    print(f"\n✅ SRT ファイル作成完了: {srt_path}")

if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    # 音声ファイル選択
    audio_path = filedialog.askopenfilename(
        title="音声ファイルを選択",
        filetypes=[("音声ファイル", "*.wav *.mp3 *.m4a *.flac")]
    )
    if not audio_path:
        print("❌ ファイルが選択されませんでした。")
        exit()

    # 保存先と名前を指定（デフォルト名は音声ファイル名）
    default_name = os.path.splitext(os.path.basename(audio_path))[0] + ".srt"
    srt_path = filedialog.asksaveasfilename(
        title="SRTファイルの保存先を選択",
        defaultextension=".srt",
        filetypes=[("SRTファイル", "*.srt")],
        initialfile=default_name
    )
    if not srt_path:
        print("❌ 保存先が選択されませんでした。")
        exit()

    transcribe_with_faster_whisper(audio_path, srt_path)
