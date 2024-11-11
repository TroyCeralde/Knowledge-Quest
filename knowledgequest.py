import tkinter as tk
from tkinter import ttk, messagebox  # Import messagebox for displaying pop-up messages
from ttkbootstrap import Style  # Ensure you have ttkbootstrap installedonaries
import random

# Set a constant for the maximum number of questions displayed
MAX_QUESTIONS = 25


knowledge_data = [
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Au", "Ag", "Fe", "Pb"],
        "answer": "Au"
    },
    {
        "question": "Which scientist developed the theory of relativity?",
        "choices": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Marie Curie"],
        "answer": "Albert Einstein"
    },
    {
        "question": "What type of wave is produced by an earthquake?",
        "choices": ["Sound waves", "Light waves", "Seismic waves", "Radio waves"],
        "answer": "Seismic waves"
    },
    {
        "question": "What is the boiling point of water at sea level in degrees Celsius?",
        "choices": ["90 degrees Celsius", "100 degrees Celsius", "110 degrees Celsius", "120 degrees Celsius"],
        "answer": "100 degrees Celsius"
    },
    {
        "question": "Which planet is closest in size to Earth?",
        "choices": ["Mars", "Venus", "Mercury", "Jupiter"],
        "answer": "Venus"
    },
    {
        "question": "Which planet has the most volcanoes?",
        "choices": ["Mars", "Venus", "Earth", "Saturn"],
        "answer": "Venus"
    },
    {
        "question": "Which is the densest planet in our solar system?",
        "choices": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Earth"
    },
    {
        "question": "In which country would you find the Leaning Tower of Pisa?",
        "choices": ["Italy", "France", "Spain", "Greece"],
        "answer": "Italy"
    },
    {
        "question": "What is a group of lions called?",
        "choices": ["Herd", "Pack", "Pride", "Gaggle"],
        "answer": "Pride"
    },
    {
        "question": "Which bird is the symbol of peace?",
        "choices": ["Eagle", "Dove", "Pigeon", "Sparrow"],
        "answer": "Dove"
    },
    {
        "question": "Which is the only mammal that can fly?",
        "choices": ["Bat", "Bird", "Squirrel", "Flying Fish"],
        "answer": "Bat"
    },
    {
        "question": "Which bird is known to be the fastest bird?",
        "choices": ["Peregrine Falcon", "Eagle", "Hawk", "Ostrich"],
        "answer": "Peregrine Falcon"
    },
    {
        "question": "The United States consists of how many states?",
        "choices": ["48", "50", "51", "52"],
        "answer": "50"
    },
    {
        "question": "Which is the hottest continent on Earth?",
        "choices": ["Asia", "Africa", "Australia", "South America"],
        "answer": "Africa"
    },
    {
        "question": "Which continent is known as the Dark Continent?",
        "choices": ["Africa", "Asia", "Europe", "America"],
        "answer": "Africa"
    },
    {
        "question": "Which is the most populous city in the United Kingdom which is also its capital city?",
        "choices": ["Birmingham", "London", "Manchester", "Liverpool"],
        "answer": "London"
    },
    {
        "question": "In which year did the Titanic sink?",
        "choices": ["1905", "1912", "1920", "1935"],
        "answer": "1912"
    },
    {
        "question": "Which is the tallest and heaviest bird in the world?",
        "choices": ["Ostrich", "Eagle", "Penguin", "Albatross"],
        "answer": "Ostrich"
    },
    {
        "question": "How many hearts does an octopus have?",
        "choices": ["1", "2", "3", "4"],
        "answer": "3"
    },
    {
        "question": "Which animal spends almost the entire day, every day, sleeping?",
        "choices": ["Cat", "Sloth", "Koala", "Dog"],
        "answer": "Koala"
    },
    {
        "question": "What is the name of a baby goat?",
        "choices": ["Kid", "Calf", "Puppy", "Cub"],
        "answer": "Kid"
    },
    {
        "question": "Which country celebrates the Day of the Dead?",
        "choices": ["Spain", "Mexico", "Brazil", "Argentina"],
        "answer": "Mexico"
    },
    {
        "question": "What do we carve on Halloween?",
        "choices": ["Pumpkin", "Apple", "Carrot", "Cucumber"],
        "answer": "Pumpkin"
    },
    {
        "question": "Which country sent the Statue of Liberty to the USA as a gift?",
        "choices": ["France", "Germany", "Italy", "Spain"],
        "answer": "France"
    },
    {
        "question": "How many continents are on planet Earth?",
        "choices": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Who was the very first president of the United States of America?",
        "choices": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
        "answer": "George Washington"
    },
    {
        "question": "Which continent is the largest?",
        "choices": ["Africa", "Asia", "North America", "Europe"],
        "answer": "Asia"
    },
    {
        "question": "Which country is the largest?",
        "choices": ["China", "Canada", "Russia", "United States"],
        "answer": "Russia"
    },
    {
        "question": "How many commandments are there?",
        "choices": ["5", "8", "10", "12"],
        "answer": "10"
    },
    {
        "question": "What is the first book in the Bible?",
        "choices": ["Genesis", "Exodus", "Leviticus", "Numbers"],
        "answer": "Genesis"
    },
    {
        "question": "Who was the first man created by God?",
        "choices": ["Adam", "Noah", "Moses", "Abraham"],
        "answer": "Adam"
    },
    {
        "question": "How many days did God create the world?",
        "choices": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "How many days did Noah live on the ark?",
        "choices": ["30", "40", "50", "60"],
        "answer": "40"
    },
    {
        "question": "What is a shape with eight sides called?",
        "choices": ["Hexagon", "Octagon", "Decagon", "Triangle"],
        "answer": "Octagon"
    },
    {
        "question": "What is the top number of a fraction called?",
        "choices": ["Denominator", "Numerator", "Factor", "Dividend"],
        "answer": "Numerator"
    },
    {
        "question": "How many lives are cats said to have?",
        "choices": ["7", "8", "9", "10"],
        "answer": "9"
    },
    {
        "question": "How many years to complete a decade?",
        "choices": ["5", "10", "15", "20"],
        "answer": "10"
    },
    {
        "question": "If Rachel has 16 crayons, Anna has 20 crayons, and Cory has 10 crayons, then how many crayons are there in total?",
        "choices": ["40", "45", "50", "46"],
        "answer": "46"
    },
    {
        "question": "Ray bought 10 apples and 5 oranges. If Mike bought 6 apples and 9 oranges, then how many oranges did Ray and Mike buy in total?",
        "choices": ["10", "12", "14", "16"],
        "answer": "14"
    },
    {
        "question": "Mom bought 20 books for her children: Mary, Zack, and Jane. If Mary got 6 books and Jane got 7 books, then how many books does Zack get?",
        "choices": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "There are 15 kids in Ms. Kayla's class. If each child receives 2 books, then how many books are there in total?",
        "choices": ["28", "30", "32", "34"],
        "answer": "30"
    },
    {
        "question": "The jackpot of the arcade ball game gives out 50 tickets. If Archie hit the jackpot 3 times, then how many tickets does Archie get?",
        "choices": ["100", "150", "200", "250"],
        "answer": "150"
    },
    {
        "question": "Scott has 28 chocolate bars. If he wants to divide it evenly between his 4 friends, then how many chocolate bars does each friend get?",
        "choices": ["6", "7", "8", "9"],
        "answer": "7"
    },
    {
        "question": "What vegetable is orange, grows underground, and is a good source of vitamin A?",
        "choices": ["Carrot", "Potato", "Pumpkin", "Sweet Potato"],
        "answer": "Carrot"
    },
    {
        "question": "An animal that only consumes another animal is called?",
        "choices": ["Herbivore", "Carnivore", "Omnivore", "Scavenger"],
        "answer": "Carnivore"
    },
    {
        "question": "In which town was Jesus born?",
        "choices": ["Nazareth", "Bethlehem", "Jerusalem", "Capernaum"],
        "answer": "Bethlehem"
    },
    {
        "question": "Who built the pyramids?",
        "choices": ["Greeks", "Romans", "Egyptians", "Mayans"],
        "answer": "Egyptians"
    },
    {
        "question": "In which country is Hindi spoken?",
        "choices": ["India", "Nepal", "Bangladesh", "Pakistan"],
        "answer": "India"
    },
    {
        "question": "What kind of transportation has four wheels, a steering wheel, and an engine?",
        "choices": ["Bicycle", "Car", "Train", "Boat"],
        "answer": "Car"
    },
    {
        "question": "What kind of building is tall and has many floors?",
        "choices": ["House", "Skyscraper", "Villa", "Cottage"],
        "answer": "Skyscraper"
    },
]


