import whisper

model = whisper.load_model("medium")
result = model.transcribe("./target/result.mp3")
print(result["text"])