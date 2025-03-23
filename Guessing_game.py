import random

def guessing_game():
    try:
        maximum=int(input('Please tell me the max value. \n'))
        minimum=int(input('Please tell me the min value. \n'))
        if maximum<=minimum:
            print('Invalid range. Min must be less than max')
            return

        numero=random.randint(minimum,maximum)
        tries=0
        
        x=int(input('Now, try to guess my number! \n'))
        
        while x != numero:
            try: 
                tries += 1
                if x < numero:
                    x=int(input('Too low! Try again. \n'))
                elif x > numero:
                    x=int(input('Too high! Try again. \n'))
            except ValueError:
                print("That's not an integer! \n")
        if tries == 0:
            print('Wow! You guessed it at your first try!')
        else:
            print(f'Congratulations, you guessed it at {tries} tries!')
    except ValueError:
        print('Invalid input of range. Please enter integers')
guessing_game()