# Function to display the welcome screen
def show_welcome():
    welcome_label.config(text="Hello there and welcome to Knowledge Quest\nAre you ready to take the quiz?")
    start_button.pack(pady=20)
    quit_button.pack(pady=10)  # Show quit button on the welcome screen

# Function to start the quiz
def start_quiz():
    welcome_frame.pack_forget()  # Hide the welcome screen
    quiz_frame.pack(fill=tk.BOTH, expand=True)  # Show the quiz screen
    reset_quiz()  # Reset the quiz data before starting
    show_question()  # Show the first question

# Function to exit the quiz
def quit_quiz():
    messagebox.showinfo("Thank You!", "Thank you, come back another time!")
    root.quit()

# This function is to display the current question and choices
def show_question():
    # Ensure current_question is within bounds
    if current_question >= len(knowledge_data):
        print("All questions answered!")  # Debugging line to check if all questions are exhausted
        return
    
    # Get the current question from the knowledge data
    question = knowledge_data[current_question]
    print(f"Displaying question: {question['question']}")  # Debugging line
    
    # Update the question label with the current question
    qs_label.config(text=question["question"])  # This should set the question text
    print(f"Question displayed: {qs_label.cget('text')}")  # Debugging line to confirm
    
    # Get the choices for the question and update the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")  # Update buttons with choices
    
    # Reset feedback label and next button
    feedback_label.config(text="")  # Clear feedback label
    next_btn.config(state="disabled")  # Disable the next button
    exit_btn.pack(pady=10)  # Show exit button during quiz

