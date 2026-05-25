"""
Text to Voice Converter - Offline Version using pyttsx3
No internet required, works offline
"""

import pyttsx3
import os

class TextToVoiceOffline:
    def __init__(self):
        """Initialize the text-to-speech engine"""
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
        
    def set_voice(self, voice_id=0):
        """Set the voice (0 for male, 1 for female if available)"""
        voices = self.engine.getProperty('voices')
        if voice_id < len(voices):
            self.engine.setProperty('voice', voices[voice_id].id)
            
    def set_speed(self, speed):
        """Set speech speed (recommended: 50-200)"""
        self.engine.setProperty('rate', speed)
        
    def set_volume(self, volume):
        """Set volume (0.0 to 1.0)"""
        if 0.0 <= volume <= 1.0:
            self.engine.setProperty('volume', volume)
    
    def speak(self, text):
        """Speak the text"""
        print(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def save_to_file(self, text, filename='output.mp3'):
        """Save speech to an MP3 file"""
        output_path = os.path.join(os.getcwd(), filename)
        self.engine.save_to_file(text, output_path)
        self.engine.runAndWait()
        print(f"Audio saved to: {output_path}")


def main():
    print("=== Text to Voice Converter (Offline) ===\n")
    
    # Create converter instance
    converter = TextToVoiceOffline()
    
    # List available voices
    voices = converter.engine.getProperty('voices')
    print(f"Available voices: {len(voices)}")
    for i, voice in enumerate(voices):
        print(f"  {i}: {voice.name}")
    
    print("\n--- Options ---")
    print("1. Speak text directly")
    print("2. Save text to audio file")
    print("3. Try different voices")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '1':
        text = input("Enter the text to speak: ")
        converter.speak(text)
        
    elif choice == '2':
        text = input("Enter the text to save: ")
        filename = input("Enter filename (default: output.mp3): ").strip()
        if not filename:
            filename = 'output.mp3'
        converter.save_to_file(text, filename)
        
    elif choice == '3':
        text = input("Enter the text to hear: ")
        voices = converter.engine.getProperty('voices')
        for i, voice in enumerate(voices):
            print(f"\n--- Voice {i}: {voice.name} ---")
            converter.set_voice(i)
            converter.speak(text)
    
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
