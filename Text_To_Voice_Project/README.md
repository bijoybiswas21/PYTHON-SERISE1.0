# Text to Voice Converter - Python Project

A comprehensive Python project for converting text to voice with multiple implementations.

## Features

 **Offline Conversion** - No internet required  
 **Online Conversion** - Support for multiple languages  
 **GUI Interface** - User-friendly graphical interface  
 **Batch Processing** - Convert entire text files  
 **Multiple Languages** - Support for 10+ languages (online version)  
 **Customizable** - Control speed, volume, and voice selection  

## Project Structure

```
Text_To_Voice_Project/
├── text_to_voice_offline.py    # Offline implementation (pyttsx3)
├── text_to_voice_online.py     # Online implementation (gTTS)
├── gui_converter.py             # GUI version with Tkinter
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Packages:
- **pyttsx3** - Offline text-to-speech engine
- **gTTS** - Google Text-to-Speech library

### 2. Installation on Windows

```bash
pip install pyttsx3 gTTS
```

### 3. Installation on macOS

```bash
pip install pyttsx3 gTTS
```

### 4. Installation on Linux

```bash
pip install pyttsx3 gTTS
# For audio playback on Linux
sudo apt-get install mpg321
```

## Usage

### Option 1: Offline Converter (Recommended)

```bash
python text_to_voice_offline.py
```

**Features:**
- No internet required
- Fast conversion
- Multiple voice options
- Save to MP3 file
- Direct speech output

**Interactive Menu:**
1. Speak text directly
2. Save text to audio file
3. Try different voices

### Option 2: Online Converter (Google TTS)

```bash
python text_to_voice_online.py
```

**Features:**
- Support for 10+ languages
- High-quality speech
- Requires internet connection
- Save to MP3 file
- Process entire text files

**Supported Languages:**
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Russian (ru)
- Japanese (ja)
- Chinese (zh)
- Hindi (hi)

### Option 3: GUI Converter (Easiest)

```bash
python gui_converter.py
```

**Features:**
- User-friendly interface
- Real-time speed and volume control
- Voice selection dropdown
- Save and speak buttons
- Status bar

## Code Examples

### Using Offline Converter Programmatically

```python
from text_to_voice_offline import TextToVoiceOffline

# Create converter
converter = TextToVoiceOffline()

# Set speed (50-200, default 150)
converter.set_speed(100)

# Set volume (0.0-1.0)
converter.set_volume(0.8)

# Speak text
converter.speak("Hello, this is a test!")

# Save to file
converter.save_to_file("Hello World", "greeting.mp3")
```

### Using Online Converter Programmatically

```python
from text_to_voice_online import TextToVoiceOnline

# Create converter
converter = TextToVoiceOnline(language='en')

# Change language
converter.set_language('es')  # Spanish

# Save to file
converter.save_to_file("Hola Mundo", "greeting_es.mp3")

# Process entire file
converter.process_text_file("input.txt", "output.mp3")
```

### Using GUI Converter

```python
import tkinter as tk
from gui_converter import TextToVoiceGUI

root = tk.Tk()
app = TextToVoiceGUI(root)
root.mainloop()
```

## Common Issues & Solutions

### Issue: "pyttsx3 initialization failed"
**Solution:** Reinstall pyttsx3
```bash
pip uninstall pyttsx3
pip install pyttsx3
```

### Issue: "No audio output on Linux"
**Solution:** Install audio player
```bash
sudo apt-get install mpg321
```

### Issue: "gTTS requires internet"
**Solution:** Use offline converter instead
```bash
python text_to_voice_offline.py
```

### Issue: "File not found when saving"
**Solution:** Check file path and permissions
```bash
# Check current directory
python -c "import os; print(os.getcwd())"
```

## Advanced Usage

### Batch Process Multiple Files

```python
from text_to_voice_offline import TextToVoiceOffline
import os

converter = TextToVoiceOffline()
text_files = [f for f in os.listdir('.') if f.endswith('.txt')]

for text_file in text_files:
    with open(text_file, 'r') as f:
        text = f.read()
    output = text_file.replace('.txt', '.mp3')
    converter.save_to_file(text, output)
    print(f"Converted: {text_file} -> {output}")
```

### Multi-language Conversion

```python
from text_to_voice_online import TextToVoiceOnline

texts = {
    'en': 'Hello World',
    'es': 'Hola Mundo',
    'fr': 'Bonjour le monde',
    'de': 'Hallo Welt'
}

for lang, text in texts.items():
    converter = TextToVoiceOnline(language=lang)
    converter.save_to_file(text, f'greeting_{lang}.mp3')
```

## Performance Tips

1. **Offline is faster** - Use offline converter for quick conversions
2. **Batch processing** - Process multiple texts in one run
3. **Optimize speed** - Set appropriate speech rate
4. **Memory efficient** - Stream large texts instead of loading entirely

## System Requirements

- Python 3.6+
- 50MB disk space (for pyttsx3)
- Internet connection (for online version only)

## Troubleshooting

Run in verbose mode for debugging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## License

This project is free to use and modify.

## Author

Text to Voice Converter Project

## Support

For issues or questions, refer to:
- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)
- [gTTS Documentation](https://gtts.readthedocs.io/)

---

**Happy Converting!** 
