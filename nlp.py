
import nltk 
nltk.download()
data="Computer is an electronic device. It takes input data, processes it andgenerates the output"
from nltk import word_tokenize, sent_tokenize
#step 1: tokenisation
sentences=sent_tokenize(data)
print(sentences)
words=word_tokenize(data)
print(words)
data1
from nltk.corpus import stopwords
stopwords.words('english')
import re
from nltk.corpus import stopwords
data="""Coronavirus disease is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.The best way to prevent and slow down transmission is be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face.
The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, 
so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).At this time, there are no specific vaccines or treatments for COVID-19. However, there are many ongoing clinical trials evaluating potential treatments. WHO will continue to provide updated information as soon as clinical findings become available."""
data = re.sub('[^a-zA-Z]', ' ',data)
data = data.lower()
data = data.split()
data = [word for word in data if not word in set(stopwords.words('english'))]
data = ' '.join(data)
print(data)