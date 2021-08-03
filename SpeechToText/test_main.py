import unittest
from unittest.mock import MagicMock, patch
from speech_to_text import SpeechToText
from main import print_processed_speech_to_text, NotFlacAudioError

# テストはパブリックとなっているメソッドのみテストしています。
class SpeechToTextTest(unittest.TestCase):
    # 以下クラスをmockして必要なメソッドが呼ばれたかどうかをテストしています。
    def test_call_speech_to_text(self):
        speech_to_text = SpeechToText(audio_file_path="audio/audio-sample.flac", search_words=["認識", "a"])
        speech_to_text.call = MagicMock()

        print_processed_speech_to_text()
        assert speech_to_text.call.assert_called_once

    @patch("builtins.input", lambda:"a.wav")
    def test_not_flac_file(self):
        with self.assertRaises(NotFlacAudioError):
            print_processed_speech_to_text()

    @patch("builtins.input", lambda:"a.flac")
    def test_not_exist_audio_file(self):
        with self.assertRaises(FileNotFoundError):
            print_processed_speech_to_text()              
    
if __name__ == "__main__":
    unittest.main()
        