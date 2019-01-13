#calculate total pay base on worked hours
def exercise_1():
    hrs = input("Enter hours:")
    h = float(hrs)
    rate = input("Enter rate:")
    r = float(rate)
    if h > 40:
        return (h - 40)*1.5*r + 40*r
    else:
        return h*r
print(exercise_1())
