# 🎯 Kaun Banega Lakhpati

A **Python-based command-line quiz game** inspired by the format of popular Indian quiz shows. The player answers a series of multiple-choice questions and can choose to continue or exit after each correct answer.

The project demonstrates Python fundamentals such as **functions, lists, dictionaries, loops, conditional statements, modules, input validation, and basic game logic**.

## 🎮 Game Features

* 10 multiple-choice questions
* 4 options for every question
* Prize ladder from **₹1,000 to ₹1,00,000**
* Continue or exit after every correct answer
* **₹20,000 safety checkpoint** after Question 5
* If the player answers incorrectly before the safety checkpoint, winnings become ₹0
* If the player answers incorrectly after reaching the safety checkpoint, ₹20,000 is retained
* Input validation for A/B/C/D answers
* Separate Python modules for questions, prizes, and game logic
* Command-line interface

## 💰 Prize Structure

| Question |        Prize |
| -------- | -----------: |
| 1        |       ₹1,000 |
| 2        |       ₹2,000 |
| 3        |       ₹5,000 |
| 4        |      ₹10,000 |
| 5        |   ₹20,000 🔒 |
| 6        |      ₹30,000 |
| 7        |      ₹40,000 |
| 8        |      ₹50,000 |
| 9        |      ₹75,000 |
| 10       | ₹1,00,000 🏆 |

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* String Manipulation
* Modules
* Input Validation

## 📂 Project Structure

```text
Kaun_Banega_Lakhpati/
│
├── main.py
├── game.py
├── questions.py
├── prizes.py
└── README.md
```

### `main.py`

Entry point of the application. It displays the game introduction and starts the game.

### `game.py`

Contains the main game logic, including:

* Displaying questions
* Accepting answers
* Checking answers
* Managing winnings
* Safety checkpoint
* Continue/exit functionality

### `questions.py`

Contains the quiz questions, options, and correct answers.

### `prizes.py`

Contains the prize ladder and safety checkpoint configuration.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Kaun-Banega-Lakhpati.git
```

### 2. Open the project

```bash
cd Kaun-Banega-Lakhpati
```

### 3. Run the game

```bash
python main.py
```

## 🎯 Game Flow

```text
Start Game
    ↓
Display Question
    ↓
Select A / B / C / D
    ↓
Check Answer
    ↓
Correct?
 ┌──Yes───────────────No──┐
 ↓                         ↓
Update Winnings       Apply Safety Amount
 ↓                         ↓
Reached Q5?            Game Over
 ↓
Ask Continue?
 ┌──Yes──────No──┐
 ↓               ↓
Next Question   Exit
 ↓
Question 10
 ↓
₹1,00,000 🏆
```

## 🧠 Learning Objectives

This project was developed to practice and demonstrate:

* Python programming fundamentals
* Breaking a program into multiple modules
* Designing functions for specific responsibilities
* Working with lists and dictionaries
* Implementing loops and conditions
* Handling user input
* Building simple real-world application logic

## 🚀 Future Improvements

Planned enhancements include:

* 🎲 Random question selection
* 🆘 Lifelines
* ⏱️ Timer for each question
* 🏆 Leaderboard
* 👤 Player profiles
* 🗄️ Database integration
* 🖥️ GUI using Tkinter
* 🧱 Object-Oriented Programming implementation
* 🌐 Web version using Django

## 👨‍💻 Author

**Mohan K**

Built as a Python project to strengthen programming fundamentals, problem-solving, and software development skills.

