from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import datetime
import random

# Create a database connection
conn = sqlite3.connect("hotel_rooms.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the rooms table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS rooms (
    room_number INTEGER PRIMARY KEY,
    type TEXT,
    status TEXT,
    cost_per_day INTEGER,
    capacity INTEGER
)
""")

# Create the bookings table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    booking_id TEXT PRIMARY KEY,
    room_number INTEGER,
    customer_id TEXT,
    check_in_date TEXT,
    check_out_date TEXT,
    total_price INTEGER,
    FOREIGN KEY (room_number) REFERENCES rooms(room_number)
)
""")

# Create the customers table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    dob TEXT,
    address TEXT,
    phone TEXT
)
""")

# Delete existing data from the rooms table
cursor.execute("DELETE FROM rooms")

# Insert sample data into the rooms table
sample_data = [
    (101, 'Single beded', 'Available', 1500, 1),
    (103, 'Double beded', 'Available', 2500, 2),
    (104, 'Single beded', 'Available', 1500, 1),
    (107, 'Double beded', 'Available', 4000, 2),
    (109, 'Triple beded', 'Available', 4000, 3),
    (202, 'Single beded', 'Available', 1500, 1),
    (204, 'Double beded', 'Available', 2500, 2),
    (206, 'Single beded', 'Available', 1500, 1),
    (207, 'Double beded', 'Available', 2500, 2),
    (208, 'Triple beded', 'Available', 4000, 3),
    (301, 'Single beded', 'Available', 1500, 1),
    (303, 'Double beded', 'Available', 2500, 2),
    (305, 'Single beded', 'Available', 1500, 1),
    (308, 'Double beded', 'Available', 2500, 2),
    (309, 'Triple beded', 'Available', 4000, 3)
]

cursor.executemany("INSERT INTO rooms (room_number, type, status, cost_per_day, capacity) VALUES (?, ?, ?, ?, ?)", sample_data)

conn.commit()  # Commit the changes

def destroy_window(window):
    window.destroy()

def generate_short_id():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=6))

def main_page():
    def logout():
        main_window.destroy()

    def customer_details_window():
        def save_customer_details():
            customer_name = name_entry.get()
            customer_dob = dob_entry.get()
            customer_address = address_entry.get()
            customer_phone = phone_entry.get()
            
            if customer_name and customer_dob and customer_phone:
                print("Customer Name:", customer_name)
                print("Customer Date of Birth:", customer_dob)
                print("Customer Address:", customer_address)
                print("Customer Phone:", customer_phone)
                save_message.config(text="Saved Successfully!")
            else:
                save_message.config(text="Please Enter all the information!")

        customer_window = Toplevel(main_window)
        customer_window.title("Customer Details")
        customer_window.geometry("1550x800")
        customer_window.configure(bg="peach puff")
        customer_window.protocol("WM_DELETE_WINDOW", lambda: destroy_window(customer_window))

        # Heading
        customer_heading_label = Label(customer_window, text="Customer Details", font=("Times New Roman", 24, "bold"), bg="peach puff")
        customer_heading_label.pack(pady=20)

        name_label = Label(customer_window, text="Name:", font=("Times New Roman", 16, "bold"), bg="peach puff")
        name_label.place(relx=0.5, rely=0.20, anchor=CENTER)
        name_entry = Entry(customer_window, font=("Times New Roman", 14, "bold"))
        name_entry.place(relx=0.5, rely=0.25, anchor=CENTER)

        dob_label = Label(customer_window, text="Date of Birth:", font=("Times New Roman", 16, "bold"), bg="peach puff")
        dob_label.place(relx=0.5, rely=0.30, anchor=CENTER)
        dob_entry = Entry(customer_window, font=("Times New Roman", 14, "bold"))
        dob_entry.place(relx=0.5, rely=0.35, anchor=CENTER)

        address_label = Label(customer_window, text="Address:", font=("Times New Roman", 16, "bold"), bg="peach puff")
        address_label.place(relx=0.5, rely=0.40, anchor=CENTER)
        address_entry = Entry(customer_window, font=("Times New Roman", 14, "bold"))
        address_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

        phone_label = Label(customer_window, text="Phone:", font=("Times New Roman", 16, "bold"), bg="peach puff")
        phone_label.place(relx=0.5, rely=0.50, anchor=CENTER)
        phone_entry = Entry(customer_window, font=("Times New Roman", 14, "bold"))
        phone_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

        save_button = Button(customer_window, text="Save", command=save_customer_details, width=10, height=2, font=("Times New Roman", 14), bg="black", fg="gold")
        save_button.place(relx=0.5, rely=0.65, anchor=CENTER)

        save_message = Label(customer_window, text="", font=("Times New Roman", 14, "bold"), bg="peach puff")
        save_message.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Back Button
        back_button = Button(customer_window, text="Back", command=lambda: destroy_window(customer_window), width=10, height=2, font=("Times New Roman", 12, "bold"), bg="black", fg="gold")
        back_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    def hotel_details_page():
        hotel_details_window = Toplevel(main_window)
        hotel_details_window.title("Hotel Details")
        hotel_details_window.geometry("1550x800")
        hotel_details_window.configure(bg="peach puff")  # Set background color
        hotel_details_window.protocol("WM_DELETE_WINDOW", lambda: destroy_window(hotel_details_window))

        # Heading
        hotel_details_label = Label(hotel_details_window, text="Hotel Details", font=("Times New Roman", 24, "bold"), bg="peach puff")
        hotel_details_label.pack(pady=20)

        hotel_info = "Hotel ID: 1000\nName: Annex Hotel\nAddress: Rd no 7, Andheri East, Mumbai, Maharashtra,pincode:400069\nPhone: 08823 69876\nEmail: annex2018@gmail.com"
        hotel_info_label = Label(hotel_details_window, text=hotel_info, font=("Times New Roman", 16), bg="peach puff")
        hotel_info_label.pack()

        # Back Button
        back_button = Button(hotel_details_window, text="Back", command=lambda: destroy_window(hotel_details_window), width=10, height=2, font=("Times New Roman", 12, "bold"), bg="black", fg="gold")
        back_button.pack(pady=20)

    def room_details_window():
        def refresh_room_details():
            room_tree.delete(*room_tree.get_children())
            cursor.execute("SELECT * FROM rooms")
            rooms_data = cursor.fetchall()
            for row in rooms_data:
                room_tree.insert("", "end", values=row)

        room_window = Toplevel(main_window)
        room_window.title("Room Details")
        room_window.geometry("1550x800")
        room_window.configure(bg="peach puff")  #background color
        room_window.protocol("WM_DELETE_WINDOW", lambda: destroy_window(room_window))

        # Heading
        room_heading_label = Label(room_window, text="Room Details", font=("Times New Roman", 24, "bold"), bg="peach puff")
        room_heading_label.pack(pady=20)

        # Retrieve room data from the database
        cursor.execute("SELECT * FROM rooms")
        rooms_data = cursor.fetchall()

        # Create a treeview to display room data
        room_tree = ttk.Treeview(room_window, columns=("Room Number", "Type", "Status", "Cost per Day", "Capacity"), height=15)
        room_tree.heading("Room Number", text="Room Number")
        room_tree.heading("Type", text="Type")
        room_tree.heading("Status", text="Status")
        room_tree.heading("Cost per Day", text="Cost per Day")
        room_tree.heading("Capacity", text="Capacity")
        room_tree.pack()

        # Insert room data into the treeview
        for row in rooms_data:
            room_tree.insert("", "end", values=row)

        # Back button
        back_button = Button(room_window, text="Back", command=room_window.destroy, width=5, height=1, font=("Times New Roman", 14, "bold"), bg="black", fg="gold")
        back_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    def booking_window(main_window):
        def book_room():
            room_no = room_no_entry.get()
            check_in_date = check_in_entry.get()
            check_out_date = check_out_entry.get()

            # Fetch cost per day from the database based on the selected room number
            cursor.execute("SELECT cost_per_day FROM rooms WHERE room_number = ?", (room_no,))
            result = cursor.fetchone()
            if result is not None:  # Check if result is not None
                cost_per_day = result[0]  # Access index [0] if result is not None

                # Calculate total price based on the cost per day and duration of stay
                try:
                    check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
                    check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
                    duration_of_stay = (check_out - check_in).days
                    total_price = duration_of_stay * cost_per_day
                    total_price_label.config(text="Total Price: $" + str(total_price))

                    # Generate short customer ID and booking ID
                    customer_id = generate_short_id()
                    booking_id = generate_short_id()

                    # Save booking details to the database
                    cursor.execute("INSERT INTO bookings (booking_id, room_number, customer_id, check_in_date, check_out_date, total_price) VALUES (?, ?, ?, ?, ?, ?)",
                                   (booking_id, room_no, customer_id, check_in_date, check_out_date, total_price))
                    conn.commit()

                    # Display generated IDs in the window
                    customer_id_label.config(text="Customer ID: " + customer_id)
                    booking_id_label.config(text="Booking ID: " + booking_id)

                    # Remove booked room from the rooms table
                    cursor.execute("DELETE FROM rooms WHERE room_number = ?", (room_no,))
                    conn.commit()

                except ValueError:
                    total_price_label.config(text="Invalid Dates")
            else:
                total_price_label.config(text="Room not found") 

        booking_window = Toplevel(main_window)
        booking_window.title("Booking")
        booking_window.geometry("1550x800")
        booking_window.configure(bg="peach puff")
        booking_window.protocol("WM_DELETE_WINDOW", lambda: destroy_window(booking_window))

        # Heading
        customer_heading_label = Label(booking_window, text="Booking Details", font=("Times New Roman", 24, "bold"), bg="peach puff")
        customer_heading_label.pack(pady=20)

        room_no_label = Label(booking_window, text="Room Number:", font=("Times New Roman", 16, "bold"), bg="peach puff")
        room_no_label.place(relx=0.5, rely=0.25, anchor=CENTER)
        room_no_entry = Entry(booking_window, font=("Times New Roman", 14, "bold"))
        room_no_entry.place(relx=0.5, rely=0.30, anchor=CENTER)

        check_in_label = Label(booking_window, text="Check-in Date (YYYY-MM-DD):", font=("Times New Roman", 16, "bold"), bg="peach puff")
        check_in_label.place(relx=0.5, rely=0.35, anchor=CENTER)
        check_in_entry = Entry(booking_window, font=("Times New Roman", 14, "bold"))
        check_in_entry.place(relx=0.5, rely=0.40, anchor=CENTER)

        check_out_label = Label(booking_window, text="Check-out Date (YYYY-MM-DD):", font=("Times New Roman", 16, "bold"), bg="peach puff")
        check_out_label.place(relx=0.5, rely=0.45, anchor=CENTER)
        check_out_entry = Entry(booking_window, font=("Times New Roman", 14, "bold"))
        check_out_entry.place(relx=0.5, rely=0.50, anchor=CENTER)

        book_button = Button(booking_window, text="Book", command=book_room, font=("Times New Roman", 14, "bold"), bg="black", fg="gold")
        book_button.place(relx=0.5, rely=0.60, anchor=CENTER)

        # Total Price Label
        total_price_label = Label(booking_window, text="", font=("Times New Roman", 14, "bold"), bg="peach puff")
        total_price_label.place(relx=0.5, rely=0.55, anchor=CENTER)

        # Display customer and booking IDs
        customer_id_label = Label(booking_window, text="", font=("Times New Roman", 16, "bold"), bg="peach puff")
        customer_id_label.place(relx=0.5, rely=0.65, anchor=CENTER)

        booking_id_label = Label(booking_window, text="", font=("Times New Roman", 16, "bold"), bg="peach puff")
        booking_id_label.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Back Button
        back_button = Button(booking_window, text="Back", command=lambda: destroy_window(booking_window), font=("Times New Roman", 14, "bold"), bg="black", fg="gold")
        back_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    main_window = Toplevel(root)
    main_window.title("Main Page")
    main_window.geometry("1550x800")
    main_window.configure(bg="peach puff")
    main_window.protocol("WM_DELETE_WINDOW", lambda: destroy_window(main_window))

    # Heading
    heading_label = Label(main_window, text="Hotel Management System", font=("Times New Roman", 20, "bold"), bg="peach puff")
    heading_label.pack(pady=20)

    # Subheading - Menu
    menu_subheading = Label(main_window, text="Menu", font=("Times New Roman", 18, "bold"), bg="peach puff")
    menu_subheading.pack()

    # Space after subheading
    space_label = Label(main_window, text="", bg="peach puff")
    space_label.pack()

    # Customer Button
    customer_button = Button(main_window, text="Customer", font=("Times New Roman", 16, "bold"), width=20, height=2, command=customer_details_window, bg="black", fg="gold")
    customer_button.pack()

    # Space after Customer button
    space_label = Label(main_window, text="", bg="peach puff")
    space_label.pack()

    # Hotel Button
    hotel_button = Button(main_window, text="Hotel", font=("Times New Roman", 16, "bold"), width=20, height=2, command=hotel_details_page, bg="black", fg="gold")
    hotel_button.pack()

    # Space after Hotel button
    space_label = Label(main_window, text="", bg="peach puff")
    space_label.pack()

    # Room Button
    room_button = Button(main_window, text="Room", font=("Times New Roman", 16, "bold"), width=20, height=2, command=room_details_window, bg="black", fg="gold")
    room_button.pack()

    # Space after Room button
    space_label = Label(main_window, text="", bg="peach puff")
    space_label.pack()

    # Booking Button
    booking_button = Button(main_window, text="Booking", font=("Times New Roman", 16, "bold"), width=20, height=2, command=lambda: booking_window(main_window), bg="black", fg="gold")
    booking_button.pack()

    # Logout Button
    logout_button = Button(main_window, text="Logout", command=logout, font=("Times New Roman", 14, "bold"), width=10, height=2, bg="black", fg="gold")
    logout_button.place(relx=1.0, rely=0.0, anchor=NE)

def signup_window():
    def back():
        signup_window.destroy()

    def validate_email(email):
        if email.endswith("@gmail.com"):
            return True
        return False

    def validate_username(username):
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            return False, "Username already exists"
        return True, ""

    def validate_password(password):
        return True, ""

    def signup():
        email = email_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        # Validate email, username, and password
        if validate_email(email):
            validation, msg = validate_username(username)
            if validation:
                validation, msg = validate_password(password)
                if validation:
                    # Insert user data into the database
                    cursor.execute("INSERT INTO users (email, username, password) VALUES (?, ?, ?)", (email, username, password))
                    conn.commit()
                    print("Account created successfully")
                    signup_window.destroy()
                    main_page()
                else:
                    validation_label.config(text=msg)
            else:
                validation_label.config(text=msg)
        else:
            validation_label.config(text="Email should end with @gmail.com")

    signup_window = Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("1550x800")
    signup_window.configure(bg="peach puff")  # background color
    signup_window.protocol("WM_DELETE_WINDOW", lambda: destroy_window(signup_window))

    # Heading
    heading_label = Label(signup_window, text="Hotel Management System", font=("Times New Roman", 20, "bold"), bg="peach puff")
    heading_label.pack(pady=20)

    email_label = Label(signup_window, text="Email:", font=("Times New Roman", 16, "bold"), bg="peach puff")
    email_label.place(relx=0.5, rely=0.20, anchor=CENTER)
    email_entry = Entry(signup_window, font=("Times New Roman", 14))
    email_entry.place(relx=0.5, rely=0.25, anchor=CENTER)

    username_label = Label(signup_window, text="Username:", font=("Times New Roman", 16, "bold"), bg="peach puff")
    username_label.place(relx=0.5, rely=0.30, anchor=CENTER)
    username_entry = Entry(signup_window, font=("Times New Roman", 14))
    username_entry.place(relx=0.5, rely=0.35, anchor=CENTER)

    password_label = Label(signup_window, text="Password:", font=("Times New Roman", 16, "bold"), bg="peach puff")
    password_label.place(relx=0.5, rely=0.40, anchor=CENTER)
    password_entry = Entry(signup_window, show="*", font=("Times New Roman", 14))
    password_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

    signup_button = Button(signup_window, text="Create Account", font=("Times New Roman", 14, "bold"), command=signup, width=20, height=2, bg="black", fg="gold")
    signup_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    validation_label = Label(signup_window, text="", font=("Times New Roman", 12, "bold"), fg="red", bg="peach puff")
    validation_label.place(relx=0.5, rely=0.8, anchor=CENTER)

    back_button = Button(signup_window, text="Back", font=("Times New Roman", 12, "bold"), command=back, width=10, height=2, bg="black", fg="gold")  # Adjusted size here
    back_button.place(relx=0.5, rely=0.9, anchor=CENTER)

def login_window():
    def back():
        login_window.destroy()

    def login():
        username = username_entry.get()
        password = password_entry.get()
        
        # Check if the username exists in the database
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        if user:
            # Check if the password matches
            if user[3] == password:
                print("Login successful")
                login_window.destroy()
                main_page()
            else:
                login_message.config(text="Invalid username or password!")
        else:
            login_message.config(text="Create an account first")

    login_window = Toplevel(root)
    login_window.title("Login")
    login_window.geometry("1550x800")
    login_window.configure(bg="peach puff")  #background color
    login_window.protocol("WM_DELETE_WINDOW", lambda: destroy_window(login_window))

    # Heading
    heading_label = Label(login_window, text="Hotel Management System", font=("Times New Roman", 20, "bold"), bg="peach puff")
    heading_label.pack(pady=20)

    username_label = Label(login_window, text="Username:", font=("Times New Roman", 16, "bold"),bg="peach puff")
    username_label.place(relx=0.5, rely=0.30, anchor=CENTER)
    username_entry = Entry(login_window, font=("Times New Roman", 14))
    username_entry.place(relx=0.5, rely=0.35, anchor=CENTER)

    password_label = Label(login_window, text="Password:", font=("Times New Roman", 16, "bold"),bg="peach puff")
    password_label.place(relx=0.5, rely=0.40, anchor=CENTER)
    password_entry = Entry(login_window, show="*", font=("Times New Roman", 14))
    password_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

    login_button = Button(login_window, text="Login", command=login, font=("Times New Roman", 14, "bold"), width=20, height=2, bg="black", fg="gold")
    login_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    login_message = Label(login_window, text="", font=("Times New Roman", 12, "bold"), fg="red", bg="peach puff")
    login_message.place(relx=0.5, rely=0.8, anchor=CENTER)

    back_button = Button(login_window, text="Back", command=back, font=("Times New Roman", 12, "bold"), width=10, height=2, bg="black", fg="gold")  # Adjusted size here
    back_button.place(relx=0.5, rely=0.9, anchor=CENTER)

root = Tk()
root.title("Hotel Management System")
root.geometry("1550x800")
root.configure(bg="peach puff")  

# Heading
heading_label = Label(root, text="Hotel Management System", font=("Times New Roman", 20, "bold"), bg="peach puff")
heading_label.pack(pady=20)

hotel_image = PhotoImage(file="C:/Users/psara/OneDrive/Desktop/project/hotelpic.png")  
image_label = Label(root, image=hotel_image)
image_label.pack()

# Login Button
login_button = Button(root, text="Login", command=login_window, font=("Times New Roman", 14), width=20, height=2, bg="black", fg="gold")
login_button.pack(side=LEFT, expand=True, padx=10, pady=10)


# Signup Button
signup_button = Button(root, text="Sign Up", command=signup_window, font=("Times New Roman", 14), width=20, height=2, bg="black", fg="gold")
signup_button.pack(side=LEFT, expand=True, padx=10, pady=10)

root.mainloop()
