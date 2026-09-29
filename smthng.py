# def addtwo(a,b):
#     c = a + b
#     return c
# x = addtwo(3, 5)
# print(x)

#Ex 6
# def compute_pay():
#     hours = int(input("Enter hours: "))
#     rate = float(input("Enter rate: "))
#     if hours <= 40:
#         pay = int(hours * rate)
#     else:
#         pay = 40 * rate + (hours - 40) * rate * 1.5
#     return int(pay)
#
# print('Pay', compute_pay())

#Ex 7
def findgrade():
    point = float(input("Enter point: "))
    if point >= 0.9:
        return 'A'
    elif point >= 0.8:
        return 'B'
    elif point >= 0.7:
        return 'C'
    elif point >= 0.6:
        return 'D'
    elif point < 0.6:
        return 'F'
    else:
        return 'Error: invalid point'
print('Grade', findgrade())
