# IBM Cloudからのresponseの形式が変わる可能性を考えて、形式を知る責務はこのクラスのみに持たせる。
class TranscriptExtractor:
    def __init__(self, response_json):
        self.response_json = response_json
    
    def call(self):
        return self._transcript()

    def _transcript(self):
        return self.response_json["results"][0]["alternatives"][0]["transcript"]
