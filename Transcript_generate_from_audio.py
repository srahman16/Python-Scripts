'''
Title: Transcript generation from any audio (.mp3)
Author: Shahriar Rahman
Version: 3b
Date: 31 August 2025

*** Pre-requisites: make sure you have OpenAI-Whisper (command: pip install -U openai-whisper) and ffmpeg (included in your system PATH) ***
'''
import os
import shutil
import sys
import whisper
import warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

audio_file_path = r"S:\Aud2Txt\abcdefg.mp3"
output_folder = r"S:\Aud2Txt"
model = whisper.load_model("small")  # Change to tiny/base/medium/large as needed
result = model.transcribe(audio_file_path, language="en")
transcript_text = result["text"].strip()
transcript_file = os.path.join(output_folder, "transcript.txt")
with open(transcript_file, "w", encoding="utf-8") as f:
    f.write(transcript_text)
print(f"Transcript saved to: {transcript_file}")
