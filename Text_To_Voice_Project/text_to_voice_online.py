"""
Text to Voice Converter - Online Version using Google Text-to-Speech (gTTS)
Requires internet connection
"""

from gtts import gTTS
import os
import platform
import shutil
from pathlib import Path

class TextToVoiceOnline:
    def __init__(self, language='en'):
        """Initialize with language code (default: English)"""
        self.language = language
        self.supported_languages = {
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'pt': 'Portuguese',
            'ru': 'Russian',
            'ja': 'Japanese',
            'zh': 'Chinese',
            'hi': 'Hindi',
            'bn': 'Bengali',
        }
    
    def set_language(self, language_code):
        """Set the language for speech"""
        if language_code in self.supported_languages:
            self.language = language_code
            print(f"Language set to: {self.supported_languages[language_code]}")
        else:
            print(f"Language '{language_code}' not supported")
    
    def get_supported_languages(self):
        """Display supported languages"""
        print("Supported languages:")
        for code, name in self.supported_languages.items():
            print(f"  {code}: {name}")
    
    def speak(self, text, speed=1.0):
        """Speak the text (plays audio)"""
        try:
            print(f"Generating speech for: {text[:50]}...")
            tts = gTTS(text=text, lang=self.language, slow=(speed < 1.0))
            
            # Save temporarily and play
            temp_file = 'temp_speech.mp3'
            tts.save(temp_file)
            
            # Play based on OS
            if platform.system() == 'Darwin':  # macOS
                os.system(f'afplay {temp_file}')
            elif platform.system() == 'Windows':
                os.system(f'start {temp_file}')
            elif platform.system() == 'Linux':
                os.system(f'mpg321 {temp_file}')
            
            os.remove(temp_file)
            print("✓ Speech played successfully!")
            
        except Exception as e:
            print(f"Error: {e}")
    
    def save_to_file(self, text, filename='output.mp3'):
        """Save speech to an MP3 file"""
        try:
            print(f"Generating speech...")
            tts = gTTS(text=text, lang=self.language)
            tts.save(filename)
            print(f"✓ Audio saved to: {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")
    
    def process_text_file(self, input_file, output_file='output.mp3'):
        """Convert entire text file to speech"""
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            print(f"Processing file: {input_file}")
            self.save_to_file(text, output_file)
            
        except FileNotFoundError:
            print(f"File not found: {input_file}")
        except Exception as e:
            print(f"Error: {e}")
    
    def get_file_info(self, filename):
        """Get information about the created MP3 file"""
        try:
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                file_size_mb = file_size / (1024 * 1024)
                abs_path = os.path.abspath(filename)
                
                print(f"\n{'='*50}")
                print(f" File Information:")
                print(f"{'='*50}")
                print(f"Filename: {filename}")
                print(f"Full Path: {abs_path}")
                print(f"File Size: {file_size_mb:.2f} MB ({file_size} bytes)")
                print(f"{'='*50}\n")
                
                return True
            else:
                print(f"File not found: {filename}")
                return False
        except Exception as e:
            print(f"Error getting file info: {e}")
            return False
    
    def open_file(self, filename):
        """Open the MP3 file with default media player"""
        try:
            if not os.path.exists(filename):
                print(f"File not found: {filename}")
                return False
            
            print(f"Opening: {filename}...")
            abs_path = os.path.abspath(filename)
            
            if platform.system() == 'Darwin':  # macOS
                os.system(f'open "{abs_path}"')
            elif platform.system() == 'Windows':
                os.system(f'start "" "{abs_path}"')
            elif platform.system() == 'Linux':
                os.system(f'xdg-open "{abs_path}"')
            
            print("✓ File opened with default player!")
            return True
        except Exception as e:
            print(f"Error opening file: {e}")
            return False
    
    def download_file(self, source_file, download_folder='Downloads'):
        """Download/copy the MP3 file to a destination folder"""
        try:
            if not os.path.exists(source_file):
                print(f"Source file not found: {source_file}")
                return False
            
            # Create download folder if it doesn't exist
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)
                print(f"Created folder: {download_folder}")
            
            filename = os.path.basename(source_file)
            destination = os.path.join(download_folder, filename)
            
            # If file already exists, add a number to it
            if os.path.exists(destination):
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(os.path.join(download_folder, f"{name}_{counter}{ext}")):
                    counter += 1
                destination = os.path.join(download_folder, f"{name}_{counter}{ext}")
            
            shutil.copy2(source_file, destination)
            abs_dest = os.path.abspath(destination)
            
            print(f"\n{'='*50}")
            print(f"✓ Download Complete!")
            print(f"{'='*50}")
            print(f"Saved to: {abs_dest}")
            print(f"{'='*50}\n")
            
            return True
        except Exception as e:
            print(f"Error downloading file: {e}")
            return False
    
    def list_audio_files(self, folder='.'):
        """List all MP3 files in a folder"""
        try:
            mp3_files = list(Path(folder).glob('*.mp3'))
            
            if not mp3_files:
                print(f"No MP3 files found in {folder}")
                return []
            
            print(f"\n{'='*50}")
            print(f" MP3 Files in: {os.path.abspath(folder)}")
            print(f"{'='*50}")
            
            files_info = []
            for i, mp3_file in enumerate(mp3_files, 1):
                size_mb = mp3_file.stat().st_size / (1024 * 1024)
                print(f"{i}. {mp3_file.name} ({size_mb:.2f} MB)")
                files_info.append(str(mp3_file))
            
            print(f"{'='*50}\n")
            return files_info
        except Exception as e:
            print(f"Error listing files: {e}")
            return []
    
    def delete_file(self, filename):
        """Delete an MP3 file"""
        try:
            if not os.path.exists(filename):
                print(f"File not found: {filename}")
                return False
            
            os.remove(filename)
            print(f"✓ File deleted: {filename}")
            return True
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False


