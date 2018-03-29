import spacy

class SpacyNer:
    def __init__(self):
        self.nlp = spacy.load('en')

    def predict(self, sentence):
        result = []
        doc = self.nlp(sentence, disable=['tagger', 'parser'])

        for tok in doc:
            ent_type = tok.ent_type_
            if not ent_type:
                ent_type = 'O'
            else:
                ent_type = self._en_ent_to_ent(ent_type)
            result.append((tok.text, ent_type))

        return result

    @staticmethod
    def _en_ent_to_ent(en_ent):
        if en_ent == 'PERSON':
            return 'PER'
        elif en_ent == 'LOC' or en_ent == 'GPE':
            return 'LOC'
        elif en_ent == 'ORG':
            return 'ORG'
        else:
            return 'MISC'
