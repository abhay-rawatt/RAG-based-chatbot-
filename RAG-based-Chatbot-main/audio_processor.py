import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import numpy as np
import threading
import queue
import time
from typing import Optional, Callable
import os

class AudioProcessor:
    def __init__(self):
        """Initialize audio processor with speech recognition and text-to-speech"""
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.audio_queue = queue.Queue()
        self.is_listening = False
        self.is_speaking = False
        
        # Configure text-to-speech engine
        self._configure_tts()
        
    def _configure_tts(self):
        """Configure text-to-speech settings"""
        try:
            # Get available voices
            voices = self.engine.getProperty('voices')
            
            # Set voice (use first available voice)
            if voices:
                self.engine.setProperty('voice', voices[0].id)
            
            # Set speech rate (words per minute)
            self.engine.setProperty('rate', 150)
            
            # Set volume (0.0 to 1.0)
            self.engine.setProperty('volume', 0.9)
            
            print("✅ Audio processor configured successfully")
            
        except Exception as e:
            print(f"❌ Failed to configure audio processor: {e}")
    
    def speech_to_text(self, timeout: int = 5, phrase_time_limit: int = 10) -> Optional[str]:
        """
        Convert speech to text using microphone input
        
        Args:
            timeout: Timeout for listening (seconds)
            phrase_time_limit: Maximum time for a single phrase (seconds)
            
        Returns:
            Transcribed text or None if failed
        """
        try:
            with sr.Microphone() as source:
                print("🎤 Listening... (speak now)")
                
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Listen for audio input
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                
                print("🔄 Processing speech...")
                
                # Convert speech to text
                text = self.recognizer.recognize_google(audio)
                print(f"✅ Transcribed: {text}")
                return text
                
        except sr.WaitTimeoutError:
            print("⏰ No speech detected within timeout")
            return None
        except sr.UnknownValueError:
            print("❓ Could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"❌ Speech recognition service error: {e}")
            return None
        except Exception as e:
            print(f"❌ Speech recognition error: {e}")
            return None
    
    def text_to_speech(self, text: str, block: bool = True):
        """
        Convert text to speech and play it
        
        Args:
            text: Text to convert to speech
            block: Whether to block until speech is complete
        """
        try:
            if not text.strip():
                return
            
            print(f"🔊 Speaking: {text[:50]}...")
            
            if block:
                self.engine.say(text)
                self.engine.runAndWait()
            else:
                # Run in separate thread to avoid blocking
                def speak():
                    self.is_speaking = True
                    self.engine.say(text)
                    self.engine.runAndWait()
                    self.is_speaking = False
                
                thread = threading.Thread(target=speak)
                thread.daemon = True
                thread.start()
                
        except Exception as e:
            print(f"❌ Text-to-speech error: {e}")
    
    def start_continuous_listening(self, callback: Callable[[str], None], 
                                 stop_event: threading.Event = None):
        """
        Start continuous listening for speech input
        
        Args:
            callback: Function to call with transcribed text
            stop_event: Event to signal stopping
        """
        if stop_event is None:
            stop_event = threading.Event()
        
        self.is_listening = True
        
        def listen_loop():
            while not stop_event.is_set() and self.is_listening:
                try:
                    text = self.speech_to_text(timeout=3, phrase_time_limit=5)
                    if text:
                        callback(text)
                except Exception as e:
                    print(f"❌ Continuous listening error: {e}")
                    time.sleep(0.1)
        
        thread = threading.Thread(target=listen_loop)
        thread.daemon = True
        thread.start()
        
        return stop_event
    
    def stop_continuous_listening(self):
        """Stop continuous listening"""
        self.is_listening = False
    
    def is_speaking_now(self) -> bool:
        """Check if currently speaking"""
        return self.is_speaking
    
    def is_listening_now(self) -> bool:
        """Check if currently listening"""
        return self.is_listening
    
    def change_voice(self, voice_id: str):
        """Change the voice for text-to-speech"""
        try:
            voices = self.engine.getProperty('voices')
            for voice in voices:
                if voice_id in voice.id:
                    self.engine.setProperty('voice', voice.id)
                    print(f"✅ Voice changed to: {voice.name}")
                    return
            print(f"❌ Voice {voice_id} not found")
        except Exception as e:
            print(f"❌ Failed to change voice: {e}")
    
    def change_speech_rate(self, rate: int):
        """Change speech rate (words per minute)"""
        try:
            self.engine.setProperty('rate', rate)
            print(f"✅ Speech rate changed to: {rate} WPM")
        except Exception as e:
            print(f"❌ Failed to change speech rate: {e}")
    
    def change_volume(self, volume: float):
        """Change volume (0.0 to 1.0)"""
        try:
            volume = max(0.0, min(1.0, volume))
            self.engine.setProperty('volume', volume)
            print(f"✅ Volume changed to: {volume}")
        except Exception as e:
            print(f"❌ Failed to change volume: {e}")

# Test function
def test_audio_processor():
    """Test the audio processor"""
    try:
        processor = AudioProcessor()
        
        print("\n🧪 Testing Audio Processor:")
        print("=" * 40)
        
        # Test text-to-speech
        print("\n🔊 Testing text-to-speech...")
        processor.text_to_speech("Hello! This is a test of the audio processor.")
        
        # Test speech-to-text
        print("\n🎤 Testing speech-to-text...")
        print("Please speak something when prompted...")
        text = processor.speech_to_text(timeout=10)
        
        if text:
            print(f"✅ Successfully transcribed: {text}")
        else:
            print("❌ Speech recognition failed")
            
    except Exception as e:
        print(f"❌ Audio processor test failed: {e}")

if __name__ == "__main__":
    test_audio_processor() 