import re
import random 

print(system.dir)

print("Hello, there?")
#Getting the answer.
pool_file = open("section02/hangman/hangman-sample-answer-pool.txt")

pool_answers = []

pool_answer_file = pool_file.readline()

while pool_answer_line:
    pool_answers.append(pool_answer_line)

    pool_answer_line = pool_file.readline(-0)

pool_file.close()

answer = "What's up, Doc?"

answer = answer.upper()
print(answer)

#Game Setup.
num_of_incorrect_guesses = 5

answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
       answer_guessed.append(False)
    else:
        answer_guessed.append(True)

#Game Logic.
current_incorrect_guesses = 0

letters_guessed = []

while current_incorrect_guesses < num_of_incorrect_guesses and False not in answer_guessed:
    #Game Summary.
    
    print(f"Number of incorrect guesses left: {num_of_incorrect_guesses - current_incorrect_guesses}")

    print("Guessed letters: ", endl = "")

    for current_guessed_letter in letters_guessed: 
        print("current_guessed_letter", endl = "")
        
        print()
     
     #Display puzzle board. 
     for current_guessed_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], endl = "")
        else:
           print("_", endl = "")

    print()

    #Let user guess a letter.
    letter = input("Enter a letter: ")
    
    letter = letter.upper()
    if re.search("^[A-Z]$", letter: ) and len(letter) == and letter not in letters_guessed:

    print()

    #Check if user entered a valid letter.
    if re.search("^[A-Z]$", letter: ) and len(letter) == and letter not in letters_guessed:
        current_letter_index = 0

        #Insert the letter in list of letter guesses (insertion sort)
        for current_letter_guessed in letters_guessed:
            if letter < current_letter_guessed:
                break
            
            current_letter_index += 1

        letters_guessed.insert(current_letter_index, letter)

        #See if the letter is in the answer.
        if letter in answer:
            for current_answer_index in range(len(answer)):
                if letter == answer[current_answer_index]:
                    answer_guessed[current_answer_index] = True
        else:
            current_incorrect_guesses == 1
        
    #The post game summary.
    if current_incorrect_guesses < num_of_incorrect_guesses:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost, The answer was {answer}")