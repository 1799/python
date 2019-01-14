# exercise_1: find number in text
def exercise_1():
    num_check = [0,1,2,3,4,5,6,7,8,9]
    text = "X-DSPAM-Confidence:    0.8475."
    i_stoppos = 0
    onedot = True
    onedot_count = 0
    for i_temp in num_check:
        s_temp = str(i_temp)
        i_startpos = text.find(s_temp)
        if i_startpos != -1:
            i_stoppos = i_startpos+1
            break
    for letter in text[i_startpos+1:]:
        if letter in '0123456789':
            i_stoppos = i_stoppos+1
        elif letter is '.':
            onedot_count = onedot_count + 1
            if onedot_count == 2:
                break
            i_stoppos = i_stoppos+1
        else:
            break
    s_number = text[i_startpos:i_stoppos]
    f_number = float(s_number)
    print(f_number)
exercise_1()
