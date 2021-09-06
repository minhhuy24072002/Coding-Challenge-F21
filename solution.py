from textblob import TextBlob
from textblob import Word
from textblob.np_extractors import ConllExtractor

def recheckSuggestion(suggestion):
    # return true if the suggested word is 100% sure, is different from word on the input, and is not a noun phrase
    return suggestion[0] != w and suggestion[1] == 1 and suggestion[0] != w.pluralize() and suggestion[0] != w.singularize() and w.lower() not in text.noun_phrases

# read input and convert it into a Textblob object
extractor = ConllExtractor()
inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")
text = TextBlob(inputFile.read(), np_extractor=extractor)
inputFile.close()
cnt = 0

# Run for each word in the input and give suggestions for misspelling words
outputFile.write("Suggest corrections:\n")
for w in text.words:
    cnt += 1
    suggestions = w.spellcheck()
    for suggestion in suggestions:
        isSuggested = False
        if (recheckSuggestion(suggestion)):
            #print out suggestion for misspelling word and its destination
            outputFile.write(w + "->" + str(suggestion[0]) + " (Word " + str(cnt) + ")\n")
            isSuggested = True
        if (isSuggested == True):
            outputFile.write("\n")

# print out the polarity as well as subjectivity of input text
outputFile.write("Text polarity:" + str(text.sentiment.polarity) + "\n")
outputFile.write("Text subjectivity:" + str(text.sentiment.subjectivity))
outputFile.close()

