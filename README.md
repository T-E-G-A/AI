# Guess the Word: AI-Based Game Development

This repository contains the implementation of the "Guess the Word" program, an interactive console-based game I developed as part of the **MOD004553 Artificial Intelligence Module** at Anglia Ruskin University. The program features unique mechanics for two difficulty levels: EASY and HARD, showcasing AI techniques in interactive systems.

---

## Project Overview

The "Guess the Word" game challenges players to guess a hidden word by suggesting letters. The program incorporates dynamic word pattern updates and word pool refinements to enhance gameplay. The HARD mode introduces innovative mechanics that require strategic thinking and highlight AI-based decision-making.

---

### Programme Design and Features

#### 1. Word Loading
- The `load_word_list` function reads a dictionary file, filters words by length, and generates a list of valid words.
  - **Strength:** Supports flexible word pools for varied gameplay.
  - **Limitation:** Dependent on dictionary file quality and path accuracy.

#### 2. Dynamic Word Revelation
- The `reveal_word` function dynamically updates the word pattern based on player guesses:
  - **EASY Mode:** Reveals all instances of correctly guessed letters.
  - **HARD Mode:** Reveals only as many instances as guessed so far, adding strategic complexity.
  - **Strength:** Provides immediate feedback for player engagement.
  - **Limitation:** HARD mode mechanics may confuse new players.

#### 3. Word Pool Refinement
- The `refine_word_pool` function dynamically filters the possible word list based on guessed letters and revealed patterns.
  - **Strength:** Efficiently narrows down possibilities to match gameplay progression.
  - **Limitation:** Can slow down for very large dictionaries.

---

### Difficulty Modes

#### EASY Mode
- Reveals all instances of correctly guessed letters.
- Example: For the word "BALLOON," guessing 'L' reveals "_ _ L L _ _ _."
- **Summary:** Encourages success with straightforward feedback.

#### HARD Mode
- Reveals one instance of a guessed letter at a time, requiring repeated guesses for multiple occurrences.
- Example: For "BALLOON," guessing 'L' once reveals "_ _ L _ _ _ _." Guessing 'L' again reveals the next 'L.'
- **Summary:** Introduces challenging mechanics that demand strategic guessing.

---

### Strengths
- **Dynamic Feedback:** Updates word patterns in real-time for engaging gameplay.
- **Customizable Word Pool:** Supports dictionary expansion for varied experiences.
- **Replayability:** Randomized word selection and adaptive difficulty ensure new challenges in every session.

---

### Limitations
- **External File Dependency:** Errors in the dictionary file can disrupt gameplay.
- **Performance Concerns:** Large dictionaries may cause delays in word pool filtering.
- **HARD Mode Complexity:** The mechanics may frustrate players unfamiliar with the rules.

---

## Development Reflection
The program leverages Python's flexibility in implementing algorithms and data structures. HARD mode's mechanics stand out for their innovative approach, introducing an added layer of difficulty and strategic depth. Future improvements could optimize performance for larger word pools and incorporate tutorials to improve the accessibility of HARD mode.

---

## Instructions for Running the Program (Appendix 1)

### Setup Requirements
1. Install Python 3.x.
2. Place the dictionary file (e.g., `dictionary.txt`) in the same directory as the program.

### Running the Program
1. Open a terminal or command prompt.
2. Navigate to the program's directory and execute the script:
   ```bash
   python guesstheword.py
