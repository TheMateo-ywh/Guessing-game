import random

def guessing_game():

    maximo=int(input('Please tell me the max value. \n'))
    minimo=int(input('Please tell me the min value. \n'))

    numero=random.randint(minimo,maximo)
    print(numero)
    x=int(input('Now, try to guess my number! \n'))
    print('Wow! You guessed it at your first try!') if x==numero else None
    while x != numero:
        try: 
            x=int(input('Try again! \n'))
            if x==numero:
                print('Congratulations! You guessed it!')
        except ValueError:
            print("That's not an integer! \n")
guessing_game()