# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...\n")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return set(list(secret_word)).issubset(letters_guessed)#fucking great technique, I wasted hours on this

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_str = []

    for char in secret_word:
        if char in letters_guessed:
            new_str += char
        else:
            new_str += "_ "

    return "".join(new_str)



def incorrect_letters(letters_guessed, secret_word):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have
    been guessed incorrectly.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    incorrect = []

    for char in letters_guessed:
        if char not in secret_word:
            incorrect.append(char+' ') 

    return "".join(incorrect)

def start(secret_word, on = True):

    print(f'''
    Welcome to the game Hangman! It's the game where someone is hanged because of you!
    I am thinking of word that is {len(secret_word)} letters long
    ----------------------------------------
    You have 6 guesses left
    You have 3 warnings left
    Available letters: {string.ascii_lowercase}
    ''')

def choker(guess, letters_guessed):
    '''
    Checks if it has non alphabets, multiple letters, duplicate letters
    '''
    if not str.isalpha(guess) or len(guess) > 1:
        print(''.rjust(40, '-'))
        print("Enter a single letter!\n")

        return True

    elif guess in letters_guessed:
        print(''.rjust(40, '-'))
        print("Enter a DIFFERENT letter!\n")

        return True

    else:
        return False

def vowel_check(guess, secret_word):
    vowels = ['a','e','i','o','u']
    return set(list(guess)).issubset(vowels)

def win_prompt(guess_left, secret_word):
    score = guess_left * len(set(secret_word))
    print(f'''
    {''.rjust(40, '-')}
    {secret_word.center(40, '-')}
    {'You Win!'.center(40, '-')}
    Your score was {score} points, congrats!'
    {''.rjust(40, '-')}
        ''')
def game(secret_word, hint = True):
    guess_left = 6
    letters_guessed = []
    warnings = 3

    while guess_left > 0:
        guess = input("Please guess a letter: ").lower().strip()
        
        if guess == '*':
            print("Possible matches are: ")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print(''.rjust(40, '-'))
            continue


        if choker(guess, letters_guessed):
            warnings -= 1
            if warnings == 0:
                guess_left -= 1
                print(''.rjust(40, '-'))
                print("Haha you just lost a guess\n")
                warnings = 3

            print("Guesses left: ", guess_left)
            print("Warnings left: ", warnings)
            print(get_guessed_word(secret_word, letters_guessed))

            continue
            
        letters_guessed.append(guess)

        if guess in secret_word:
            if is_word_guessed(secret_word, letters_guessed):
                win_prompt(guess_left, secret_word)
                break
            print(f'''
    {''.rjust(40, '-')}
    Oh wow that was correct!
    {get_guessed_word(secret_word, letters_guessed)}
    Incorrect letters: {incorrect_letters(letters_guessed, secret_word)}
    Guesses left: {guess_left}
    Warnings left: {warnings}
    {''.rjust(40, '-')}
            ''')
        else:
            if vowel_check(guess, secret_word):
                guess_left -= 2
            else:
                guess_left -= 1
            
            print(f'''
    {''.rjust(40, '-')}
    That's incorrect, you fool!
    {get_guessed_word(secret_word, letters_guessed)}
    Incorrect letters: {incorrect_letters(letters_guessed, secret_word)}
    Guesses left: {guess_left}
    Warnings left: {warnings}
    {''.rjust(40, '-')}
            ''')
            

    if not is_word_guessed(secret_word, letters_guessed):
        print(f'''
        {''.rjust(40, '-')}
        You fail! The dude has been hanged!!
        {''.rjust(40, '-')}
                    \n
        _________ 
        |       |   
        |       0   
        |      /|\  
        |      / \  
        |           
        |           \n

        {''.rjust(40, '-')}
        The word was: {secret_word}
        ''')

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    start(secret_word)
    game(secret_word, hint = False)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i = 0
    for char in my_word.replace(" ", ""):
        if i >= len(other_word):
            return False
        if char != other_word[i] and char != "_":
            return False
        i += 1
    return True

    #word = my_word.replace(" ", "")
    #word2 = word.replace("_", "")
    #return set(word2).issubset(set(other_word)) and (len(word) == len(other_word)) 
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            print(other_word)




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    start(secret_word)
    game(secret_word)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    #hangman_with_hints("doonkey")

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
