import tkinter as tk
from PIL import Image, ImageTk
import loginpage

def open_login_page():
    root.destroy()  # Close cover page
    loginpage.show_login_page()  # Open login page

def main():
    global root
    root = tk.Tk()
    root.title("Image Placement")

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Load images
    image1 = Image.open("../assets/sanj6.jpg")
    image2 = Image.open("../assets/san.jpg")

    # Resize image2 to match the screen dimensions
    image2 = image2.resize((screen_width, screen_height))

    # Resize image1
    image1 = image1.resize((int(screen_width * 0.3), int(screen_height * 0.3)))  # Resize image1 to 30% of screen width and height

    # Calculate the position to place image1 at the middle of the top of image2
    x_center = (screen_width - image1.width) // 2
    y_center = int(screen_height * 0.1)  # Position image1 at 10% of the screen height from the top

    # Create a new image by pasting image1 onto image2
    image2.paste(image1, (x_center, y_center))

    # Convert the final image to a Tkinter PhotoImage object
    final_image_tk = ImageTk.PhotoImage(image2)

    # Create a label to display the final image
    label = tk.Label(root, image=final_image_tk)
    label.pack()

    # Create a label below image1 with a gap and brown background
    gap = 50  # Adjust the gap as needed
    text_label = tk.Label(root, text="WELCOME BOOK SEEKER!!", font=("Helvetica", 30, "bold"), bg="Sienna")
    text_label.place(x=x_center - 40, y=y_center + image1.height + gap)  # Adjust the y-coordinate and gap as needed
    text_label.update_idletasks()  # Ensure the label is properly placed - a method that processes all pending events and updates the GUI immediately.

    # Create a button below the label
    button = tk.Button(root, text="Let's Go", font=("Helvetica", 16), bg="grey", fg="white", command=open_login_page)
    button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  # Position the button at the bottom center
    button.update_idletasks()  # Ensure the button is properly placed

    root.mainloop()

if __name__ == "__main__":
    main()
