print('hello')

#implementing variables
abc = input('Are you in USA or Europe?')
con = input('Which floor are you on?')


if (abc == 'USA') | (abc == 'Usa'):
    res = int(con) - 1
    print('In Europe it will be floor nr', res)
elif abc == 'Europe':
    res = int(con) + 1
    print('In USA it will be floor nr', res)
else: print('You have typed wrong country')
