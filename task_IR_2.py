from nltk.tokenize import word_tokenize
x=" NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all,NLTK is a free, open source, community-driven project"
print(word_tokenize(x))


print("-------------------------------------------------------")
print("-------------------------------------------------------")

from nltk.tokenize import sent_tokenize
y=" NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all,NLTK is a free, open source, community-driven project"
print(sent_tokenize(y))