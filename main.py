import nltk
from nltk import RegexpParser
from nltk import pos_tag
from nltk import word_tokenize

text = "The train was late"
list_of_words = word_tokenize(text)

pos_tagged = pos_tag(list_of_words)
print (pos_tagged)

chunk_extract = '''Chunk: {<DT>*<NN>*<NNP>*}'''
chunk_parser = nltk.chunk.RegexpParser(chunk_extract)
chunked_sentence  = chunk_parser.parse(pos_tagged)
chunked_sentence.draw()
