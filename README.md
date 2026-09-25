# Python-Quiz-Master
A command-line quiz application built with Python and SQLite featuring random questions, score tracking, and a leaderboard.

## FIRST UNDERTAND THIS BEFORE GOING TO THE PROGRAM 👇👇👇:
## Workflow

### 1️⃣ Play Quiz
1. Ask player's name
2. Get 5 random questions from database
3. Show each question + 4 options
4. Player answers
5. Check answer
6. Keep score
7. After 5 questions → show final score
8. Save score in database
9. Return to main menu
### Example

```text
Player: Alex

Question 1/5

What is 2 + 2?

A. 3
B. 4
C. 5
D. 6

Answer: B

✓ Correct!
```

### 2️⃣ View Leaderboard
1. Get saved scores from database
2. Sort highest → lowest
3. Display leaderboard
4. Return to main menu
## Example Leaderboard
```text
========== LEADERBOARD ==========

Rank   Name       Score
1      Alex       5
2      Rahul      4
3      Priya      3
```


### 3️⃣ Add Question
1. Ask for question
2. Ask for option A
3. Ask for option B
4. Ask for option C
5. Ask for option D
6. Ask for correct answer
7. Save everything in QUESTIONS table
8. Return to main menu
### Example

```text
Question: What is Python?

A: Programming Language
B: Database
C: Operating System
D: Browser

Correct answer: A

✓ Question added!
```

### 4️⃣ Exit
1. Close database connection
2. End program
