from tkinter import *
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.geometry("200x100")


def miles_to_kilo():
    miles = float(miles_input.get())
    if miles == 0:
        print("Enter valid input")
    km = round(1.609*miles)
    km_result_label.config(text=km)


miles_input = Entry()
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_result_label = Label(text=0)
km_result_label.grid(column=1, row=1)
calculate_button = Button(text="Calculate", command=miles_to_kilo)
calculate_button.grid(column=1, row=2)


window.mainloop()
