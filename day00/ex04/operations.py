# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 14:12:41 by alpascal          #+#    #+#              #
#    Updated: 2020/03/10 14:44:00 by alpascal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    if len(sys.argv) > 3:
        print ('InputError: too many arguments')
        return
    if len(sys.argv) < 3:
        print ('Usage: python operations.py <number1> <number2>')
        print ('Example:')
        print ('    python operations.py 10 3')
        return
    for char in sys.argv[1]:
        if char.isdigit() != 1:
            print ('InputError: only numbers')
            return
    for char in sys.argv[2]:
        if char.isdigit() != 1:
            print ('InputError: only numbers')
            return
    print (f'Sum:         ${int(sys.argv[1]) + int(sys.argv[2])}')
    print (f'Difference:  ${int(sys.argv[1]) - int(sys.argv[2])}')
    print (f'Product:     ${int(sys.argv[1]) * int(sys.argv[2])}')
    if int(int(sys.argv[2]) != 0):
        print (f'Quotient:    ${int(sys.argv[1]) / int(sys.argv[2])}')
        print (f'Modulo:      ${int(sys.argv[1]) % int(sys.argv[2])}')
    else:
        print (f'Quotient:    Error (div by zero)')
        print (f'Modulo:      Error (modulo by zero)')

main()
