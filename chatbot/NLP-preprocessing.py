#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:59:30 2017

@author: jwcunha
"""

import PyPDF2 
import textract
import nltk
import re

# http://www.nltk.org/nltk_data/
#nltk.download('punkt')
nltk.download('rslp')
nltk.download('mac_morpho')
nltk.download('floresta')
nltk.data.load('tokenizers/punkt/portuguese.pickle')


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import floresta
from nltk.stem.porter import PorterStemmer #root word



#write a for-loop to open many files -- leave a comment if you'd #like to learn how
filename = 'resources/LDT.pdf' 

#open allows you to read the file
pdfFileObj = open(filename,'rb')

#The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfReader.numPages
count = 0
text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
else:
   text = textract.process(fileurl, method='tesseract', language='eng')

# Cleansing data
def cleansing(r):        
    #review = re.sub('[^a-zA-Z]', ' ', r)
    review = review.lower()
    review = review.split()
    ps = nltk.stem.RSLPStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('portuguese'))]    
    review = ' '.join(review)
    return review

reviewed = cleansing(text)

# Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
# Now, we will clean our text variable, and return it as a list of keywords.
#The word_tokenize() function will break our text phrases into #individual words
tokens = word_tokenize(text)
#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',']
#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
stop_words = stopwords.words('english')
#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and  not word in string.punctuation]