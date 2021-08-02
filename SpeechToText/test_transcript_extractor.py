import json
import unittest
from transcript_extractor import TranscriptExtractor

# テストはパブリックとなっているメソッドのみテストしている。
class TranscriptExtractorTest(unittest.TestCase):
    def setUp(self):
        json_file = open("sample_for_transcript_extractor_test.json", "r")
        json_dict_file = json.load(json_file)
        self.transcript_extractor = TranscriptExtractor(json_dict_file)

    def test_response(self):
        actual_result = self.transcript_extractor.call()
        expected_result = "これはテスト用のjsonファイルです"

        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()
        