#!/usr/bin/env python

import sys
import numpy as np

def running_median(file_object, file):
    '''
      Counts the number of unique words per line in a file, and calculates their running median

      Arguments:
              file_object: name of file object created for the input file containing the tweets

      Returns:
              None
    '''
    count_tweets = 0                                                   # Keep track of number of tweets
    median = 0.0                                                       # Current median
    for line in file_object:                                           # Going through each line in the file. This method avoids storing the entire file into memory
        count_tweets += 1                                              
        unique_words = {}                                              # Initialising a new dictionary that will store each unique word as a key
        lst = line.split()                                             # Splits the line into a list of words
        for word in lst:                                               # Going through each word in tweet, if it exists do nothing, else initialise it
            if word not in unique_words:
               unique_words[word] = 1
        median = ((median*(count_tweets-1)) + len(unique_words))/count_tweets     # Formula for calculating current median that scales well with input size
        file.write(str(median) + '\n')                               # Writing the median of a growing list of medians to the output file


if __name__ == '__main__':
   try:
      input_file_path = sys.argv[1]
      output_file_path = sys.argv[2]
   except:
      print "Error: please check file names or path"
   tweets = open(input_file_path, 'r')                                 # File object that points to the input file containing tweets, and opened in reading mode 
   ft2 = open(output_file_path, 'w')                                   # File object that points to the output file containing medians, and opened in writing mode
   running_median(tweets, ft2)                                     
   tweets.close()                                                      # Close the file object 
   ft2.close()                                                         # Close the file object

