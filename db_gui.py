import tkinter as tk
from tkinter import ttk
import db_client
from PIL import Image, ImageTk
from tkinter import filedialog


def create_blood_type(letter, rh):
    """Modular function that can be tested that combines the blood type
        letter and rh factor into a single string that can be uploaded to the
        server.

    Args:
        letter (str): the blood type letter (A, B, AB, O)
        rh (str): "-" or "+"

    Returns:
        string, combined blood type

    """
    output = "{}{}".format(letter, rh)
    return output


def convert_string_to_integer(input_string):
    """Convert numeric string to integer, if possible

    Using a try/except block, the input string is converted to an integer
    using the "int" function.  If the input string is not a numeric string,
    a ValueError will be raised, which is captured and a boolean value of False
    is returned.  Otherwise, the resulting integer is returned.

    Args:
        input_string: string obtained from GUI that may contain a number

    Returns:
        int: the integer found in the numeric string, or
        bool: False if the string is non-numeric.

    """
    try:
        output_int = int(input_string)
    except ValueError:
        return False
    return output_int


def upload_data_to_server(patient_name, patient_id, patient_blood_letter,
                          patient_rh_factor):
    """Manipulates patient data and calls client code to upload the data to
        the server

    This function is called by the GUI and is sent patient information that was
    entered into the GUI.  It first calls a function to combine the blood type
    letter and rH factor into a single string for upload.  It then calls a
    function to convert the patient_id, obtained as a string from the GUI, into
    an integer.  The resulting patient data is then sent to a client function
    to be uploaded to the server.

    Args:
        patient_name (str): Patient named as entered into GUI
        patient_id (str): Patient id as entered into GUI
        patient_blood_letter (str): Patient blood type letter as entered into
            GUI
        patient_rh_factor (str): positive or negative rH factor.

    Returns:
        string: message with outcome of the function to be displayed in GUI

    """
    blood_type = create_blood_type(patient_blood_letter, patient_rh_factor)
    patient_id = convert_string_to_integer(patient_id)
    if patient_id is False:
        return "Patient ID is not an integer.  Try again."
    msg, code = db_client.upload_patient_info(patient_name,
                                              patient_id,
                                              blood_type)
    return msg


