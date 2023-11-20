# student_data = {
#     'Jason': 'Gryffindor',
#     'Kaitlynne': 'Ravenclaw',
#     'Aidan': 'Slytherin',
#     'Nicole': 'HufflePuff',
#     'Antonio': 'Gryffindor',
#     'Alexander': 'Ravenclaw',
#     'Samantha': 'Slytherin',
#     'Reagan': 'Hufflepuff',
#     'Lauren': 'Gryffindor',
#     'Emma': 'Ravenclaw',
#     'Veronica': 'Slytherin',
#     'Matthew': 'HufflePuff',
#     'Madison': 'Gryffindor',
#     'Jijoy': 'Ravenclaw',
#     'Christopher': 'Slytherin',
#     'Alex': 'HufflePuff',
#     'Cedric': 'Gryffindor'
# }

# print("Students in Gryffindor: ")
# for student, house in student_data.items():
#     if house == 'Gryffindor':
#         print(student)

# import math

# def calculate_odds(probability):
#     return probability / (1 - probability)

# probability = float(input("Enter the probability of the event (between 0 and 1): "))

# odds = calculate_odds(probability)

# print(f"The odds are: {odds:.2f} to 1")

def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

radius_input = input("Enter Radius: ")
radius = float(radius_input)

circleArea = calculate_area(radius)
print("The area of the circle is: ", circleArea)
