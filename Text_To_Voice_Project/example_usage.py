"""
Example usage of Text to Voice Converters
Shows different ways to use the converters programmatically
"""

from text_to_voice_offline import TextToVoiceOffline
from text_to_voice_online import TextToVoiceOnline

def example_offline_basic():
    """Basic offline conversion"""
    print("\n=== Example 1: Basic Offline Conversion ===")
    
    converter = TextToVoiceOffline()
    text = "Hello World! This is a text to speech example."
    converter.speak(text)


def example_offline_save():
    """Save offline speech to file"""
    print("\n=== Example 2: Save Offline Speech to File ===")
    
    converter = TextToVoiceOffline()
    text = "This audio file has been saved from text to speech conversion."
    converter.save_to_file(text, "example_output.mp3")


def example_offline_custom_settings():
    """Offline conversion with custom settings"""
    print("\n=== Example 3: Custom Settings ===")
    
    converter = TextToVoiceOffline()
    
    # Set slower speed for clarity
    converter.set_speed(80)
    
    # Set higher volume
    converter.set_volume(1.0)
    
    # Use different voice
    converter.set_voice(0)  # Try voice index 0
    
    text = "This is a slower speech with custom settings."
    converter.speak(text)


def example_offline_voice_comparison():
    """Compare different voices"""
    print("\n=== Example 4: Voice Comparison ===")
    
    converter = TextToVoiceOffline()
    text = "Testing different voice options."
    
    voices = converter.engine.getProperty('voices')
    print(f"Found {len(voices)} available voices")
    
    for i, voice in enumerate(voices):
        print(f"\n--- Voice {i}: {voice.name} ---")
        converter.set_voice(i)
        converter.speak(text)


def example_online_basic():
    """Basic online conversion"""
    print("\n=== Example 5: Basic Online Conversion ===")
    
    converter = TextToVoiceOnline()
    text = "Hello! This is Google Text to Speech."
    converter.speak(text)


def example_online_multilanguage():
    """Multi-language online conversion"""
    print("\n=== Example 6: Multi-Language Conversion ===")
    
    texts = {
        'en': 'Hello in English',
        'es': 'Hola en español',
        'fr': 'Bonjour en français',
        'de': 'Hallo auf Deutsch',
    }
    
    for lang_code, text in texts.items():
        print(f"\nConverting to {lang_code}...")
        converter = TextToVoiceOnline(language=lang_code)
        converter.save_to_file(text, f'example_{lang_code}.mp3')


def example_online_file_processing():
    """Process text file to speech"""
    print("\n=== Example 7: Process Text File ===")
    
    # First, create a sample text file
    sample_text = """
    The quick brown fox jumps over the lazy dog.
    This is a sample text file for conversion.
    All the vowels are present in this sentence.
    """
    
    with open('sample_input.txt', 'w') as f:
        f.write(sample_text)
    
    # Convert file to speech
    converter = TextToVoiceOnline()
    converter.process_text_file('sample_input.txt', 'example_from_file.mp3')


def example_batch_conversion():
    """Batch convert multiple texts"""
    print("\n=== Example 8: Batch Conversion ===")
    
    messages = [
        "First message",
        "Second message",
        "Third message",
        "Fourth message"
    ]
    
    converter = TextToVoiceOffline()
    
    for i, message in enumerate(messages):
        output_file = f'batch_output_{i+1}.mp3'
        converter.save_to_file(message, output_file)
        print(f"Saved: {output_file}")


def example_speed_variations():
    """Create speech with different speeds"""
    print("\n=== Example 9: Speed Variations ===")
    
    converter = TextToVoiceOffline()
    text = "The speed of this speech varies."
    speeds = [80, 120, 150, 200]
    
    for speed in speeds:
        converter.set_speed(speed)
        output_file = f'speed_{speed}.mp3'
        converter.save_to_file(text, output_file)
        print(f"Saved at {speed} wpm: {output_file}")


def example_volume_levels():
    """Create speech with different volumes"""
    print("\n=== Example 10: Volume Levels ===")
    
    converter = TextToVoiceOffline()
    text = "Testing different volume levels."
    volumes = [0.3, 0.6, 0.9]
    
    for volume in volumes:
        converter.set_volume(volume)
        output_file = f'volume_{int(volume*100)}.mp3'
        converter.save_to_file(text, output_file)
        print(f"Saved at {volume*100}% volume: {output_file}")


# Main execution
if __name__ == "__main__":
    print("=" * 50)
    print("TEXT TO VOICE - USAGE EXAMPLES")
    print("=" * 50)
    
    try:
        # Uncomment the examples you want to run:
        
        example_offline_basic()
        example_offline_custom_settings()
        example_offline_save()
        
        # example_offline_voice_comparison()  # Takes time, comment out if not needed
        
        # example_online_basic()  # Requires internet
        # example_online_multilanguage()  # Requires internet
        # example_online_file_processing()  # Requires internet
        
        example_batch_conversion()
        
        # example_speed_variations()  # Takes time
        # example_volume_levels()  # Takes time
        
        print("\n" + "=" * 50)
        print("✓ Examples completed!")
        print("=" * 50)
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
