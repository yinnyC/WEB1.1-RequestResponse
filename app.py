from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/penguins')
def penguin():
    """Shows off the animal"""
    return 'Penguins are cute!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'


@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Display a funny story to the user with the 2 strings they typed."""
    return f'Would it be a {adjective} idea to add {noun} onto a pizza?'


@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """ Display the multiply result to the user that changes based on the 2 numbers user give. """
    if number1.isdigit() and number2.isdigit():
        return f'{number1} times {number2} is {int(number1)*int(number2)}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'


@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """ Display a message to the user that will repeat a string a given number of times."""
    if n.isdigit():
        sayntimes_msg = [word for _ in range(int(n))]
        return " ".join(sayntimes_msg)
    else:
        return 'Invalid input. Please try again by entering a word and a number!'


@app.route('/reverse/<word>')
def reverse(word):
    """ Display a reversed message to the user based on their input. """
    return word[::-1]


@app.route('/strangecaps/<word>')
def strangecaps(word):
    """ Display a message that will output a given word in “strange caps” to the user based on their input. """
    word = list(word)
    for i in range(0, len(word)):
        if i % 2 == 0:
            word[i] = word[i].lower()
        else:
            word[i] = word[i].upper()
    return "".join(word)


@app.route('/dicegame')
def dicegame():
    """ Display a dice game result based on the random generated 1-6 number. """
    result = randint(1, 6)
    if result is 6:
        return f'You rolled a {result}. Yon won!'
    else:
        return f'You rolled a {result}. Yon lost!'


if __name__ == '__main__':
    app.run(debug=True)
