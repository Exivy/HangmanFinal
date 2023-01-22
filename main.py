from replit import clear

import random


import hangman_art
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
playgame = True
while playgame == True:
  
  end_of_game = False
  lives = 6
  print (hangman_art.logo)
  #Testing code
  #print(f'Pssst, the solution is {chosen_word}.')
  
  #Create blanks
  display = []
  guesses = []
  for _ in range(word_length):
      display += "_"  
  while not end_of_game:
      guess = input("Guess a letter: ").lower()
      clear()
      print (hangman_art.logo) 
      print ()
      guesses += guess
      print (f"You already guessed: {', '.join(guesses)}")
      if guess in display:
        print (f"You already guessed '{guess}'")       
      for position in range(word_length):
          letter = chosen_word[position]          
          if letter == guess:
              display[position] = letter
  
      
      if guess not in chosen_word:
          
          print (f"'{guess}' is not in the word.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print(hangman_art.you_lose)
            
              print (f'The word was: "{chosen_word}" ')
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print(hangman_art.you_won)
  
      
      print(hangman_art.stages[lives])
  play_again = input("If you'd like to play again, please type 'y': ").lower()
  clear()
  if play_again == "y":
    continue
    
  else:
    break
print (hangman_art.logo)
print ("")
print ("Thank you for playing.")