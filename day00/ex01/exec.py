# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 12:12:17 by alpascal          #+#    #+#              #
#    Updated: 2020/03/09 14:18:07 by alpascal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    test = ""
    for str in sys.argv[1:]:
        if test:
            test += ' '
        test += ft_reverse(str)
    i = len(test) - 1
    while i >= 0:
        print(test[i], end='')
        i = i - 1
    print('')

def ft_reverse(str):
    test = ""
    for char in str:
        if char.isupper():
            test += char.lower()
        if char.islower():
            test += char.upper()
    return test

main()
