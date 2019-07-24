from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as summarize
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

#import nltk
#nltk.download('punkt')

language= 'english'

url= input("Insert article's url: ")
#url= 'https://medium.com/autonomous-agents/laymans-intro-to-ai-and-neural-networks-ce074457d85a'
sentences_count= input("Insert number of bites-size sentences: ")

if __name__ == '__main__':
    parser= HtmlParser.from_url(url, Tokenizer(language))
    stemmer= Stemmer(language)

    summarized= summarize(stemmer)
    summarized.stop_words= get_stop_words(language)

    #bites= []
    #bites.append(sentence)
    i=1

    for sentence in summarized(parser.document, int(sentences_count) ):
        print(str(i)+'.'+ str(sentence) )
        i+=1

