#!/usr/bin/env python

import sys

def words_freq(file_object):
    '''
      Counts the frequency of each word occuring in a file
      
      Arguments:
              file_object: name of file object created for the input file containing the tweets

      Returns:
              A dictionary containing key/value pairs of word/frequency
    '''
    freq_dict = {}                                                   # Initialising a new dictionary that will store each word as a key, and its frequency as its value
    for line in file_object:                                         # Going through each line in the file. This method avoids storing the entire file into memory
       lst = line.split()                                            # Splits the line into a list of words
       for word in lst:                                              # Going through each word in tweet, if it exists increment its frequency by 1, else initialise it
           if word in freq_dict:
              freq_dict[word] += 1
           else:
              freq_dict[word] = 1
    return freq_dict


def write_freq_file(file_object, dict):
    '''
      Writes a file using data from a dictionary

      Arguments:
              file_object:    name of file object written into
              dict:           name of input dictionary whose key/value pairs are written on new lines of a file

      Returns:
              None
    '''
    for word in sorted(dict):                                        # Going through each word in the dictionary that is sorted according to ASCII code
       file_object.write(word + ' '*(40 - len(word)) + str(dict[word]) + '\n')        # Writing each word and its frequency, separated by a fixed space, on a new line


if __name__ == '__main__':
   try:
      input_file_path = sys.argv[1]
      output_file_path = sys.argv[2]
   except:
      print "Error: please check file names or path"
   tweets = open(input_file_path, 'r')                               # File object that points to the input file containing tweets, and opened in reading mode
   count_words = words_freq(tweets)                                  # Stores the ouput of the "words_freq" function
   tweets.close()                                                    # Close the file object
   ft1 = open(output_file_path, 'w')                                 # File object that points to the output file which prints the words and their frequencies
   write_freq_file(ft1, count_words)                                 # To write the file
   ft1.close()                                                       # Close the file object

