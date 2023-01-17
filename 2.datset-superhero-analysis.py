#This library draws the graphs
import matplotlib.pyplot as plt
#To imitate the theme used by ggplot
plt.style.use('ggplot')

#This library generates the networks
import networkx as nx

#This library is used to recognize keywords
import nltk
nltk.download ('punkt')
nltk.download('averaged_perceptron_tagger')

#This library is used to manage the datasets
import pandas as pd

from collections import Counter

import numpy as np

!pip install praw
import praw

superhero = pd.read_csv("marvel_dc.csv")

superheroyearnum = superhero['Year'].value_counts(sort=False)

superheroyearslist = list(superhero['Year'])
superheroyearslist2 = sorted(list(dict.fromkeys(superheroyearslist)))

superhero_zip_iterator = zip(superheroyearslist2, superheroyearnum)
superhero_dictionary = dict(superhero_zip_iterator)

allyears = list(yearrange)

zerolist = []
for element in yearrange:
  zerolist.append(0)

allyears_zip_iterator = zip(allyears, zerolist)
allyears_dictionary = dict(allyears_zip_iterator)

fixed_superhero = allyears_dictionary.copy()
fixed_superhero.update(superhero_dictionary)

print(fixed_superhero)

disney = pd.read_csv("disney2.csv")

disneyyearslist = disney['year']
disneyyearslist2 = sorted(list(dict.fromkeys(disneyyearslist)))
print(disneyyearslist2)

totalgross = []
yearrange2 = range(2010,2017) #range of years that we consider (2010-2016)
for year in yearrange2:
  disneyyear = disney[disney['year'] == year] #selects the designated year
  grossyear = list(disneyyear['total_gross']) #selects the column containing the gross values for that year in America
  totalgrossyear = sum(grossyear) #sums all the incomes of the movies released in that year 
  totalgross.append(totalgrossyear) #appends the results in a list
print(totalgross)

marvelgross = pd.read_csv("marvelgross2.csv")

marveldisney = marvelgross[marvelgross['Distributor'] == 'Walt Disney Studios Motion Pictures'] #select only the movies released by Disney
marveltotalgross = []
for year in yearrange2:
  marveldisney2 = marveldisney[marveldisney['Year'] == year] #selects the year
  marvelgrossyear = list(marveldisney2['North America']) #selects the incomes only for America
  marveltotalgrossyear = sum(marvelgrossyear) #sums the incomes of the movies released that year
  marveltotalgross.append(marveltotalgrossyear) #appends the results in a list
print(marveltotalgross)

grosspercent = []
x = 0
for gross in totalgross:
  gp = (marveltotalgross[x]/gross)* 100
  grosspercent.append(gp)
  x = x + 1
print(grosspercent)
