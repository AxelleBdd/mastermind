secret_code = ['blue', 'red']
colors = ['blue', 'red', 'yellow', 'green']
attempt = 0


def game(secret_code, attempt):
    user_colors = []
    attempt = attempt + 1
    print('Attempt: '+ str(attempt))

    choose_color(user_colors)
    good_answer = is_it_correct(secret_code, user_colors)
    if good_answer:
        print('You won in ' + str(attempt) + ' attempts')
    else:
        print('Try again')
        if attempt <=3:
            game(secret_code, attempt)


def choose_color(user_colors):
    first_color = input('Choose the first color between red, green, blue and yellow: ')
    is_input_in_colors(first_color, colors, user_colors)
    second_color = input('Choose the second color between red, green, blue and yellow: ')
    is_input_in_colors(second_color, colors, user_colors)


def is_input_in_colors(color, colors, user_colors):
    if color in colors:
        user_colors.append(color)
    else:
        input('Choose between red, green, blue and yellow: ')


def is_it_correct(secret_code, user_colors):
    if all(secret_code_list == user_colors_list for secret_code_list, user_colors_list in zip(secret_code, user_colors)):
        return True
    else:
        return False
    
game(secret_code, attempt)