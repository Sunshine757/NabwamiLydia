#square of a number
def squareNumber():
    number = 5
    square = number * number
    print(square)

    #calling the function
    squareNumber()

    #write a function that takes in input and calculates the area of a recatangle
    def areaOfRectangle():
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        area = length * width
        print("The area of the rectangle is:", area)

    #calling the function
    areaOfRectangle()