def main():
    print("=== Text to Voice Converter (Online - gTTS) ===\n")
    
    # Create converter instance
    converter = TextToVoiceOnline()
    
    while True:
        print("--- Main Menu ---")
        print("1. Convert text to speech")
        print("2. Convert from file")
        print("3. Change language")
        print("4. Show supported languages")
        print("5. List MP3 files")
        print("6. Open MP3 file")
        print("7. Download MP3 file")
        print("8. Delete MP3 file")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            text = input("Enter the text to convert: ")
            filename = input("Enter filename to save (default: output.mp3): ").strip()
            if not filename:
                filename = 'output.mp3'
            
            converter.save_to_file(text, filename)
            converter.get_file_info(filename)
            
            # Ask for download option
            download_choice = input("Do you want to download this file? (y/n): ").strip().lower()
            if download_choice == 'y':
                download_folder = input("Enter download folder (default: Downloads): ").strip()
                if not download_folder:
                    download_folder = 'Downloads'
                converter.download_file(filename, download_folder)
            
            # Ask to open file
            open_choice = input("Do you want to open this file? (y/n): ").strip().lower()
            if open_choice == 'y':
                converter.open_file(filename)
                
        elif choice == '2':
            input_file = input("Enter input text file path: ").strip()
            output_file = input("Enter output filename (default: output.mp3): ").strip()
            if not output_file:
                output_file = 'output.mp3'
            
            converter.process_text_file(input_file, output_file)
            converter.get_file_info(output_file)
            
            # Ask for download option
            download_choice = input("Do you want to download this file? (y/n): ").strip().lower()
            if download_choice == 'y':
                download_folder = input("Enter download folder (default: Downloads): ").strip()
                if not download_folder:
                    download_folder = 'Downloads'
                converter.download_file(output_file, download_folder)
            
            # Ask to open file
            open_choice = input("Do you want to open this file? (y/n): ").strip().lower()
            if open_choice == 'y':
                converter.open_file(output_file)
                
        elif choice == '3':
            converter.get_supported_languages()
            lang_code = input("Enter language code: ").strip()
            converter.set_language(lang_code)
            
        elif choice == '4':
            converter.get_supported_languages()
            
        elif choice == '5':
            folder = input("Enter folder path (default: current folder): ").strip()
            if not folder:
                folder = '.'
            converter.list_audio_files(folder)
            
        elif choice == '6':
            filename = input("Enter MP3 filename to open: ").strip()
            converter.open_file(filename)
            
        elif choice == '7':
            filename = input("Enter MP3 filename to download: ").strip()
            download_folder = input("Enter download folder (default: Downloads): ").strip()
            if not download_folder:
                download_folder = 'Downloads'
            converter.download_file(filename, download_folder)
            
        elif choice == '8':
            filename = input("Enter MP3 filename to delete: ").strip()
            confirm = input(f"Are you sure you want to delete {filename}? (y/n): ").strip().lower()
            if confirm == 'y':
                converter.delete_file(filename)
            else:
                print("Deletion cancelled.")
        
        elif choice == '9':
            print("Thank you for using Text to Voice Converter!")
            break
        
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
