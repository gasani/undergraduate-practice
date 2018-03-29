class StubNer:
    def predict(self, sentence):
        result = []
        for w in sentence.split(' '):
            result.append((w, 'O'))
        return result
