import pyttsx3
import threading
import time
from typing import Optional, Callable
import os

class SimpleAudioProcessor:
    def __init__(self):
        """Initialize simplified audio processor with text-to-speech only"""
        self.engine = pyttsx3.init()
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
            
            print("✅ Simple audio processor configured successfully")
            
        except Exception as e:
            print(f"❌ Failed to configure audio processor: {e}")
    
    def speech_to_text(self, timeout: int = 5, phrase_time_limit: int = 10) -> Optional[str]:
        """
        Placeholder for speech-to-text (requires PyAudio)
        Returns None to indicate speech recognition is not available
        """
        print("⚠️ Speech-to-text not available. Install PyAudio for full audio support.")
        print("💡 You can still use text input and get audio responses.")
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
        Placeholder for continuous listening (requires PyAudio)
        """
        print("⚠️ Continuous listening not available. Install PyAudio for full audio support.")
        return threading.Event()
    
    def stop_continuous_listening(self):
        """Stop continuous listening"""
        pass
    
    def is_speaking_now(self) -> bool:
        """Check if currently speaking"""
        return self.is_speaking
    
    def is_listening_now(self) -> bool:
        """Check if currently listening (always False for simple version)"""
        return False
    
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
def test_simple_audio_processor():
    """Test the simple audio processor"""
    try:
        processor = SimpleAudioProcessor()
        
        print("\n🧪 Testing Simple Audio Processor:")
        print("=" * 40)
        
        # Test text-to-speech
        print("\n🔊 Testing text-to-speech...")
        processor.text_to_speech("Hello! This is a test of the simple audio processor.")
        
        # Test speech-to-text (will show warning)
        print("\n🎤 Testing speech-to-text...")
        text = processor.speech_to_text(timeout=10)
        
        if text:
            print(f"✅ Successfully transcribed: {text}")
        else:
            print("ℹ️ Speech-to-text not available (as expected)")
            
    except Exception as e:
        print(f"❌ Simple audio processor test failed: {e}")

if __name__ == "__main__":
    test_simple_audio_processor() 