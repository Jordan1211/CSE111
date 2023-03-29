import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
from datetime import datetime

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Concrete Price Calculator")
    frm_main.pack(padx=85, pady=20, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_length = Label(frm_main, text="Length:")

    # Create an integer entry box where the user will enter her age.
    ent_length = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=500)

    # Create a label that displays "Age:"
    lbl_width = Label(frm_main, text="Width:")
    # Create an integer entry box where the user will enter her age.
    ent_width = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=500)

    # Create a label that displays "Age:"
    lbl_depth = Label(frm_main, text="Depth:")
    # Create an integer entry box where the user will enter her age.
    ent_depth = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=500)

    # Create a label that displays "Age:"
    lbl_cost = Label(frm_main, text="Cost:")
    # Create an integer entry box where the user will enter her age.
    ent_cost = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=500)

    # Create a label that displays "years"
    lbl_length_units = Label(frm_main, text="feet")

    # Create a label that displays "years"
    lbl_width_units = Label(frm_main, text="feet")

    # Create a label that displays "years"
    lbl_depth_units = Label(frm_main, text="inches")

    # Create a label that displays "years"
    lbl_cost_units = Label(frm_main, text="dollars")

    # Create labels that will display the total.
    lbl_total = Label(frm_main, text="<Total>", width=30)

    # Create labels that will display the date.
    lbl_date = Label(frm_main, text="<Date>", width=30)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_length.grid(      row=0, column=0, padx=3, pady=3)
    ent_length.grid(      row=0, column=1, padx=3, pady=3)
    lbl_length_units.grid(row=0, column=2, padx=0, pady=3)

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_width.grid(      row=1, column=0, padx=3, pady=3)
    ent_width.grid(      row=1, column=1, padx=3, pady=3)
    lbl_width_units.grid(row=1, column=2, padx=0, pady=3)

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_depth.grid(      row=2, column=0, padx=3, pady=3)
    ent_depth.grid(      row=2, column=1, padx=3, pady=3)
    lbl_depth_units.grid(row=2, column=2, padx=0, pady=3)

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_cost.grid(      row=3, column=0, padx=3, pady=3)
    ent_cost.grid(      row=3, column=1, padx=3, pady=3)
    lbl_cost_units.grid(row=3, column=2, padx=3, pady=3)

    lbl_total.grid(     row=5, columnspan=4)
    lbl_date.grid(      row=6, columnspan=5)
    btn_clear.grid(row=7, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # 
            length = ent_length.get()
            width = ent_width.get()
            depth = ent_depth.get()
            cost = ent_cost.get()
            current_date_and_time = datetime.now()

            # 
            depth_feet = depth/12
            area = length*width*depth_feet
            surface_area = length*width
            labor = surface_area*3
            cubic_yards = area/27

            total_price = (cubic_yards * cost) + labor

            lbl_total.config(text=f"Total Cost: ${total_price:.2f}")
            lbl_date.config(text=f"Quoted: {current_date_and_time:%m/%d/%Y %I:%M%p}")

        except ValueError:
            # When the user deletes all the digits in the cost
            # entry box, clear the total label.
            lbl_total.config(text="")
            lbl_date.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_length.clear()
        ent_width.clear()
        ent_depth.clear()
        ent_cost.clear()
        lbl_total.config(text="")
        lbl_date.config(text="")
        ent_length.focus()


    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_cost.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_length.focus()


# Duplicating the exact calculate event in order to complete testing
def calculate_area(length, width, depth, cost):
    """Compute and display the user's slowest
    and fastest beneficial heart rates.
    """
    try:
        # Completeing calucaltions in order to set total price
        depth_feet = depth/12
        area = length*width*depth_feet
        surface_area = length*width
        labor = surface_area*3
        cubic_yards = area/27

        total_price = (cubic_yards * cost) + labor
        
        return round(total_price,2)

    except ValueError as val_err:
        # When the user deletes all the digits in the cost
        # entry box, clear the total label.
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for" \
                " the line number.")


# If this file is executed like this:
# > python project.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()