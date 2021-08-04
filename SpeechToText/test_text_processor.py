import sys
import unittest
from io import StringIO
from text_processor import TextProcessor

# テストはパブリックとなっているメソッドのみテストしています。
class TextProcessorTest(unittest.TestCase):
    def setUp(self):
        # ""や" "はなにも表示されないのが予期している挙動
        search_words = ["音声", "a", "", " "]
        text = "音声認識は、近年流行しているアプリケーションの一つだ。今回は、音声を入力し、それをテキストに変換する。"
        self.text_processor = TextProcessor(search_words=search_words, text=text)
        self.org_stdout, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdout = self.org_stdout

    def test_result(self):
        actual_result = self.text_processor.result()
        self.assertIn("「音声」の検索結果", sys.stdout.getvalue())
        self.assertIn("出現位置", sys.stdout.getvalue())
        self.assertIn("前後5文字も含めた文字列", sys.stdout.getvalue())
        self.assertIn("音声認識は、近", sys.stdout.getvalue())
        self.assertIn("(0, 2)", sys.stdout.getvalue())
        self.assertIn("今回は、音声を入力し、", sys.stdout.getvalue())
        self.assertIn("(31, 33)", sys.stdout.getvalue())
        self.assertIn("「a」の検索結果", sys.stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
        