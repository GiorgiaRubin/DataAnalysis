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

#cretentials of the API used by Praw to connect with Reddit
reddit = praw.Reddit(client_id='client', 
                     client_secret='client', 
                     user_agent='agent', 
                     username='name', 
                     password='password')

subreddit = reddit.subreddit('movies') #this code tells Praw to connect to the subreddit call r/movies
sub = subreddit.top('year', limit=250) #this code selects the top 250 post of the last year

#the following code creates a list that contains all the post that we selected previously:
post = []
for submission in sub:
  post.append(submission.title)
  
  #this code counts the number of post that contains one of the keyword related to superheroes
co = 0
shwords = ['Marvel', 'marvel', 'DC', 'dc', 'Superhero', 'superhero', 'Superman', 'Batman', 'Avengers', 'Spider-Man', 'Venom', 'Eternals', 'Black Widow', 'Mutants', 'Shang-Chi', 'Deadpool', 'Suicide Squad', 'Doctor Strange', 'Thor', 'Black Panther', 'Guardians of the Galaxy', 'Ant Man', 'Fantastic Four', 'Captain America']
for posttitle in post:
  for word in shwords:
    if word in posttitle:
      co = co + 1
print (co)

#this is the total number of posts
co2 = 0
for posttitle in post:
  co2 = co2 + 1
print(co2)

#this code calculates the percent of superhero related posts over the total
percent = (co/co2)*100
percent = round(percent,1)
print(percent)

#the same operation has been made with r/all instead of r/movies to focus on a community that is not exclusively related to cinema
subreddit2 = reddit.subreddit('all')
sub2 = subreddit2.top('year', limit=250)

post2 = []
for submission in sub2:
  post2.append(submission.title)
print(post2)

co3 = 0
shwords = ['Marvel', 'marvel', 'DC', 'dc', 'Superhero', 'superhero', 'Superman', 'Batman', 'Avengers', 'Spider-Man', 'Venom', 'Eternals', 'Black Widow', 'Mutants', 'Shang-Chi', 'Deadpool', 'Suicide Squad', 'Doctor Strange', 'Thor', 'Black Panther', 'Guardians of the Galaxy', 'Ant Man', 'Fantastic Four', 'Captain America']
for posttitle in post2:
  for word in shwords:
    if word in posttitle:
      co3 = co3 + 1
print (co3)

co4 = 0
for posttitle in post:
  co4 = co4 + 1
print(co4)

percent2 = (co3/co4)*100
percent2 = round(percent2,1)
print(percent2)
