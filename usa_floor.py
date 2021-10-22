print('hello')

#implementing variables
abc = input('Are you in USA or Europe?')
con = input('Which floor are you on?')

try:
    res = int(con)
    if (abc == 'USA') | (abc == 'Usa'):
        res = res - 1
        print('In Europe it will be floor nr', res)
    elif abc == 'Europe':
        res = res + 1
        print('In USA it will be floor nr', res)
    else: print('You have typed wrong country')
except:
    print('User has put word', con,'which is not a number')
    res = 0

#abs
