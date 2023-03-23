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

# Get user input for length and width of rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Calculate and print area and perimeter of rectangle
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)
print("Area of rectangle: ", area)
print("Perimeter of rectangle: ", perimeter)
