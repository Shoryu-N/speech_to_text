import unittest
from unittest.mock import MagicMock
from speech_to_text import SpeechToText
from speech_to_text_request import SpeechToTextRequest
from text_processor import TextProcessor
from transcript_extractor import TranscriptExtractor

# テストはパブリックとなっているメソッドのみテストしています。
class SpeechToTextTest(unittest.TestCase):
    def setUp(self):
        self.speech_to_text = SpeechToText(audio_file_path="audio/audio-sample.flac", search_words=["認識", "a"])

    # 以下クラスをmockして必要なメソッドが呼ばれたかどうかをテストしています。
    def test_call_speech_to_text_request(self):
        speech_to_text_request = SpeechToTextRequest("audio/audio-sample.flac")
        speech_to_text_request.response = MagicMock()

        self.speech_to_text.call()
        assert speech_to_text_request.response.assert_called_once

    # 以下クラスをmockして必要なメソッドが呼ばれたかどうかをテストしています。
    def test_call_text_processor(self):
        speech_to_text_processor = TextProcessor(search_words=["test", "aaa"] ,text="aaa")
        speech_to_text_processor.call = MagicMock()

        self.speech_to_text.call()
        assert speech_to_text_processor.call.assert_called_once

    # 以下クラスをmockして必要なメソッドが呼ばれたかどうかをテストしています。
    def test_call_transcript_extractor(self):
        transcript_extractor = TranscriptExtractor({"test": "1"})
        transcript_extractor.call = MagicMock()

        self.speech_to_text.call()
        assert transcript_extractor.call.assert_called_once        
        
if __name__ == "__main__":
    unittest.main()
        