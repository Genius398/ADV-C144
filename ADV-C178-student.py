
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("ioued")
root.geometry("800x600")
root.config(bg="#2a63bf")



label_heading=Label(root, text="Juicy Jucie Jucies", bg="#2a63bf",fg="white",  font=("Sylfaen", 18,"bold", "italic"))
label_heading.place(relx=0.05, rely=0.1, anchor=W)

#########

fruit_image=Label(root, bg="orange2")
fruit_image.place(rel=0.75, rely=0.8, anchor=CENTER)

label_name=Label(root, text="Select Fruit", bg="#2a63bf")
label.place(relx=0.96, rely=0.2, anchor=E)

fruit_list = ["Apple", "Mango", "Orange"]
fruit_dropdown = ttk.Combobox(root, state = "readonly", values=fruit_list, justify="right")
fruit_dropdown.place(Relx=0.95, rely=0.25, anchor=E)


label_quantity = Label(root, text="Enter Quantity", bg="#2a63bf")
label_quantity.place(relx=0.96, rely=0.35, anchor=E)

input_quantity=Entry(root)
input_quantity.place(relx=0.95, rely=0.8, anchor=E)

label_show_amount = Label(root, bg="#2a63bf",)
label_show_amount.place(relx=0.95, rely=0.7, anchor=E)


label_show_quantity = Label(root, bg="#2a63bf",)
label_show_quantity.place(relx=0.95, rely=0.8, anchor=E)






















class Juice:
    def __init__(self, fruit_name, quantity):
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self.__cost = 250

    def __calculateCost(self):
        total_cost = self.quantity * self.__cost
        label_show_amount['text'] ="You need to pay :" + str(total_cost) + "USD"
        print("You shall pay:" + str(total_cost) + "$")
        if(self.fruit == "Apple"):
            calorie = self.quantity * 
            fruit_image['image'] = apple
        if(self.fruit == "Mango"):
            calorie = self.quantity * 60
            fruit_image['image'] = mango
        if(self.fruit == "Orange"):
            calorie = self.quantity * 47
            fruit_image=orange

        print("x"+str(self.quantity)+" = "+str(calorie)+" Calories ")

    def getCost(self):
        self.__calculateCost()


def orderJuice():
    fruit = "Orange"
    quantity = 200
    obj1 = Juice(fruit, quantity)
    obj1.getCost()


btn = Button(root, text="TOTAL", command=orderJuice)
btn.place(relx=0.95, rely=0.5, anchor=E)

root.mainloop()
