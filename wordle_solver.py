import random
import nltk
from nltk.corpus import words

nltk.download('words')

# List of possible words from the English dictionary
word_list = words.words()

def get_feedback(guess, solution):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            feedback.append('correct')
        elif guess[i] in solution:
            feedback.append('present')
        else:
            feedback.append('absent')
    return feedback

def filter_words(word_list, guess, feedback):
    filtered_words = []
    for word in word_list:
        if len(word) != len(guess):
            continue
        match = True
        for i in range(len(guess)):
            if feedback[i] == 'correct' and word[i] != guess[i]:
                match = False
                break
            elif feedback[i] == 'present' and (word[i] == guess[i] or guess[i] not in word):
                match = False
                break
            elif feedback[i] == 'absent' and guess[i] in word:
                match = False
                break
        if match:
            filtered_words.append(word)
    return filtered_words

def solve_wordle(word_list):
    solution = random.choice([word for word in word_list if len(word) == 5])  # Assuming the solution length is 5
    word_list = [word for word in word_list if len(word) == len(solution)]
    attempts = 0
    while True:
        guess = random.choice(word_list)
        attempts += 1
        feedback = get_feedback(guess, solution)
        print(f"Attempt {attempts}: Guess = {guess}, Feedback = {feedback}")
        if feedback == ['correct'] * len(solution):
            print(f"Solved! The word is {solution}. Attempts: {attempts}")
            break
        word_list = filter_words(word_list, guess, feedback)

if __name__ == "__main__":
    solve_wordle(word_list)
