print('How many years have you been a employee: ')
emyears = int(input())
if emyears >= 30:
    vacadays = int(emyears * 3)
elif emyears >= 20:
    vacadays = int(emyears * 2)
elif emyears >= 10:
    vacadays = int(emyears * 1.5)
else:
    vacadays = int(emyears * 1)
print('You have ' + str(vacadays) + ' vacation days.')
