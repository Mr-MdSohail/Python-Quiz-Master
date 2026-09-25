# 1️⃣ Play Quiz
# 1. Ask player's name
# 2. Get 5 random questions from database
# 3. Show each question + 4 options
# 4. Player answers
# 5. Check answer
# 6. Keep score
# 7. After 5 questions → show final score
# 8. Save score in database
# 9. Return to main menu
# Example
# Player: Alex
# Question 1/5
# What is 2 + 2?
# A. 3
# B. 4
# C. 5
# D. 6
# Answer: B
# ✓ Correct!

# 2️⃣ View Leaderboard
# 1. Get saved scores from database
# 2. Sort highest → lowest
# 3. Display leaderboard
# 4. Return to main menu
# Example:
# ========== LEADERBOARD ==========
# Rank   Name       Score
# 1      Alex       5
# 2      Rahul      4
# 3      Priya      3

# 3️⃣ Add Question
# 1. Ask for question
# 2. Ask for option A
# 3. Ask for option B
# 4. Ask for option C
# 5. Ask for option D
# 6. Ask for correct answer
# 7. Save everything in QUESTIONS table
# 8. Return to main menu
# Example:
# Question: What is Python?
# A: Programming Language
# B: Database
# C: Operating System
# D: Browser
# Correct answer: A
# ✓ Question added!

# 4️⃣ Exit
# 1. Close database connection
# 2. End program

import sqlite3
from tabulate import tabulate

connection = sqlite3.connect(
    r"quiz_master.db"
)
cursor = connection.cursor()
print("========== WELCOME TO THE QUIZ ==========")
while True:
    print("1. Play Quiz\n2. View Leaderboard\n3. Add Question\n4. Exit\n")
    try:
        user_choice = int(input("Enter your choice:  \n"))
        choices=[1,2,3,4]
        if user_choice not in choices:
            print("Please choose a valid option")
            continue
    except ValueError:
        print("Please choose a valid option")
        continue
    if user_choice==1:
        while True:
            username=input("Enter your name: ").upper()
            if username != '':
                break
            else:
                print("Please enter a valid username...")
        cursor.execute(
            '''SELECT * FROM SCORES
            WHERE PLR_NAME=?;''',
            (username,)
        )
        exists=cursor.fetchone()
        if exists!=None:
            print(f"\n========== WELCOME BACK {username} ==========")
        else:
            cursor.execute(
                '''INSERT INTO SCORES (PLR_NAME,PLR_SCORE) VALUES(?,0);''',
                (username,)
            )
            connection.commit()
        table=cursor.execute(
        '''SELECT QUESTION,OPTA,OPTB,OPTC,OPTD,CORRECT FROM QUIZ
        ORDER BY RANDOM()
        LIMIT 5;'''
        )
        rows=cursor.fetchall()
        options=['','A.','B.','C.','D.']
        user_options=['A','B','C','D']
        user_score=0
        for i in rows:
            print("\nQ.",i[0])
            print("Options:")
            for k in range(1,5):
                print(options[k],i[k])
            while True:
                user_ans=input("Enter answer(A/B/C/D): ").upper()
                if user_ans not in user_options:
                    print("Please choose a valid option...")
                else:
                    break
            if user_ans==i[5]:
                user_score=user_score+1
        print(f"You got {user_score} correct!!")
        cursor.execute(
            '''UPDATE SCORES
            SET PLR_SCORE=PLR_SCORE+?
            WHERE PLR_NAME=?;''',
            (user_score,username,)
        )
        connection.commit()

    elif user_choice==2:
        cursor.execute(
            '''SELECT * FROM SCORES
            ORDER BY PLR_SCORE DESC;'''
        )
        leaderboard=cursor.fetchall()
        print(tabulate(leaderboard,headers=['Rank','Player Name','Player Score'],tablefmt='fancy_grid',showindex=range(1,len(leaderboard)+1)))

    elif user_choice==3:
        while True:
            print("========== ADD QUESTION ==========")
            while True:
                question=input("Enter question: ").upper()
                if question != '':
                    break
                else:
                    print("Please enter a valid question...")
            while True:
                op1=input("Enter option A: ").upper()
                op2=input("Enter option B: ").upper()
                op3=input("Enter option C: ").upper()
                op4=input("Enter option D: ").upper()
                if (op1!= '' and op2!= '' and op3!= '' and op4!= ''):
                    break
                else:
                    print("Please enter valid options")
            while True:
                correct_op=input("Enter correct option : ").upper()
                if correct_op not in user_options:
                    print("Please enter a valid correct option")
                else:
                    break
            cursor.execute(
                '''INSERT INTO QUIZ (QUESTION,OPTA,OPTB,OPTC,OPTD,CORRECT) VALUES(?,?,?,?,?,?);''',
                (question,op1,op2,op3,op4,correct_op,)
            )
            connection.commit()
            print("Question added successfully !")
            while True:
                another_choices=['Y','N','YES','NO']
                another=input("Add another question? (Y/N)").upper()
                if another not in another_choices:
                    print("please enter a valid option (Y/N)")
                    continue
                else:
                    break
            if another=='N' or another=='NO':
                break

    elif user_choice==4:
        print("Think you've seen it all? 😏 More crazy questions are waiting for you... Come back soon!")
        break