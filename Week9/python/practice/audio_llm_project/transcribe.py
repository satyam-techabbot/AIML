import os, pyttsx3, wave, pyaudio
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq (
    api_key=os.getenv("GROQ_API_KEY")
)

def record_audio(filename, duration=5):
    """Records audio from the mic for a set duration."""
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    
    p = pyaudio.PyAudio()
    stream = p.open (
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    print(f"--- Recording for {duration} seconds... ---")
    frames = []

    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("--- Recording Complete. Transcribing... ---")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def transcribe_audio(filename):
    """Sends the audio file to Groq for transcription."""
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3-turbo",
            response_format="text"
        )
    return transcription

def say_text_local(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175) 
    engine.setProperty('volume', 0.9)
    
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    audio_file = "temp_recording.wav"

    record_audio(audio_file, duration=5)
    result_text = transcribe_audio(audio_file)
    
    print("\nTRANSCRIPTION:")
    print("-" * 20)
    print(result_text)
    print("-" * 20)

    say_text_local(result_text)
    
    if os.path.exists(audio_file):
        os.remove(audio_file)