import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

# Define global variables
root_first = None
background_label = None
original_image = None

def search_database(book_name, author):
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kavya@28245",
            database="booksdatabase"
        )
        cursor = db_connection.cursor()
        
        # Execute a SELECT query to search for the book
        cursor.execute("SELECT * FROM table_books WHERE book_name = %s AND author = %s", (book_name, author))
        row = cursor.fetchone()
        
        # Close cursor and connection
        cursor.close()
        db_connection.close()
        print("Database connection closed")
        
        if row:
            # If book found, display all values of that row
            display_data(row, book_name, author)
        else:
            # If book not found, show message box
            messagebox.showinfo("Book Not Found", f"The book '{book_name}' by '{author}' was not currently present in our Library.\nTHANK YOU🙏")
        
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to connect to the database: {error}")

def display_data(data, book_name, author):
    # Close the first window
    root_first.destroy()
    
    # Create the second window for displaying book details
    root_second = tk.Tk()
    root_second.title("Book Details")
    
     # Get the screen width and height
    screen_width = root_second.winfo_screenwidth()
    screen_height = root_second.winfo_screenheight()
    root_second.geometry(f"{screen_width}x{screen_height}+0+0")
    
    # Load background image
    background_image = Image.open("../assets/sanj2.jpg")
    background_image = background_image.resize((screen_width, screen_height))
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = tk.Label(root_second, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame
    frame = tk.Frame(root_second, bg="#e8c08c")
    frame.place(relx=0.3, rely=0.45, anchor="center")
    
    # Display all values of the row with larger font size and column names
    labels = [("Book ID", data[0]), 
              ("Book Name", data[1]), 
              ("Author", data[2]), 
              ("Genre", data[3]), 
              ("Number of Copies", data[4]), 
              ("Average Ratings", data[5]),
              ("Books Section", data[6])]  # Change this to the actual column name
              
    for i, (column_name, value) in enumerate(labels):
        label_name = tk.Label(frame, text=f"{column_name}:", bg="#e8c08c", fg="black", font=("Arial", 30))  # Adjust font size here
        label_name.grid(row=i, column=0, padx=(50,10), pady=10, sticky="w")
        label_value = tk.Label(frame, text=str(value), bg="#e8c08c", fg="black", font=("Arial", 30))  # Adjust font size here
        label_value.grid(row=i, column=1, padx=(10,50), pady=10, sticky="w")

    # Create a feedback button
    def display_feedback():
        root_second.destroy()  # Destroy second window
        show_feedback_page(book_name, author)  # Open feedback window
    btn_feedback = tk.Button(root_second, text="Feedback", command=display_feedback, font=("Arial", 15), bg="black", fg="white", width=10)
    btn_feedback.place(relx=0.8, rely=0.8, anchor="center")
    
    # Create a back button
    def go_back():
        root_second.destroy()
        show_first_page()
    btn_back = tk.Button(root_second, text="Back", command=go_back, font=("Arial", 15), bg="black", fg="white", width=10)
    btn_back.place(relx=0.2, rely=0.8, anchor="center")
    
    root_second.mainloop()

def show_feedback_page(book_name, author):
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kavya@28245",
            database="feedbackdb"
        )
        cursor = db_connection.cursor()
        
        # Execute a SELECT query to search for the feedback data
        cursor.execute("SELECT * FROM fbtable WHERE book_name = %s AND author = %s", (book_name, author))
        feedback_data = cursor.fetchall()
        
        # Close cursor and connection
        cursor.close()
        db_connection.close()
        print("Feedback database connection closed")
        
        if feedback_data:
            # If feedback data found, display in a new window
            display_feedback_data(feedback_data)
        else:
            # If no feedback found, show message box
            messagebox.showinfo("Feedback Not Found", f"No feedback available for the book '{book_name}' by '{author}'")
        
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to connect to the feedback database: {error}")



