import re

secret_code = ['blue', 'red']
colors = ['blue', 'red', 'yellow', 'green']
attempt = 0


def game(secret_code, attempt):
    attempt = attempt + 1
    print('Attempt number: '+ str(attempt))
    
    user_input = input('Chose 2 colors between blue, red, yellow, green:')
    user_input_list = re.split(",", user_input)

    color_is_okay = is_input_a_color(colors, user_input_list)
    if color_is_okay == True:
        good_combinasion = is_it_the_combinaison(user_input_list, secret_code)
        if good_combinasion == True:
            print('You win!')
        else:
            game(secret_code, attempt)
    else:
        game(secret_code, attempt)
    



def is_it_the_combinaison(user_input_list, secret_code):
    for color in secret_code:
        for user_color in user_input_list:
            if color == user_color:
                return True
            else:
                return False
                

def is_input_a_color(colors, user_input_list):
    if set(colors) & set(user_input_list):
        return True
    else:
        print('Choose colors between green, blue, red and yellow')
        return False

game(secret_code, attempt)
