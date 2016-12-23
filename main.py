#! /usr/bin/env python
import random
from encrypt import scramble

def robot_answer():
    answers = [
        'Hey',
        'Nice weather today, eh?',
        "Have you seen that movie with that guy doing that thing? It's awesome!"
        ""
    ]
    return scramble(random.choice(answers))


def main_chat():
    while True:
        message = raw_input('Type your secret message, human! >')
        encrypted_message = scramble(message)
        print 'Encrypted your message: %s' % encrypted_message
        print 'Pretending to send it to the other side...'
        reply = robot_answer()
        print 'Received encrypted message from the other side: %s' % reply
        decrypted_reply = scramble(reply)
        print 'Decrypted reply: %s' % decrypted_reply


main_chat()
