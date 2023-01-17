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

movie = pd.read_csv("wiki_movie_plots_deduped.csv")

def movieinfo(column_name):
  movieinfonum = movie[column_name].value_counts() #counts the frequency of each value inside a designated column
  movieinfolabel = movie[column_name].tolist() #generate a list containing each element of a column
  c = Counter(movieinfolabel) #counts the frequency of an element
  movieinfolabel2 = sorted(movieinfolabel, key = lambda x : (c[x], x), reverse = True) #sorts the elements in a decreasing order
  movieinfolabel3 = list(dict.fromkeys(movieinfolabel2)) #converts all in dictionary to delete duplicates and then again in a list 
  return(movieinfolabel3,movieinfonum)

yeargenre = []

yearrange = range (1901,2018)

for year in yearrange:
  movieyear = movie[movie['Release Year'] == year] #selects each year
  movieyearnum = movieyear['Genre'].value_counts() #selects the column 'genre' of the designated year and counts the values

  movieyearlabel = movieyear['Genre'].tolist() #creates a list containing all the genre names
  c = Counter(movieyearlabel) #counts the frequency
  movieyearlabel2 = sorted(movieyearlabel, key = lambda x : (c[x], x), reverse = True) #sorts the elements in a decreasing order
  movieyearlabel3 = list(dict.fromkeys(movieyearlabel2)) #converts all in dictionary to delete duplicates and then again in a list
  
#this block selects the second most popular genre if the first is marked as 'unknown', 
#if an alternative is not available it takes 'unknown' to avoid errors
  try: 
    if movieyearlabel3[0] == 'unknown':
      yeargenre.append(movieyearlabel3[1])
    else:
      yeargenre.append(movieyearlabel3[0])
  except:
    yeargenre.append(movieyearlabel3[0])

#this code generates a dictionary containing the year associated with its most popular genre
zip_iterator = zip(yearrange, yeargenre)
a_dictionary = dict(zip_iterator)
print(a_dictionary)

def genretrend(moviegenre):
  genrename = movie[movie['Genre'] == moviegenre] #selects the specific genre
  genreyearnum = genrename['Release Year'].value_counts(sort=False) #counts the number of releases in that year

  genreyearslist = list(genrename['Release Year']) #list of all years involved
  genreyearslist2 = sorted(list(dict.fromkeys(genreyearslist))) #order the list and removes duplicates using a dictionary

#creates a dictionary that associates each year with the number of releases
  genre_zip_iterator = zip(genreyearslist2, genreyearnum)
  genre_dictionary = dict(genre_zip_iterator)

#the dictionary called 'genre_dictionary' contains only the years where a movie belonging to the selected genre was released,
#to avoid the missing years we used the following code that generates a dictionary full of zeros as replacement:

  allyears = list(yearrange) #list containing all years 

#creates a list containg a '0' for each year in yearrange
  zerolist = []
  for element in yearrange:
    zerolist.append(0)

#creates a dictionary that associates each year with a '0'
  allyears_zip_iterator = zip(allyears, zerolist)
  allyears_dictionary = dict(allyears_zip_iterator)

#updates the dictionary with the missing years
  fixed_genre = allyears_dictionary.copy()
  fixed_genre.update(genre_dictionary)

  return(fixed_genre)
