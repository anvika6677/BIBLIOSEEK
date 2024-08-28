import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import first_window

# Define global variables
root_login = None
original_image = None
background_label = None
entry_username = None
entry_password = None

def validate_login():
    global root_login
    # Get username and password from entry widgets
    username = entry_username.get()
    password = entry_password.get()

    # Connect to MySQL database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kavya@28245",
            database="loginpage"
        )

        cursor = connection.cursor()

        # Query database for user
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            print(user)
            messagebox.showinfo("Success", "Login Successful!")
            root_login.destroy()  # Close login window
            first_window.show_first_page()  # Open book details page
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to connect to database: {error}")

    finally:
        # Close database connection
        if 'connection' in locals() or 'connection' in globals():
            if connection.is_connected():
                cursor.close()
                connection.close()

def resize_image(event):
    # Update window width and height
    global window_width, window_height
    window_width = max(event.width, 500)  # Increased minimum width to 500
    window_height = max(event.height, 500)  # Increased minimum height to 400

    # Resize the image to fit the window
    resized_image = original_image.resize((window_width, window_height))
    new_image = ImageTk.PhotoImage(resized_image)
    background_label.config(image=new_image)
    background_label.image = new_image

# Create the main window for login page
def show_login_page():
    global root_login, original_image, background_label, entry_username, entry_password

    root_login = tk.Tk()
    root_login.title("Login")

    # Set initial window size
    window_width = 500  # Increased initial width
    window_height = 500  # Increased initial height

    # Set minimum window size
    root_login.minsize(500, 500)  

    # Load background image
    original_image = Image.open("C:/Users/LENOVO/Desktop/wise/assets/sanj4.jpg")  
    resized_image = original_image.resize((window_width, window_height))
    background_photo = ImageTk.PhotoImage(resized_image)

    # Create a label with the background image
    background_label = tk.Label(root_login, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Bind the resize event
    root_login.bind("<Configure>", resize_image)

    # Define very light brown color aesthetic background
    bg_color = "#ab8572"  # Very light brown

    # Create a frame to hold the widgets
    frame = tk.Frame(root_login, bg=bg_color, bd=5, relief=tk.FLAT, width=400, height=600)  # Increased frame width and height
    frame.place(relx=0.1, rely=0.5, anchor=tk.W)  # Positioned towards the left

    # Create labels and entry widgets for username
    label_username = tk.Label(frame, text="Username", font=("Helvetica", 23), fg="black", bg=bg_color)
    label_username.grid(row=0, column=0, pady=5, sticky="w")

    entry_username = tk.Entry(frame, font=("Helvetica", 23))
    entry_username.grid(row=1, column=0, pady=5)

    # Create labels and entry widgets for password
    label_password = tk.Label(frame, text="Password", font=("Helvetica", 23), fg="black", bg=bg_color)
    label_password.grid(row=2, column=0, pady=5, sticky="w")

    entry_password = tk.Entry(frame, show="*", font=("Helvetica", 23))
    entry_password.grid(row=3, column=0, pady=5)

    # Create a login button
    login_button = tk.Button(frame, text="Login", font=("Helvetica", 23, "bold"), bg="#D2B48C", fg="black", command=validate_login, bd=0, width=10)
    login_button.grid(row=4, column=0, pady=20)

    # Run the Tkinter event loop for login page
    root_login.mainloop()

if __name__ == "__main__":
    show_login_page()
    