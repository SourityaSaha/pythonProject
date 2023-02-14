
#Souritya Saha Assingment 1b

months={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',
        10:'October',11:'November',12:'December'}
days={1:[1,31],2:[1,28],3:[1,31],4:[1,30],5:[1,31],6:[1,30],7:[1,31],8:[1,31],9:[1,30],10:[1,31],11:[1,30],12:[1,31]}
date=input('Enter a date in this format mm/dd/yyyy: ')
form =date.split('/')
if len(form)!=3:
    print('Incorrect format')
else:
    mm,dd,yyyy=form
    if not mm.isnumeric() or not dd.isnumeric() or not yyyy.isnumeric():
        print("You didn't entered a numeric data ")
    else:
        mm=int(mm)
        dd=int(dd)
        yyyy=int(yyyy)
        if mm<1 or mm>12:
            print('Month is not correct please enter 1-12')
        elif dd<days[mm][0] or dd>days[mm][1]:
            print('Day is not matching the month')
        else:
            print('{:s} {:d}, {:d}'.format(months[mm],dd,yyyy))