def main_window():
    """ Defines main window of the GUI

    The function creates the widgets and layout for the main window of the
    Database entry GUI.  After the root window is defined, each widget is
    created and added to the Grid Layout Manager.  For widgets that will
    receive some sort of input, tkinter.StringVars are created to hold that
    input.  Some widgets have "command" functions linked to them, and those
    command functions can be found as "sub-functions" of this function.

    These sub-functions should only do three things:
        1. Get information from the GUI
        2. Call separate, modular, testable functions to do the work
        3. Update the GUI as necessary based on response for functions in
        step 2.

    Returns:
        None
    """

    def get_update_info():
        """Mock function to demonstrate the use of '.after()' method

        The `.after()` method is a method of the root window (or, any other
        widget for that matter), that establishes a callback to happen after
        a certain amount of time.  `.after()` takes two parameters.  The first
        is an integer that specifies the number of milliseconds to wait until
        calling the desired function.  The second parameter is the name of the
        function that should be called after the specified time has elapsed.
        The function name should NOT include `()` after it.

        In the main code of the "main_window" function, the first '.after()`
        call is made to call this function after a certain period of time.  So
        that this function is called again after that same period of time, this
        function must end with another call to '.after()'.

        Replace the first line of this function with whatever code you would
        like to have recurred.

        """
        print("Get Data")
        root.after(2000, get_update_info)

    def ok_cmd():
        """Gather data from GUI and call function to upload it to server

        This function is called when the "Ok" button on the GUI is clicked.
        It should be clicked after the user has entered the desired information
        in the GUI and wants to upload it to the server.  As described in the
        docstring for the "main_window", this function only does three things:
        1) get data from gui
            It accesses the various "StringVar"s to get the inputted
            information.  While doing this, it does check to see if a selection
            was made for the rH factor.  If not, the function is cancelled.
        2) call other functions
            It sends the information obtained from the GUI to a function to
            be manipulated and uploaded to server
         3) update gui
            It updates the status label with the message received from the
            called code.
        """
        # Get data from interface
        if rh_button.get() == "":
            print("Choose a rh factor")
            return
        patient_name = patient_name_entry.get()
        patient_id = patient_id_entry.get()
        patient_blood_letter = blood_letter_selection.get()
        patient_rh_factor = rh_button.get()

        # Call other testable functions to do all the work
        msg = upload_data_to_server(patient_name, patient_id,
                                    patient_blood_letter,
                                    patient_rh_factor)

        # Update GUI based on results of other functions
        status_label.configure(text=msg)

    def cancel_cmd():
        """Closes window upon the 'Cancel' button being clicked

        The main interface window has a 'Cancel' button whose command function
        is linked to this function.  When clicked, this function will call the
        `.destroy()` method of the root window, which will end the GUI causing
        the main window to close.
        """
        root.destroy()

    def picture_button_cmd():
        """User can select new image to be displayed in GUI

        This function is lined to the click action of the "Load Picture"
        button.  The user clicks this button when they want to add a
        patient picture to the GUI.  The function uses the "askopenfilename"
        to get an image file name.  If the user clicks "Cancel" in this
        dialog window, a blank string is returned.  If the blank string is
        returned, the function ends.  Otherwise, this filename is used to load
        in a Pillow image object.  This Pillow image object is resized such
        that the height of the image is 100 pixels and the width scales to keep
        the original image dimensions.  This resized image is converted to a
        tkinter image object which is attached to the image label.

        Returns:
            None

        """
        new_file = filedialog.askopenfilename()
        if new_file == "":
            return
        print("Filename: {}".format(new_file))
        pil_image = Image.open(new_file)
        x_size, y_size = pil_image.size
        new_y = 100
        new_x = new_y * x_size / y_size
        pil_image = pil_image.resize((round(new_x), round(new_y)))
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image

    # Define Main Window
    root = tk.Tk()
    root.title("Blood Donor Database Window")
    # root.geometry("600x300")
    # Use the line above if you want to define window to a particular size.

    # Title Label
    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                      columnspan=2,
                                                      sticky=tk.W)

    # Name Widgets
    ttk.Label(root, text="Name:").grid(column=0, row=1)
    patient_name_entry = tk.StringVar()
    ttk.Entry(root, width=50, textvariable=patient_name_entry).grid(column=1,
                                                                    row=1)

    # Id Widgets
    ttk.Label(root, text="Id:").grid(column=0, row=2, sticky=tk.E)
    patient_id_entry = tk.StringVar()
    ttk.Entry(root, textvariable=patient_id_entry).grid(column=1, row=2,
                                                        sticky="W")

    # Blood Type Widgets
    blood_letter_selection = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter_selection,
                    value="A").grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root, text="B", variable=blood_letter_selection,
                    value="B").grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root, text="AB", variable=blood_letter_selection,
                    value="AB").grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(root, text="O", variable=blood_letter_selection,
                    value="O").grid(column=0, row=6, sticky=tk.W)

    rh_button = tk.StringVar()
    ttk.Checkbutton(root, text="Rh Positive",
                    variable=rh_button,
                    onvalue="+",
                    offvalue="-").grid(column=1, row=4)

    # Closest Donation Center Widgets
    ttk.Label(root, text="Closest Donation Center").grid(column=2, row=0)
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(column=2, row=1)
    donor_center_combo["values"] = ["Durham", "Cary", "Raleigh"]
    donor_center_combo.state(["readonly"])

    # Bottom Buttons
    ttk.Button(root, text="Ok", command=ok_cmd).grid(column=1, row=6)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(column=2, row=6)

    other_button = ttk.Button(root, text="Other", state=tk.DISABLED)
    other_button.grid(column=2, row=7)

    picture_button = ttk.Button(root, text="Load Picture",
                                command=picture_button_cmd)
    picture_button.grid(column=2, row=8)

    # Status Label
    status_label = ttk.Label(root, text="Status")
    status_label.grid(column=0, row=8)

    # Image Label with initial image shown
    pil_image = Image.open("Images/blank_pic.jpeg")
    pil_image = pil_image.resize((100, 100))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.grid(column=1, row=8)

    # Start recurring function call
    root.after(2000, get_update_info)

    # Activate GUI Loop (should always be the last command in this function)
    root.mainloop()


if __name__ == '__main__':
    main_window()
