import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

def entity_extractor(text):
    return_dict = {}
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                entity_text = ' '.join(c[0] for c in chunk)
                if chunk.label() in return_dict:
                    if entity_text not in return_dict[chunk.label()]:
                        return_dict[chunk.label()].append(entity_text)
                    
                if chunk.label() not in return_dict:
                    return_dict[chunk.label()] = []
                    return_dict[chunk.label()].append(entity_text)
                    
    return return_dict
if __name__ == "__main__":
    my_sent = "New Delhi, Oct 9: The Supreme Court on Tuesday ruled out an urgent hearing of a plea seeking a review of its verdict allowing women into Kerala's Sabarimala temple. Also Read | Despite review petition, Kerala government to implement Sabarimala verdict The review petition comes in the wake of the Kerala government refusing to interfere and file an appeal in the Supreme Court."
    entity_dict = entity_extractor(my_sent)
    print(entity_dict)