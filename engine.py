import random as rd
import math

with open("words.csv") as f:
    guessing_list = []
    for line in f:
        line = line.strip()
        guessing_list.append(line)

word = rd.choice(guessing_list)

def compute_entropy(int_list):
    total = sum(int_list)
    entropy = 0
    for i in int_list:
        p = i / total
        entropy += -p * math.log(p)

    return entropy

def make_guess(guessing_list, a_list):
    max_entropy = -1
    best_guess = ""

    for guess in guessing_list:
        bins = {}
        for a in guessing_list:
            mask = evaluate_guess(guess, a)
            if mask not in bins.keys():
                bins[mask] = 1
            else:
                bins[mask] += 1

        new_entropy = compute_entropy(bins.values())
        if new_entropy > max_entropy:
            max_entropy = new_entropy
            best_guess = guess
    
    return best_guess
        

def evaluate_guess_char(guess, answer, pos):
    if answer[pos]==guess[pos]:
        return "Y"
    unmatched_answer_chars = 0
    unmatched_guess_chars = 0
    this_guess_num = 0 
    for i in range(5):
        if answer[i]==guess[pos]:
            if answer[i]!=guess[i]:
                unmatched_answer_chars += 1
        if guess[i]==guess[pos]:
            if answer[i]!=guess[i]:
                unmatched_guess_chars += 1
                if i<pos:
                    this_guess_num += 1
    if this_guess_num<unmatched_answer_chars:
        return "M"
    return "N"

def evaluate_guess(guess, answer):
    return "".join(evaluate_guess_char(guess, answer, i) for i in range(5))

def game_over(accuracy):
    for acc in accuracy:
        if acc != "🟩":
            return False
    return True

# 2P
def play_game(word):
    answer_list = guessing_list.copy()
    opening = "raise"
    mask = input("What was the result? (in 0,1,2s): ")
    mask = (mask.replace("2", "Y")
                .replace("1", "M")
                .replace("0", "N"))
    answer_list = [a for a in answer_list if evaluate_guess(opening, a) == mask]
    while len(answer_list) > 1:
        best_guess = make_guess(answer_list, answer_list)
        print("Try", best_guess)

        mask = input("What was the result? (in 0,1,2s): ")
        mask = (mask.replace("2", "Y")
                    .replace("1", "M")
                    .replace("0", "N"))
        answer_list = [a for a in answer_list if evaluate_guess(best_guess, a) == mask]
    
    print("Word is", answer_list)

play_game(word)

# CPU
# def play_game(answer):
#     best_guess = "raise"
#     mask = evaluate_guess(best_guess, answer)
#     answer_list = guessing_list.copy()
    
#     answer_list = [a for a in answer_list if evaluate_guess(best_guess, a) == mask]
#     print(best_guess)
#     mask = (mask.replace("Y", "🟩")
#                 .replace("M", "🟨")
#                 .replace("N", "⬛"))

#     print(mask)
#     for _ in range(5):
#         best_guess = make_guess(answer_list, answer_list)
#         print(best_guess)
#         mask = evaluate_guess(best_guess, answer)
#         answer_list = [a for a in answer_list if evaluate_guess(best_guess, a) == mask]

#         mask = (mask.replace("Y", "🟩")
#                     .replace("M", "🟨")
#                     .replace("N", "⬛"))
        
#         # print(best_guess)
#         print(mask)
#         if game_over(mask):
#             print("Word guessed:", answer)
#             return
#     print("Game over, word was:", answer)

# play_game(word)
