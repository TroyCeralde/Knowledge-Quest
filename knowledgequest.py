import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkbootstrap import Style  # Ensure you have ttkbootstrap installed
from quiz_data import quiz_data  # Assuming quiz_data is a list of dictionaries

# Function to display the welcome screen
def show_welcome():
    welcome_label.config(text="Hello there and welcome to Knowledge Quest\nAre you ready to take the quiz?")
    start_button.pack(pady=20)
    quit_button.pack(pady=20)

# Function to start the quiz
def start_quiz():
    welcome_frame.pack_forget()  # Hide the welcome screen
    show_question()  # Show the first question

# Function to exit the quiz
def quit_quiz():
    root.destroy()

# This function is to display the current question and choices
def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])
    
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    global score, wrong_answers
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        wrong_answers += 1
        feedback_label.config(text="Incorrect! Correct answer: {}".format(question["answer"]), foreground="red")

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal") 

    if wrong_answers >= 3:
        end_quiz("You've answered 3 questions incorrectly. Quiz over!")
    elif score >= 25:
        end_quiz("Congratulations! You've answered 25 questions correctly and passed!")

# Function to move to the next question         
def next_question():
    global current_question
    current_question += 1
    
    if current_question < len(quiz_data):
        show_question()
    else:
        end_quiz("Quiz completed! Final score: {}/{}".format(score, len(quiz_data)))

# Function to end the quiz
def end_quiz(message):
    messagebox.showinfo("Quiz Finished", message)
    root.destroy()    

# This is to create the main window 
root = tk.Tk()
root.title("Knowledge Quest")
root.geometry("600x500")
style = Style(theme="flatly")

# Creating a frame for the welcome screen with a background color
welcome_frame = ttk.Frame(root, padding=20)
welcome_frame.pack(fill=tk.BOTH, expand=True)
welcome_frame.configure(style='info.TFrame')

# Welcome label with larger font size
welcome_label = ttk.Label(welcome_frame, anchor="center", wraplength=500, font=("Helvetica", 28))
welcome_label.pack(pady=20)

# Start quiz button with larger font size
start_button = ttk.Button(welcome_frame, text="Yes", command=start_quiz, style='primary.TButton', width=20)
start_button.pack(pady=10)

# Quit button with larger font size
quit_button = ttk.Button(welcome_frame, text="No", command=quit_quiz, style='danger.TButton', width=20)
quit_button.pack(pady=10)

# This is to create the question label with larger font size
qs_label = ttk.Label(root, anchor="center", wraplength=500, padding=10, font=("Helvetica", 24))
qs_label.pack(pady=10)

# Creating the choices buttons with larger font size
choice_btns = []
for i in range(4):
    button = ttk.Button(root, command=lambda i=i: check_answer(i), style='secondary.TButton', width=20)
    button.pack(pady=10)
    choice_btns.append(button)

# Creating the feedback label with larger font size
feedback_label = ttk.Label(root, anchor="center", padding=10, font=("Helvetica", 20))
feedback_label.pack(pady=10)

# Initialize score and wrong answers
score = 0   
wrong_answers = 0

# Creating the scoring label with larger font size
score_label = ttk.Label(root, text="Score: 0/{}".format(len(quiz_data)), anchor="center", padding=10, font=("Helvetica", 24))
score_label.pack(pady=10)

# Creating the next button with larger font size
next_btn = ttk.Button(root, text="Next", command=next_question, state="disabled", style='info.TButton', width=20)
next_btn.pack(pady=10)

# Initialize the current question
current_question = 0

# Show the welcome screen
show_welcome()

# Start the main event loop
root.mainloop()
