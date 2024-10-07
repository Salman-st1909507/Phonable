def backtrack(words, target_length, current_combination, current_length, results):
    # Base Case: If the current combination matches the target length
    if current_length == target_length:
        results.append(" ".join(current_combination))
        return

    # Recursive Case: Try adding each word to the current combination
    for i in range(len(words)):
        word = words[i]
        
        # Calculate the new length if we add this word
        new_length = current_length + len(word) + (1 if current_combination else 0)  # +1 for space
        
        # If the new length is less than or equal to the target length, proceed
        if new_length <= target_length:
            current_combination.append(word)  # Add the word to the combination
            backtrack(words, target_length, current_combination, new_length, results)
            current_combination.pop()  # Backtrack (remove the last added word)

def find_word_combinations(words, target_length):
    results = []
    backtrack(words, target_length, [], 0, results)
    return results

# Example usage
words = ["cat", "dog", "mouse", "bat"]
target_length = 9
combinations = find_word_combinations(words, target_length)

for combo in combinations:
    print(combo)
