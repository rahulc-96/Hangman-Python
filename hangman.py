# Hangman game
#

# ----------------------------------

import random
import string

WORDLIST_FILENAME = "C:/Users/RAHUL C/Desktop/Python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for ch in secretWord:
        if ch in lettersGuessed:
            flag=True
        else:
            flag=False
            break
    return flag
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    length=len(secretWord)
    L=[]
    for i in range(length):
        L.append('_')
    for i in range(length):
        if secretWord[i] in lettersGuessed:
            L[i]=secretWord[i]
    s=' '.join(L)
    return s



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s=string.ascii_lowercase
    available=''
    for ch in s:
        if ch not in lettersGuessed:
            available=available+ch
    return available
        
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    length=len(secretWord)
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is "+str(length)+' letters long.')
    print('-----------')
    lettersGuessed=[]
    guesses=8
    correct=False
    while guesses>0:
        if isWordGuessed(secretWord, lettersGuessed):
                print('Congratulations, you won!')
                correct=True
                break
        
        print("You have "+str(guesses)+" guesses left ")
        print('Available Letters:'+getAvailableLetters(lettersGuessed))
        ch=input('Please guess a letter:')
        ch=ch.lower()
        ch=ch.lower()
        available=getAvailableLetters(lettersGuessed)
        if ch not in available:
            print("Oops! You've already guessed that letter:"+getGuessedWord(secretWord, lettersGuessed))
            print('------------') 
            continue
        if ch not in secretWord:
            guesses-=1
            lettersGuessed.append(ch)
            print('Oops! That letter is not in my word:'+getGuessedWord(secretWord, lettersGuessed))
            print('------------')        
        else:
            lettersGuessed.append(ch)
            print('Good guess:'+getGuessedWord(secretWord, lettersGuessed))
            print('------------')
            
            
    if correct==False:
        print('Sorry, you ran out of guesses. The word was '+str(secretWord)+'.')
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
