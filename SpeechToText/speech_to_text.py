from speech_to_text_request import SpeechToTextRequest
from text_processer import TextProcessor
from transcript_extractor import TranscriptExtractor

class SpeechToText:
    def __init__(self, *, audio_file_path ,search_words):
        self.audio_file_path = audio_file_path
        self.search_words = search_words

    def call(self):
        self._processed_text()

    def _processed_text(self):
        return TextProcessor(search_words=self.search_words, text=self._transcript()).result()
    
    def _transcript(self):
        return TranscriptExtractor(self._response()).call()

    def _response(self):
        return SpeechToTextRequest(self.audio_file_path).response()

        
