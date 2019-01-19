# exercise_1: find number in text
def exercise_1(input):
    num_check = [0,1,2,3,4,5,6,7,8,9]
    text = "X-DSPAM-Confidence:    0.8475."
    i_stoppos = 0
    onedot = True
    onedot_count = 0
    for i_temp in num_check:
        s_temp = str(i_temp)
        i_startpos = input.find(s_temp)
        if i_startpos != -1:
            i_stoppos = i_startpos+1
            break
    for letter in input[i_startpos+1:]:
        if letter in '0123456789':
            i_stoppos = i_stoppos+1
        elif letter is '.':
            onedot_count = onedot_count + 1
            if onedot_count == 2:
                break
            i_stoppos = i_stoppos+1
        else:
            break
    s_number = input[i_startpos:i_stoppos]
    f_number = float(s_number)
    return f_number


#exercise_2: read exactly data from file and calculate average i_value
def exercise_2():
    fname = input('Enter file name:')
    count = 0
    value = 0.0
    fopen = open(fname)
    for line in fopen:
        line = line.rstrip()
        if not line.startswith('X-DSPAM-Confidence:'):
            continue
        value = value + exercise_1(line)
        count = count + 1
    average = value/count
    print('Average spam confidence: ',str_average)
#exercise_2()
def exercise_3():
    lst = list()
    fname = input('Enter file name:')
    fopen = open(fname)
    for line in fopen:
        line = line.split()
        for value in line:
            if value not in lst:
                lst.append(value)
    lst.sort()
    print(lst)
#exercise_3()

def exercise_4():
    lst = list()
    count = 0
    fname = input('Enter file name:')
    fopen = open(fname)
    for line in fopen:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        lst = line.split()
        print(lst[1])
        count = count +1
    print("There were", count, "lines in the file with From as the first word")
#exercise_4()

def exercise_5():
    lst = list()
    dic = dict()
    count = 0
    item = ''
    fname = input('Enter file name:')
    fopen = open(fname)
    for line in fopen:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        lst.append(line[1])
    for key in lst:
        dic[key] = dic.get(key,0) + 1
    for key,value in dic.items():
        if count == 0 or value > count:
            count = value
            item = key
    print(item, count)
exercise_5()
