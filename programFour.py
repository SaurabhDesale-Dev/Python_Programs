
def crypt(sentence):
    translation=''
    for element in sentence:
        if element in 'Aa':
            translation=translation +'1'
        elif element in 'Bb':
            translation=translation+ '2'
        elif element in 'Cc':
            translation=translation +'3'
        elif element in 'Dd':
            translation=translation +'4'
        elif element in 'Ee':
            translation=translation +'$'
        elif element in 'Ff':
            translation=translation +'+'
        elif element in 'Gg':
            translation=translation +'@'
        elif element in 'Hh':
            translation=translation +'^'
        elif element in 'Ii':
            translation=translation +'!'
        elif element in 'Jj':
            translation=translation +'%'
        elif element in 'Kk':
            translation=translation+'&'

        else:
            translation ==translation +element

    return translation

    
print(crypt(input('What do you want to crypt : ')))