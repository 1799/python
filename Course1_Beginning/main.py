#exercise_1: calculate total pay base on worked hours
def exercise_1():
    hrs = input("Enter hours:")
    h = float(hrs)
    rate = input("Enter rate:")
    r = float(rate)
    if h > 40:
        return (h - 40)*1.5*r + 40*r
    else:
        return h*r
#print(exercise_1())

#exercise_2: find max and min from input
def exercise_2():
    max = None
    min = None
    while True:
        s_value = input('Enter the number: ')
        if s_value == 'done':
            break
        try:
            i_value = int(s_value)
        except:
            print('Invalid input')
            continue
        if max is None and min is None:
            max = i_value
            min = i_value
            continue
        if i_value < min:
            min = i_value
        if i_value > max:
            max = i_value
    print('Maximum is', max)
    print('Minimum is', min)
exercise_2()
