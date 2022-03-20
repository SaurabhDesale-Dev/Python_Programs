our_password='pass123'
your_answers =''
number_of_try=0
number_max_of_try=3
Max_try='not reached'

while your_answers!=our_password and Max_try!='Reached':
    if number_of_try<number_max_of_try:
        your_answers=input('what is the password :')
        number_of_try=number_of_try+1
    else:
        Max_try='Reached'

if Max_try =='Reached':
    print("account blocked")
else:
    print('access granted')