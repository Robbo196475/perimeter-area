'''
Area

'''
# Heading 



# Define function to calculate area of rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Define function to calculate perimeter of rectangle
# Define function to calculate perimeter of rectangle
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

  #------------main-----------------
# Get user input for length and width of rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Calculate and print area and perimeter of rectangle
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)
print("Area of rectangle: ", area)
print("Perimeter of rectangle: ", perimeter)


import tkinter as tk
from tkinter import ttk, Canvas

def draw_shape():
    canvas.delete("all")
    
    shape = shape_var.get()
    if shape == "Rectangle":
        canvas.create_rectangle(50, 50, 150, 150, fill='red')
    elif shape == "Oval":
        canvas.create_oval(50, 50, 150, 150, fill='blue')
    elif shape == "Triangle":
        canvas.create_polygon(100, 50, 50, 150, 150, 150, fill='green')

root = tk.Tk()
root.title("Shape Chooser")

canvas = Canvas(root, width=200, height=200, bg='white')
canvas.pack()

shape_var = tk.StringVar(value="Rectangle")

shape_dropdown = ttk.Combobox(root, textvariable=shape_var,
                              values=["Rectangle", "Oval", "Triangle"], state="readonly")
shape_dropdown.pack()

draw_button = ttk.Button(root, text="Draw", command=draw_shape)
draw_button.pack()

root.mainloop()


import tkinter as tk
from tkinter import ttk, Canvas

def calculate_area_perimeter():
    canvas.delete("all")
    
    shape = shape_var.get()
    dimensions = dimensions_entry.get()
    dimension_list = dimensions.split(",")
    for i in range(len(dimension_list)):
        dimension_list[i] = int(dimension_list[i])
    
    if shape == "Rectangle":
        area = dimension_list[0] * dimension_list[1]
        perimeter = 2 * (dimension_list[0] + dimension_list[1])
        canvas.create_rectangle(50, 50, 50+dimension_list[0], 50+dimension_list[1], fill='red')
    elif shape == "Circle":
        radius = dimension_list[0]
        area = 3.14 * radius * radius
        perimeter = 2 * 3.14 * radius
        canvas.create_oval(50, 50, 50+2*radius, 50+2*radius, fill='blue')
    elif shape == "Triangle":
        base = dimension_list[0]
        height = dimension_list[1]
        area = 0.5 * base * height
        perimeter = dimension_list[0] + dimension_list[1] + dimension_list[2]
        canvas.create_polygon(50, 50, 50+base, 50, 50+base/2, 50+height, fill='green')
    
    area_label.config(text="Area: {:.2f}".format(area))
    perimeter_label.config(text="Perimeter: {:.2f}".format(perimeter))

root = tk.Tk()
root.title("Shape Calculator")

canvas = Canvas(root, width=200, height=200, bg='white')
canvas.pack()

shape_var = tk.StringVar(value="Rectangle")

shape_dropdown = ttk.Combobox(root, textvariable=shape_var,
                              values=["Rectangle", "Circle", "Triangle"], state="readonly")
shape_dropdown.pack()

dimensions_label = ttk.Label(root, text="Enter dimensions (separated by commas):")
dimensions_label.pack()

dimensions_entry = ttk.Entry(root)
dimensions_entry.pack()

calculate_button = ttk.Button(root, text="Calculate", command=calculate_area_perimeter)
calculate_button.pack()

area_label = ttk.Label(root, text="Area: ")
area_label.pack()

perimeter_label = ttk.Label(root, text="Perimeter: ")
perimeter_label.pack()

root.mainloop()
