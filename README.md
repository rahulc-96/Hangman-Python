# Hangman-Python
A python code that implements a variation of the classic word guessing game of Hangman. For additional information regarding the game do visit this link:http://en.wikipedia.org/wiki/Hangman%20%28game%29

words.txt file contains all the available words that can be used to frame the word list.

On successful loading of the words list, following message will be displayed:
   
Loading word list from file...
55909 words loaded.

If you see an IOError instead (e.g., "No such file or directory"), you should change the value of the WORDLIST_FILENAME constant (defined near the top of the file) to the complete pathname for the file words.txt (This will vary based on where you saved the file). Windows users, change the backslashes to forward slashes, like below.
For example, if you saved ps3_hangman.py and words.txt in the directory "C:/Users/Ana/" change the line: 

WORDLIST_FILENAME = "words.txt"  to something like\

WORDLIST_FILENAME = "C:/Users/Ana/words.txt"

This folder will vary depending on where you saved the files.
