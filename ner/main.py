import sys
import argparse

from taggers import stub
#TODO from taggers import corenlp
#TODO from taggers import neuroner
#TODO from taggers import spacy

def make_tagger(name):
    if name == 'stub':
        return stub.StubNer()
    #elif name == 'corenlp':
    #    #TODO
    #elif name == 'neuroner':
    #    #TODO
    #elif name == 'spacy':
    #    #TODO
    else:
        print('ERROR: Unrecognized tagger:', name)
        sys.exit(1)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Find Named Entities in a sentence')
    argparser.add_argument('sentence', metavar='SENTENCE', type=str)
    argparser.add_argument('-t, --tagger', dest='tagger', type=str, default='stub')

    args = argparser.parse_args()

    ner = make_tagger(args.tagger)
    result = ner.predict(args.sentence)

    for w, t in result:
        print('{}\t{}'.format(w, t))
