from collections import Counter
import random

def predict_next(numbers):
    counter = Counter(numbers)
    total = sum(counter.values())
    probabilities = {num: count / total for num, count in counter.items()}
    weighted_probs = [(num, prob + random.uniform(0, 0.05)) for num, prob in probabilities.items()]
    weighted_probs.sort(key=lambda x: x[1], reverse=True)
    return weighted_probs[0][0]
