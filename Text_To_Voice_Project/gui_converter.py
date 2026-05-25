"""
Text to Voice Converter - GUI Version using Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pyttsx3
import threading
import os
import shutil
from pathlib import Path

class TextToVoiceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Voice Converter")
        self.root.geometry("700x650")
        self.root.resizable(True, True)
        
        # Initialize engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
        self.last_saved_file = None
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the GUI components"""
        # Title
        title_label = tk.Label(self.root, text="Text to Voice Converter", 
                               font=("Arial", 16, "bold"), fg="blue")
        title_label.pack(pady=10)
        
        # Text Input Frame
        input_frame = ttk.LabelFrame(self.root, text="Text Input", padding=10)
        input_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.text_widget = tk.Text(input_frame, height=10, width=70, wrap="word")
        self.text_widget.pack(side="left", fill="both", expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(input_frame, orient="vertical", command=self.text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_widget['yscrollcommand'] = scrollbar.set
        
        # Controls Frame
        controls_frame = ttk.Frame(self.root)
        controls_frame.pack(padx=10, pady=10, fill="x")
        
        # Speed Control
        ttk.Label(controls_frame, text="Speed:").pack(side="left", padx=5)
        self.speed_var = tk.IntVar(value=150)
        speed_scale = ttk.Scale(controls_frame, from_=50, to=300, orient="horizontal", 
                                variable=self.speed_var, command=self.update_speed)
        speed_scale.pack(side="left", padx=5, fill="x", expand=True)
        
        # Volume Control
        ttk.Label(controls_frame, text="Volume:").pack(side="left", padx=5)
        self.volume_var = tk.DoubleVar(value=0.9)
        volume_scale = ttk.Scale(controls_frame, from_=0.0, to=1.0, orient="horizontal",
                                 variable=self.volume_var, command=self.update_volume)
        volume_scale.pack(side="left", padx=5, fill="x", expand=True)
        
        # Voice Selection Frame
        voice_frame = ttk.Frame(self.root)
        voice_frame.pack(padx=10, pady=5, fill="x")
        
        ttk.Label(voice_frame, text="Voice:").pack(side="left", padx=5)
        voices = self.engine.getProperty('voices')
        self.voice_names = [voice.name for voice in voices]
        self.voice_var = tk.StringVar(value=self.voice_names[0] if self.voice_names else "")
        
        voice_combo = ttk.Combobox(voice_frame, textvariable=self.voice_var, 
                                   values=self.voice_names, state="readonly", width=30)
        voice_combo.pack(side="left", padx=5)
        
        # Buttons Frame
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(padx=10, pady=10, fill="x")
        
        speak_btn = ttk.Button(buttons_frame, text="🔊 Speak", command=self.speak_text)
        speak_btn.pack(side="left", padx=5)
        
        save_btn = ttk.Button(buttons_frame, text="💾 Save to File", command=self.save_to_file)
        save_btn.pack(side="left", padx=5)
        
        stop_btn = ttk.Button(buttons_frame, text="⏹ Stop", command=self.stop_speech)
        stop_btn.pack(side="left", padx=5)
        
        clear_btn = ttk.Button(buttons_frame, text="🗑 Clear", command=self.clear_text)
        clear_btn.pack(side="left", padx=5)
        
        # Downloads Frame
        download_frame = ttk.LabelFrame(self.root, text="Download & Manage", padding=10)
        download_frame.pack(padx=10, pady=10, fill="x")
        
        # Download buttons
        download_btn = ttk.Button(download_frame, text="⬇️ Download Last File", 
                                  command=self.download_last_file)
        download_btn.pack(side="left", padx=5)
        
        open_btn = ttk.Button(download_frame, text="📂 Open Last File", 
                              command=self.open_last_file)
        open_btn.pack(side="left", padx=5)
        
        browse_btn = ttk.Button(download_frame, text="📁 Browse Files", 
                                command=self.browse_files)
        browse_btn.pack(side="left", padx=5)
        
        # Status Bar
        self.status_label = ttk.Label(self.root, text="Ready", relief="sunken")
        self.status_label.pack(side="bottom", fill="x", padx=10, pady=5)
    
    def update_speed(self, value):
        """Update speech speed"""
        speed = int(float(value))
        self.engine.setProperty('rate', speed)
    
    def update_volume(self, value):
        """Update volume"""
        volume = float(value)
        self.engine.setProperty('volume', volume)
    
    def update_status(self, message):
        """Update status bar"""
        self.status_label.config(text=message)
        self.root.update()
    
    def speak_text(self):
        """Speak the text in a separate thread"""
        text = self.text_widget.get("1.0", "end-1c").strip()
        
        if not text:
            messagebox.showwarning("Warning", "Please enter some text!")
            return
        
        # Update voice
        voices = self.engine.getProperty('voices')
        selected_voice = self.voice_var.get()
        for voice in voices:
            if voice.name == selected_voice:
                self.engine.setProperty('voice', voice.id)
                break
        
        # Speak in separate thread to keep GUI responsive
        thread = threading.Thread(target=self._speak_thread, args=(text,))
        thread.daemon = True
        thread.start()
    
    def _speak_thread(self, text):
        """Speak text in background thread"""
        self.update_status("Speaking...")
        self.engine.say(text)
        self.engine.runAndWait()
        self.update_status("Ready")
    
    def save_to_file(self):
        """Save speech to file"""
        text = self.text_widget.get("1.0", "end-1c").strip()
        
        if not text:
            messagebox.showwarning("Warning", "Please enter some text!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")]
        )
        
        if filename:
            # Update voice
            voices = self.engine.getProperty('voices')
            selected_voice = self.voice_var.get()
            for voice in voices:
                if voice.name == selected_voice:
                    self.engine.setProperty('voice', voice.id)
                    break
            
            # Save in thread
            thread = threading.Thread(target=self._save_thread, args=(text, filename))
            thread.daemon = True
            thread.start()
    
    def _save_thread(self, text, filename):
        """Save text to file in background thread"""
        self.update_status(f"Saving to {filename}...")
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
        self.last_saved_file = filename
        self.update_status(f"Saved to {filename}")
        messagebox.showinfo("Success", f"File saved successfully!\n{filename}")
    
    def stop_speech(self):
        """Stop current speech"""
        self.engine.stop()
        self.update_status("Stopped")
    
    def clear_text(self):
        """Clear text widget"""
        self.text_widget.delete("1.0", "end")
        self.update_status("Ready")
    
    def download_last_file(self):
        """Download the last saved file"""
        if not self.last_saved_file:
            messagebox.showwarning("Warning", "No file has been saved yet!")
            return
        
        if not os.path.exists(self.last_saved_file):
            messagebox.showerror("Error", f"File not found: {self.last_saved_file}")
            return
        
        download_folder = filedialog.askdirectory(title="Select download folder")
        if not download_folder:
            return
        
        try:
            filename = os.path.basename(self.last_saved_file)
            destination = os.path.join(download_folder, filename)
            
            # If file already exists, add a number to it
            if os.path.exists(destination):
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(os.path.join(download_folder, f"{name}_{counter}{ext}")):
                    counter += 1
                destination = os.path.join(download_folder, f"{name}_{counter}{ext}")
            
            shutil.copy2(self.last_saved_file, destination)
            self.update_status(f"Downloaded to: {destination}")
            messagebox.showinfo("Success", f"File downloaded successfully!\n{destination}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download file: {e}")
    
    def open_last_file(self):
        """Open the last saved file with default player"""
        if not self.last_saved_file:
            messagebox.showwarning("Warning", "No file has been saved yet!")
            return
        
        if not os.path.exists(self.last_saved_file):
            messagebox.showerror("Error", f"File not found: {self.last_saved_file}")
            return
        
        try:
            abs_path = os.path.abspath(self.last_saved_file)
            import platform
            
            if platform.system() == 'Darwin':  # macOS
                os.system(f'open "{abs_path}"')
            elif platform.system() == 'Windows':
                os.system(f'start "" "{abs_path}"')
            elif platform.system() == 'Linux':
                os.system(f'xdg-open "{abs_path}"')
            
            self.update_status(f"Opening: {self.last_saved_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")
    
    def browse_files(self):
        """Browse and manage saved MP3 files"""
        folder = filedialog.askdirectory(title="Select folder to browse")
        if not folder:
            return
        
        mp3_files = list(Path(folder).glob('*.mp3'))
        
        if not mp3_files:
            messagebox.showinfo("Info", f"No MP3 files found in:\n{folder}")
            return
        
        # Create a new window to show files
        file_window = tk.Toplevel(self.root)
        file_window.title("MP3 Files")
        file_window.geometry("600x400")
        
        # Frame for listbox
        list_frame = ttk.Frame(file_window)
        list_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Listbox with scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        
        listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
        listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=listbox.yview)
        
        # Add files to listbox
        for mp3_file in mp3_files:
            size_mb = mp3_file.stat().st_size / (1024 * 1024)
            listbox.insert(tk.END, f"{mp3_file.name} ({size_mb:.2f} MB)")
        
        # Buttons frame
        btn_frame = ttk.Frame(file_window)
        btn_frame.pack(padx=10, pady=10, fill="x")
        
        def open_selected():
            selection = listbox.curselection()
            if not selection:
                messagebox.showwarning("Warning", "Please select a file!")
                return
            selected_file = str(mp3_files[selection[0]])
            abs_path = os.path.abspath(selected_file)
            
            import platform
            if platform.system() == 'Darwin':
                os.system(f'open "{abs_path}"')
            elif platform.system() == 'Windows':
                os.system(f'start "" "{abs_path}"')
            elif platform.system() == 'Linux':
                os.system(f'xdg-open "{abs_path}"')
        
        def delete_selected():
            selection = listbox.curselection()
            if not selection:
                messagebox.showwarning("Warning", "Please select a file!")
                return
            
            file_to_delete = str(mp3_files[selection[0]])
            confirm = messagebox.askyesno("Confirm", f"Delete {os.path.basename(file_to_delete)}?")
            if confirm:
                os.remove(file_to_delete)
                listbox.delete(selection)
                messagebox.showinfo("Success", "File deleted!")
        
        ttk.Button(btn_frame, text="▶️ Open", command=open_selected).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="⬇️ Download", command=lambda: messagebox.showinfo(
            "Info", f"Select folder in file dialog")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="🗑 Delete", command=delete_selected).pack(side="left", padx=5)


def main():
    root = tk.Tk()
    app = TextToVoiceGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
