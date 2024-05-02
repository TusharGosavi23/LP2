Questions = [
    'Do you have cough?',
    'Do you have fever?',
    'Do you have Cold?',
    'Do you have sour Throat?',
    'Do you have stuffy Nose?',
    'Do you have Headache?',
    'Do you have itchy throat?'
]

Threashold = {
    'Mild' : 30,
    'Severe' : 50,
    'Extreme' : 70
}

def expertSystem (Questions, Threashold):
    score = 0
    for question in Questions:
        print(question + ' (Y/N)')
        ans = input('> ')
        if (ans.lower() =='y'):
            print('On the scale of 1 to 10 , How bad it is : ')
            ip = input('> ')
            while ((not ip.isnumeric()) or int(ip) < 1 or int(ip) > 10):
                print("Enter valid number ")
                ip = input('> ')
            score  += int(ip)
    print('\n')
    if(score >= Threashold['Extreme']):
        print('Its Extreme')
    elif(score >= Threashold['Severe']):
        print('Its severe')
    elif(score >= Threashold['Mild']):
        print('Its Mild')
    else:
        print('No Symptoms')
        
print("Welcome to the COVID 19 Expert System\n-----give correct answers-----\n")
expertSystem(Questions, Threashold)