# Function to check the selected answer and provide feedback
def check_answer(choice):
    global score, wrong_answers
    question = knowledge_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        score += 1
        score_label.config(text="Score: {}/{}".format(score, MAX_QUESTIONS))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        wrong_answers += 1
        feedback_label.config(text="Incorrect! Correct answer: {}".format(question["answer"]), foreground="red")

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal") 

    if wrong_answers >= 3:
        end_quiz("You've answered 3 questions incorrectly. Quiz over!")
    elif score >= MAX_QUESTIONS:
        end_quiz("Congratulations! You've answered {} questions correctly and passed!".format(score))

# Function to move to the next question         
def next_question():
    global current_question
    current_question += 1
    
    if current_question < MAX_QUESTIONS:  # Limit to 25 questions
        show_question()
    else:
        end_quiz("Quiz completed! Final score: {}/{}".format(score, MAX_QUESTIONS))

# Function to end the quiz with a custom frame for "Play Again" option
def end_quiz(message):
    # Hide the quiz question frame and show the play again options
    quiz_frame.pack_forget()  # Hide quiz frame
    
    # Show the welcome-style frame for the end screen
    end_frame.pack(fill=tk.BOTH, expand=True)
    
    # Display the final message
    final_message_label.config(text=message)
    final_message_label.pack(pady=20)

    # Show the "Do you want to play again?" message with Yes/No buttons
    play_again_label.pack(pady=10)
    play_again_button.pack(pady=10)
    quit_button_after_quiz.pack(pady=10)

# Function to reset the quiz for a new round
def reset_quiz():
    global score, wrong_answers, current_question, knowledge_data
    score = 0
    wrong_answers = 0
    current_question = 0
    
    # Shuffle the questions for a different quiz experience
    random.shuffle(knowledge_data)  # This will shuffle the question order each time
    score_label.config(text="Score: 0/{}".format(MAX_QUESTIONS))

    # Reset feedback (ensure no incorrect answers are shown)
    feedback_label.config(text="")

    # Reset buttons to be active
    for button in choice_btns:
        button.config(state="normal")

# Function to handle the "Play Again" button click
def play_again():
    # Reset the final screen and show the quiz again
    end_frame.pack_forget()  # Hide end screen
    quiz_frame.pack(fill=tk.BOTH, expand=True)  # Show quiz frame
    reset_quiz()  # Reset and show the first question again

# Function to handle the "Quit" button click after the quiz ends
def quit_after_quiz():
    final_message_label.config(text="Thanks for answering the quiz!")
    play_again_label.pack_forget()
    play_again_button.pack_forget()
    quit_button_after_quiz.pack_forget()

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

# --- Quiz Screen Frame ---
# Creating the quiz frame to hold questions and answers
quiz_frame = ttk.Frame(root, padding=20)
quiz_frame.pack_forget()  # Initially hidden

# This is to create the question label with larger font size
qs_label = ttk.Label(quiz_frame, anchor="center", wraplength=500, padding=10, font=("Helvetica", 24))

# Pack the question label into the quiz frame
qs_label.pack(pady=10)

# Creating the choices buttons with larger font size
choice_btns = []
for i in range(4):
    button = ttk.Button(quiz_frame, command=lambda i=i: check_answer(i), style='secondary.TButton', width=20)
    button.pack(pady=10)
    choice_btns.append(button)

# Creating the feedback label with larger font size
feedback_label = ttk.Label(quiz_frame, anchor="center", padding=10, font=("Helvetica", 20))
feedback_label.pack(pady=10)

# Initialize score and wrong answers
score = 0   
wrong_answers = 0

# Creating the scoring label with larger font size
score_label = ttk.Label(quiz_frame, text="Score: 0/{}".format(MAX_QUESTIONS), anchor="center", padding=10, font=("Helvetica", 24))
score_label.pack(pady=10)

# Creating the next button with larger font size
next_btn = ttk.Button(quiz_frame, text="Next", command=next_question, state="disabled", style='info.TButton', width=20)
next_btn.pack(pady=10)

# Creating the exit button for the quiz
exit_btn = ttk.Button(quiz_frame, text="Exit", command=quit_quiz, style='danger.TButton', width=20)

# Initialize the current question
current_question = 0

# Create a frame for the end screen similar to the welcome screen
end_frame = ttk.Frame(root, padding=20)
end_frame.pack_forget()  # Initially hidden
end_frame.configure(style='info.TFrame')

# New Labels and Buttons for the "Play Again" screen
final_message_label = ttk.Label(end_frame, anchor="center", wraplength=500, font=("Helvetica", 20))
play_again_label = ttk.Label(end_frame, text="Do you want to play again?", font=("Helvetica", 18))
play_again_button = ttk.Button(end_frame, text="Yes", command=play_again, style='success.TButton', width=20)
quit_button_after_quiz = ttk.Button(end_frame, text="No", command=quit_after_quiz, style='danger.TButton', width=20)

# Show the welcome screen
show_welcome()

# Start the main event loop
root.mainloop()
