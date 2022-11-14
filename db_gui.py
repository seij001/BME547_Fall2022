import tkinter as tk
from tkinter import ttk


def main_window():

    def ok_cmd():
        other_button.configure(state=tk.NORMAL)
        if rh_button.get() == "":
            print("Choose a rh factor")
            return
        print("Patient name: {}".format(patient_name_entry.get()))
        print("Patient id: {}".format(patient_id_entry.get()))
        print("Blood type: {}{}".format(blood_letter_selection.get(),
                                        rh_button.get()))
        print("Donation Center: {}".format(donor_center.get()))
        print("Clicked Ok button")

    def cancel_cmd():
        root.destroy()

    root = tk.Tk()
    root.title("Blood Donor Database Window")
    # root.geometry("600x300")

    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                      columnspan=2,
                                                      sticky=tk.W)
    ttk.Label(root, text="Name:").grid(column=0, row=1)

    patient_name_entry = tk.StringVar()
    ttk.Entry(root, width=50, textvariable=patient_name_entry).grid(column=1,
                                                                    row=1)

    ttk.Label(root, text="Id:").grid(column=0, row=2, sticky=tk.E)
    patient_id_entry = tk.StringVar()
    ttk.Entry(root, textvariable=patient_id_entry).grid(column=1, row=2,
                                                        sticky="W")

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

    ttk.Label(root, text="Closest Donation Center").grid(column=2, row=0)
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(column=2, row=1)
    donor_center_combo["values"] = ["Durham", "Cary", "Raleigh"]
    donor_center_combo.state(["readonly"])


    ttk.Button(root, text="Ok", command=ok_cmd).grid(column=1, row=6)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(column=2, row=6)


    other_button = ttk.Button(root, text="Other", state=tk.DISABLED)
    other_button.grid(column=2, row=7)


    root.mainloop()


if __name__ == '__main__':
    main_window()
