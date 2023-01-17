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

def tok (sentence):
    sentence = nltk.word_tokenize(sentence)
    sentence = nltk.pos_tag(sentence)
    return sentence
  
 def movienetwork(genre): #selects a genre to work only on movies in the dataset belonging to the genre choosed 
  movie2 = movie[movie['Genre'] == genre]
  movie3 = movie2['Plot'][:50] #works on plots of movies 
  movie4 = list(movie2['Title'][:50]) #identifies the movie as its title

  movieplot = [] #extracts the movie plot from the dataset
  for plot in movie3:
    movieplot2 = [plot]
    movieplot.append(movieplot2)

  moviepos = [] #tokenizes every words of the plot
  for plot in movieplot:
    for plot2 in plot:
      moviepos.append(tok(plot2))   
  
  moviepos2 = [] #filters only plural and singualr proper nouns
  for plot in moviepos:
    temp1 = []
    moviepos2.append(temp1)
    for word in plot:
      for el in word:
        if el == 'NNP' or el == 'NNPS':
          temp1.append(word)       
  
  moviepos3 = [] #for each plot creates lists of preselected nouns belonging to the same film
  for plot in moviepos2:
    temp2 = []
    moviepos3.append(temp2)
    for word in plot:
      temp2.append(word[0])    

  moviepos4 = [] #deletes duplicates in previous lists
  for plot in moviepos3:
    temp = list(dict.fromkeys(plot))
    moviepos4.append(temp)
  moviepos4.pop(0)
 
  nodes = movie4 # takes movie titles thanks to the genre entered in the function
  
  #creates edges throgh nodes: if there are common words between multiple movie plots, these plots (nodes) are linked togheter
  edges = [] 
  flagposinit = 0 #places nodes in list
  flagpostemp = 0 #places temp in list
  for plot in moviepos4:
    temp = moviepos4[moviepos4.index(plot)+1:] #temporary list that permits to compare the plot under consideration to its following temporary list of different plots
    flagpostemp = flagposinit + 1  
    for plottemp in temp:
      if bool(set(plot) & set(plottemp)): #true if two nodes has some common element
        edges.append([nodes[flagposinit], nodes[flagpostemp]])
      flagpostemp = flagpostemp + 1 #when the plot under consideration has been compared, 
    flagposinit= flagposinit + 1    #this is flagged to continue the operation to the end of moviepos4
  print(edges)
 
  words = [] #join every sublist in a unique list
  for plot in moviepos4:
    for el in plot:
      words.append(el)
  my_dict = dict((el, words.count(el)) for el in words) #which is the most used name?
  sortdict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
  print(sortdict)  
  
  G = nx.Graph() #this function generates graphs of networks, it's able to show nodes and edges between them 
  G.add_nodes_from(nodes)
  G.add_edges_from(edges) 
  plt.figure(figsize=(15,15))
  pos = nx.circular_layout(G)
  nx.draw_networkx(G, pos = pos, node_color= '#fb8500', edge_color= '#023047')
