#!/usr/bin/python

#Import Statements
import tkinter
import csv
import random
from PIL import ImageTk, Image

#Assign Variables
answer = {}
question = ''
counter = 1
csv_reader = {}
list_of_column_names = []
disorder = ''
result = ''

#Initialise GUI and Add Elements using Grid Table-Like Positioning and Assign Buttons A Defined Function as a Command and Creating Images
window = tkinter.Tk()
window.title('Current Mood Guesser')
heading_label = tkinter.Label(window, text='Welcome to the Current Mood Guesser Game. Please start by answering the questions below: ')        
heading_label.grid(row = 0, column = 0, columnspan = 25)
question_label = tkinter.Label(window)
question_label.grid(row = 1, column = 0, columnspan = 25)

happy_face = (Image.open("happyface.png"))
resized_happy_face = happy_face.resize((100,100), Image.ANTIALIAS)
new_happy_face = ImageTk.PhotoImage(resized_happy_face)

sad_face = (Image.open("sadface.png"))
resized_sad_face = sad_face.resize((100,100), Image.ANTIALIAS)
new_sad_face = ImageTk.PhotoImage(resized_sad_face)

answer_label = tkinter.Label(window)
answer_label.grid(row = 2, column = 0, columnspan = 25)
yes_button = tkinter.Button(window, text='Yes', width=25, command=lambda: answer_question(question, 'yes'))
no_button = tkinter.Button(window, text='No', width=25, command=lambda: answer_question(question, 'no'))
yes_button.grid(row = 3, column = 0, padx = 25, pady = 25)
no_button.grid(row = 3, column = 1, padx = 25, pady = 25)

#Loop through CSV File Dataset and read as a Dictionary and then get the headings (Questions) as a List and setup the first Question to be displayed Randomly
with open('dataset.csv', 'r') as csv_file:
    csv_reader_x = csv_file.readlines()

csv_reader_y = csv.DictReader(csv_reader_x)

dict_from_csv = dict(list(csv_reader_y)[0])

# making a list from the keys of the dict
list_of_column_names = list(dict_from_csv.keys())

csv_reader = csv.DictReader(csv_reader_x)

question = random.choice(list_of_column_names)
question_formatted = question
question_formatted = question_formatted.replace('.', ' ').title() + '?'
list_of_column_names.remove(question)
list_of_column_names.remove('Disorder')
question_label.configure(text=question_formatted)

#Function to be Assigned when Buttons are Clicked
def answer_question(label_text, selected_answer):
    #Define Parameters again as Global so that they can maintain the value if modified in function
    global answer
    global question
    global counter
    global list_of_column_names
    global csv_reader
    global disorder
    global result
    
    #Check if List contains anymore Questions and display them in a Random Order, removing the previously displayed Question and store the selected Answer and Question into a Dictionary
    if len (list_of_column_names) > 0:
        question = label_text
        answer[question] = selected_answer
        question = random.choice(list_of_column_names)
        list_of_column_names.remove(question)
        question_formatted = question
        question_formatted = question_formatted.replace('.', ' ').title() + '?'
        question_label.configure(text=question_formatted)
    
    #Check if List does not contain anymore Questions match Dictionary against the Dictionary containing all possible matches.
    #If the selected Answers are a Subset of the original Dictionary then print out the current Mood, otherwise display a different message
    if len(list_of_column_names) == 0:
        for row in csv_reader:
            if answer.items() <= row.items():
                disorder = row['Disorder']
                result = 'Your current mood is: ' + row['Disorder']
            else:
                disorder = ''
                result = 'Sorry, could not determine your current mood at the moment.'
        heading_label.configure(text='Game Over.')
        question_label.configure(text=result)
        if disorder == 'Normal':
            answer_label.configure(image=new_happy_face)
        else:
            answer_label.configure(image=new_sad_face)
#Run and Display the Window
window.mainloop()
