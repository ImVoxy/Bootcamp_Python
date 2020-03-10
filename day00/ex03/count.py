# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 15:44:54 by alpascal          #+#    #+#              #
#    Updated: 2020/03/10 14:12:17 by alpascal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(*arg):

    text = ""
    total, up, low, space, punct = 0, 0, 0, 0, 0
    if len(arg) != 1:
        if len(arg) != 0:
            print ("ERROR")
            return
        else:
            print ("What is the text to analyse?")
            for line in sys.stdin:
                text += line
            text_analyzer(text)
            return
    text = arg[0]

    for char in text:
        total += 1
        if char.islower():
            low += 1
        elif char.isspace():
            space += 1
        elif char.isupper():
            up += 1
        elif char in string.punctuation:
            punct += 1
    print (f'The text contains ${total} caracters:\n')
    print (f'- ${up} upper letters\n')
    print (f'- ${low} lower letters\n')
    print (f'- ${punct} punctuation marks\n')
    print (f'- ${space} spaces\n')

