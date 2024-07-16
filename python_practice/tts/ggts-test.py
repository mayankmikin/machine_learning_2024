from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def generate_gtts_audio(text, language='hi', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)

def play_audio_with_pydub(audio_file):
    audio = AudioSegment.from_mp3(audio_file)
    play(audio)

# Example usage
text = "नमस्ते दुनिया Player X hits a boundary! What a shot! YE LAGA DIA HAI SHOT ..... HAWA ME GEND"
output_file = "output.mp3"

# Generate speech with gTTS
generate_gtts_audio(text, output_file=output_file)

# Play the generated audio file wi
# th pydub
play_audio_with_pydub(output_file)
