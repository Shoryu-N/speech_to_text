from speech_to_text import SpeechToText

class NotFlacAudioError(Exception):
    pass

# TODO: 検索ワードによって、何語かを判別し、叩くAPIをハンドリングする。
# TODO: 現段階では結果をprintしているが、これをクライアントサイドにレスポンスとして返すようにする。
def print_processed_speech_to_text():
    print("audio_fileの相対パスを入力してください")
    audio_file_path = input()
    _is_flac(audio_file_path)
    print("検索したい単語を半角スペース区切りで入力してください")
    search_words = list(input().split())

    return SpeechToText(audio_file_path=audio_file_path, search_words=search_words).call()

def _is_flac(file_path):
    if file_path[-5:] != ".flac":
        raise NotFlacAudioError("flac形式のファイルではありません。")

if __name__ == '__main__':
    print_processed_speech_to_text()