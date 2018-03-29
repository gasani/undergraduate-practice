import os
from nltk.tag import StanfordNERTagger

class StanfordNer:
    def __init__(self, corenlp_dir=None, model='english.conll.4class.distsim.crf.ser.gz'):
        if corenlp_dir is not None:
            corenlp_dir = os.path.abspath(corenlp_dir)
            os.environ['CLASSPATH'] = corenlp_dir
            os.environ['STANFORD_MODELS'] = os.path.join(corenlp_dir, 'classifiers')

        # Also can look at model: 'english.all.3class.distsim.crf.ser.gz'
        self.st = StanfordNERTagger(model)

    def predict(self, sentence):
        tagged = self.st.tag(sentence.split())
        result = []
        for w, t in tagged:
            result.append((w, t if t == 'MISC' else t[:3]))
        return result
