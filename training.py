import engine
import math

with open("words.csv") as f:
    words = []
    for line in f:
        line = line.strip()
        words.append(line)

# def compute_entropy(evaluated):
    

def make_guess(guessing_list, answer_list):
    max_entropy = -1
    best_guess = ""

    for guess in guessing_list:
        bins = {}
        for a in answer_list:
            mask = engine.evaluate_guess(guess, a)
            if mask not in bins.keys():
                bins[mask] = 1
            else:
                bins[mask] += 1

        print(bins)
        # new_entropy = compute_entropy(bins.values())
        # if new_entropy > max_entropy:
        #     max_entropy = new_entropy
        #     buest_guess = guess
    
    # return buest_guess
        
make_guess(words, words)