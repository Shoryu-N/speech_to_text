import requests
import json

#　このクラスはSpeechToTextのAPIを叩いて結果を返す責務を持ちます
class SpeechToTextRequest:
    def __init__(self, audio_file_path):
        self.audio_file_path = audio_file_path

    # TODO: responseが一定秒数返ってこない場合、APIサービスが利用できないと判断し、エラーをraiseするようにする。
    def response(self):
        res = requests.post(self._url(), headers=self._headers(), data=self._audio_file(), auth=("apikey", self._api_key()))
        return res.json()

    # TODO: flac以外の拡張子にも対応する。
    def _headers(self):
        return {
          "Content-Type": "audio/flac",
        }

    def _audio_file(self):
        with open(self.audio_file_path, "rb") as file:
            data = file.read()
        return data  

    # 実際のプロダクトでは下記は.envなどを用いて読み込むべきだが、今回は動作確認のしやすさを優先し、割愛する
    def _api_key(self):
        return "auDZkYK3SaTtzcrCSrBqfmTumKedsHl4saxhOMwl3SCA"

    # 実際のプロダクトでは下記は.envなどを用いて読み込むべきだが、今回は動作確認のしやすさを優先し、割愛する
    def _url(self):
        return "https://api.jp-tok.speech-to-text.watson.cloud.ibm.com/instances/430ceb8a-03a2-486c-9c65-32616fc2213a/v1/recognize?model=ja-JP_BroadbandModel"
