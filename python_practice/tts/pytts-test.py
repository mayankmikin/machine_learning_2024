import pyttsx3

def text_to_speech(text,language='hi'):
    engine = pyttsx3.init("espeak")
    
    # Get available voices
    voices = engine.getProperty('voices')
    
    # find hindi speaker 
    voice_id = next((v for v in voices if v.id == language), None)
    engine.setProperty('voice', voice_id)
    # Choose a voice (e.g., female voice)
    # engine.setProperty('voice', voices[1].id)
    
    # Set speech rate
    engine.setProperty('rate', 150)
    
    # Set volume (0.0 to 1.0)
    engine.setProperty('volume',1.0)
    
    # Speak the text
    engine.say(text)
    
    # Wait for the speech to finish
    engine.runAndWait()
    # for voice in voices:
    #     print(voice, voice.id)
    #     engine.setProperty('voice', voice.id)
    #     engine.say("YE LAGA DIA HAI SHOT ..... HAWA ME GEND")
    #     engine.runAndWait()
    #     engine.stop()

# Example usage
text = "Player X hits a boundary! What a shot! YE LAGA DIA HAI SHOT ..... HAWA ME GEND"
text_to_speech(text)
