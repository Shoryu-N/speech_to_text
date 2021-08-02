import unittest
from speech_to_text_request import SpeechToTextRequest

# テストはパブリックとなっているメソッドのみテストしている。
class SpeechToTextRequestTest(unittest.TestCase):
    def setUp(self):
        test_audio_path = "audio/test-audio.flac"
        self.speech_to_text_request = SpeechToTextRequest(test_audio_path)

    def test_response(self):
        actual_result = self.speech_to_text_request.response()
        expected_result = {'result_index': 0, \
            'results': [{'final': True, 'alternatives': [{'transcript': '日本語 ', 'confidence': 0.65}]}]}

        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()
        