def display_feedback_data(feedback_data):
    # Create the feedback window
    feedback_window = tk.Tk()
    feedback_window.title("Feedback Data")

    # Get the screen width and height
    screen_width = feedback_window.winfo_screenwidth()
    screen_height = feedback_window.winfo_screenheight()
    feedback_window.geometry(f"{screen_width}x{screen_height}+0+0")
    
    # Load background image
    background_image = Image.open("../assets/sanj.jpg")
    background_image = background_image.resize((screen_width, screen_height))
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = tk.Label(feedback_window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame
    frame = tk.Frame(feedback_window, bg="#dedac5")
    frame.place(relx=0.3, rely=0.45, anchor="center")

    # Display feedback data
    for i, data in enumerate(feedback_data):
        for j, (column_name, value) in enumerate(zip(["Book Name", "Author", "Feedback1", "Feedback2", "Feedback3", "Feedback4", "Feedback5"], data)):
            label_name = tk.Label(frame, text=f"{column_name}:", bg="#dedac5", fg="black", font=("Arial", 30, "bold"))
            label_name.grid(row=i*7+j, column=0, padx=10, pady=10, sticky="w")
            label_value = tk.Label(frame, text=str(value), bg="#dedac5", fg="black", font=("Arial", 30))
            label_value.grid(row=i*7+j, column=1, padx=10, pady=10, sticky="w")      
    

    # Create "Give Feedback" label
    give_feedback_label = tk.Label(frame, text="Give Feedback:", bg="#dedac5", fg="black", font=("Arial", 30, "bold"))
    give_feedback_label.grid(row=len(feedback_data)*7, column=0, padx=10, pady=10, sticky="w")

    # Create entry box for feedback
    feedback_entry = tk.Entry(frame, font=("Arial", 30))
    feedback_entry.grid(row=len(feedback_data)*7, column=1, padx=10, pady=10, sticky="w")


    
    # Create "Enter" button
    enter_button = tk.Button(frame, text="Enter", command=lambda: enter_feedback(feedback_entry), font=("Arial", 25))
    enter_button.grid(row=len(feedback_data)*7, column=3, padx=10, pady=10, sticky="w")


     # Create exit button
    exit_button = tk.Button(frame, text="Exit", command=feedback_window.destroy, font=("Arial", 30))
    exit_button.grid(row=len(feedback_data)*7+1, columnspan=2, padx=10, pady=10)
    feedback_window.mainloop()
def enter_feedback(feedback_entry):
    feedback = feedback_entry.get()
    # Do something with the feedback, like saving it or processing it
    print("Feedback received:", feedback)

    

def show_first_page():
    global root_first, background_label, original_image
    # Create the main window for the first page
    root_first = tk.Tk()
    root_first.title("Book Search")

    # Load background image
    original_image = Image.open("../assets/sanj5.jpg")

    # Get the screen width and height
    screen_width = root_first.winfo_screenwidth()
    screen_height = root_first.winfo_screenheight()

    # Resize the image to fit the window
    resized_image = original_image.resize((screen_width, screen_height))

    # Convert Image object into Tkinter PhotoImage object
    background_image_tk = ImageTk.PhotoImage(resized_image)

    # Create a label with the background image
    background_label = tk.Label(root_first, image=background_image_tk)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Set the position of the window
    root_first.geometry(f"{screen_width}x{screen_height}+0+0")
        
    # Create a frame for the book name
    frame_book_name = tk.Frame(root_first)
    frame_book_name.pack(pady=(100, 20))  # Increased padding at the top to move downward

    # Book Name label and entry widget with padding
    label_book_name = tk.Label(frame_book_name, text="Book Name:", font=("Arial", 20))
    label_book_name.pack(side=tk.LEFT, padx=(10, 5))  # Added padding on the right side of the label

    entry_book_name = tk.Entry(frame_book_name, font=("Arial", 20))
    entry_book_name.pack(side=tk.LEFT, padx=(0, 10))  # Added padding on the left side of the entry

    # Create a frame for the Author
    frame_author = tk.Frame(root_first)
    frame_author.pack(pady=50)  # Increased padding at the top to move downward

    # Author label and entry widget with padding
    label_author = tk.Label(frame_author, text="Author:", font=("Arial", 20))
    label_author.pack(side=tk.LEFT, padx=(10, 5))  # Added padding on the right side of the label

    entry_author = tk.Entry(frame_author, font=("Arial", 20))
    entry_author.pack(side=tk.LEFT, padx=(0, 10)) 


    # Button to search the database
    btn_search = tk.Button(root_first, text="Search", command=lambda: search_database(entry_book_name.get(), entry_author.get()), bg="green", fg="white", font=("Arial", 20))
    btn_search.pack(pady=(screen_height//20, screen_height//10))

    # Bind the resize event
    root_first.bind("<Configure>", resize_image)

    root_first.mainloop()

def resize_image(event):
    global background_label, original_image
    window_width = event.width
    window_height = event.height
    resized_image = original_image.resize((window_width, window_height))
    resized_image_tk = ImageTk.PhotoImage(resized_image)
    background_label.config(image=resized_image_tk)
    background_label.image = resized_image_tk

if __name__ == "__main__":
    show_first_page()
