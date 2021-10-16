

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


paragraph = """" You can't connect the dots looking forward; you can only connect them looking backward. 
So you have to trust that the dots will somehow connect in your future. 
You have to trust in something — your gut, destiny, life, karma, whatever. 
This approach has never let me down, and it has made all the difference in my life.”

“ When I was 17, I read a quote that went something like: 
"If you live each day as if it was your last, someday you'll most certainly be right.
" It made an impression on me, and since then, for the past 33 years, 
I have looked in the mirror every morning and asked myself: "If today were the last day of my life, 
would I want to do what I am about to do today?" 
And whenever the answer has been "No" for too many days in a row, I know I need to change something."""


sentences = nltk.sent_tokenize(paragraph)

stemmer = PorterStemmer()

# Stemming

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = ' '.join(words)



