def question():
    rules=input('You need to answer each and every question by yes or no:')
    if rules!='yes':
        return print('try again')
    else: print('next question')
    Question1=input('Are your hungry:')
    if Question1!='yes':
        return print('then lets go for a walk')
    else: print('next question')
    Question2=input('Do you want to eat at a restaurant?:')
    if Question2!='yes':
        return print('come at my place to eat')
    else: print('next question')
    Question3=input("Do you want to eat pizza:")
    if Question3!='yes':
        return print('Lets go and eat a burger then')
    else: print('Lets go and eat a pizza')

question()
    
