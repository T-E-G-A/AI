import random

def load_word_list(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()

def pick_random_word(words, desired_length):
    return random.choice([word for word in words if len(word) == desired_length])

def reveal_word(secret_word, guessed_characters, hard_mode=False):
    if not hard_mode:
        # Easy mode: Reveal all occurrences of correctly guessed characters
        return ''.join([char if char in guessed_characters else '_' for char in secret_word])
    else:
        # Hard mode: Reveal only guessed occurrences of each character
        revealed = ['_'] * len(secret_word)
        for idx, char in enumerate(secret_word):
            if char in guessed_characters:
                count_in_word = secret_word[:idx + 1].count(char)
                count_in_guesses = guessed_characters[char]
                if count_in_guesses >= count_in_word:
                    revealed[idx] = char
        return ''.join(revealed)

def refine_word_pool(words, guessed_characters, revealed_pattern):
    return [
        word for word in words
        if len(word) == len(revealed_pattern) and all(
            char in guessed_characters or char == revealed_pattern[idx]
            for idx, char in enumerate(word)
        )
    ]

def play_easy(words, target_word, guessed_set, attempts_left):
    while attempts_left > 0:
        print(f"\nRemaining attempts: {attempts_left}")
        print("Current word:", reveal_word(target_word, guessed_set))
        print("Guessed letters:", ", ".join(sorted(guessed_set)))

        guess = input("Enter a single letter: ").lower()
        while len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please type a single letter.")
            guess = input("Enter a single letter: ").lower()

        if guess in guessed_set:
            print("You already tried that letter.")
            continue

        guessed_set.add(guess)

        if guess in target_word:
            print("Nice! That letter is in the word.")
            if set(target_word) <= guessed_set:
                print(f"Well done! You discovered the word: {target_word}")
                return True
        else:
            print("Oops! That letter isn't in the word.")
            attempts_left -= 1

        words = refine_word_pool(words, guessed_set, reveal_word(target_word, guessed_set))

    print(f"\nOut of attempts! The word was: {target_word}")
    return False

def play_hard(words, target_word, guessed_set, attempts_left):
    guessed_count = {char: 0 for char in set(target_word)}

    while attempts_left > 0:
        print(f"\nRemaining attempts: {attempts_left}")
        print("Current word:", reveal_word(target_word, guessed_count, hard_mode=True))
        print("Guessed letters:", ", ".join(f"{char}:{count}" for char, count in guessed_count.items() if count > 0))

        guess = input("Enter a single letter: ").lower()

        # Penalize invalid guesses
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Non-letter characters cost an attempt.")
            attempts_left -= 1
            continue

        if guess in guessed_count:
            guessed_count[guess] = guessed_count.get(guess, 0) + 1

            # Remove from guesses if all occurrences are found
            if guessed_count[guess] > target_word.count(guess):
                guessed_count[guess] -= 1
                print("Oops! That letter isn't in the word.")
                attempts_left -= 1
                continue

        if guess in target_word:
            print("Nice! That letter is in the word.")
            if all(guessed_count[char] >= target_word.count(char) for char in set(target_word)):
                print(f"Well done! You discovered the word: {target_word}")
                return True
        else:
            print("Oops! That letter isn't in the word.")
            attempts_left -= 1

        words = refine_word_pool(words, guessed_count, reveal_word(target_word, guessed_count, hard_mode=True))

    print(f"\nOut of attempts! The word was: {target_word}")
    return False

def main():
    try:
        dictionary_path = "dictionary.txt"
        word_collection = load_word_list(dictionary_path)
        chosen_length = random.randint(4, 12)
        selected_word = pick_random_word(word_collection, chosen_length)
        max_attempts = chosen_length * 2

        mode = input("Select difficulty (easy/hard): ").lower()

        if mode == "easy":
            play_easy(word_collection, selected_word, set(), max_attempts)
        elif mode == "hard":
            play_hard(word_collection, selected_word, set(), max_attempts)
        else:
            print("Invalid difficulty choice. Exiting game.")
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")

if __name__ == "__main__":
    main()
