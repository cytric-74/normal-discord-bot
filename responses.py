import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message[0:1] == '!':
        if p_message[1:] == 'hello':
            return "hey there!! wassup?"

        if p_message[1:] == 'whats my lucky number':
            return str(random.randint(1, 100))

        if p_message[1:] == 'when is your bfs bday':
            return 'he was born by the end of the year on 28th'

        if p_message[1:] == 'intro':
            return "I'm Nina , nice to meet you ^ ^"

        if p_message[1:] == 'be my gf':
            return 'sorry im taken , but we could hangout sometimes ;)'

        if p_message[1:] == 'ily':
            return "Oh no , its time for you to touch some GRASS!!!! \n" \
                   "and meet some irl peoples..."

        if p_message[1:] == 'bye':
            return "ooh got bored of me ??? see ya dear "

        if p_message[1:] == 'help':
            return '`sorry im currently in a working phase. My boyfriend is a slow ass pussy. He doesnt wants to do me` \n use `?` to send private dms'


