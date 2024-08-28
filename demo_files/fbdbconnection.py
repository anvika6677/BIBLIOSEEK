import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kavya@28245",
    database="feedbackdb"
)
root = Tk()
root.title("Feedback Display")
root.geometry("600x400")
def display_feedback():
    # Get the book name and author from the entry widgets
    book_name = book_name_entry.get()
    author = author_entry.get()
    
    # Create a cursor to execute SQL queries
    cursor = db_connection.cursor()
    
    # Execute SQL query to fetch feedback data for the given book and author
    cursor.execute("SELECT * FROM fbtable WHERE book_name = %s AND author = %s", (book_name, author))
    
    # Fetch the results
    feedback_data = cursor.fetchone()
    
    # Close the cursor
    cursor.close()
    
    # Display feedback data in labels
    if feedback_data:
        feedback1_label.config(text="Feedback 1: " + feedback_data[2])
        feedback2_label.config(text="Feedback 2: " + feedback_data[3])
        feedback3_label.config(text="Feedback 3: " + feedback_data[4])
        feedback4_label.config(text="Feedback 4: " + feedback_data[5])
        feedback5_label.config(text="Feedback 5: " + feedback_data[6])
    else:
        feedback1_label.config(text="No feedback found for this book and author")
# Create entry widgets
book_name_entry = Entry(root, width=30)
book_name_entry.pack()
book_name_entry.insert(0, "Enter Book Name")

author_entry = Entry(root, width=30)
author_entry.pack()
author_entry.insert(0, "Enter Author Name")

# Create a button to trigger feedback display
search_button = Button(root, text="Search Feedback", command=display_feedback)
search_button.pack()
# Create labels to display feedback data
feedback1_label = Label(root, text="")
feedback1_label.pack()

feedback2_label = Label(root, text="")
feedback2_label.pack()

feedback3_label = Label(root, text="")
feedback3_label.pack()

feedback4_label = Label(root, text="")
feedback4_label.pack()

feedback5_label = Label(root, text="")
feedback5_label.pack()
root.mainloop()
