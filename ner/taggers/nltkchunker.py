from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree

# Conversion from the nltk tags
LABEL_MAPPING = {"ORGANIZATION" : "ORG", "PERSON" : "PER", "LOCATION" : "LOC",
 "DATE" : "MISC", "TIME" : "MISC", "MONEY" : "MISC", "PERCENT" : "MISC",
 "FACILITY" : "MISC", "GPE" : "LOC"}

class ChunkerNer:
    # Extract NER tags from an nltk.tree.Tree
    def parseTree(self, tree):
        tags = []
        for subtree in tree:
            if type(subtree) == Tree:
                if subtree.label() in LABEL_MAPPING:
                    for leaf in subtree.leaves():
                        tags.append(LABEL_MAPPING[subtree.label()])
                else:
                    self.parseTree(subtree)
            else:
                if subtree[1] in LABEL_MAPPING:
                    tags.append(LABEL_MAPPING[subtree[1]])
                else:
                    tags.append("O")
        return tags

    # Perform NER
    def predict(self, sentence):
        tree = ne_chunk(pos_tag(word_tokenize(sentence)))
        # Traverse the tree
        tags = self.parseTree(tree)
        result = []
        for word, tag in zip(sentence.split(' '), tags):
            result.append((word, tag))
        return result
