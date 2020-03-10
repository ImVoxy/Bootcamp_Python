# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 14:21:37 by alpascal          #+#    #+#              #
#    Updated: 2020/03/09 15:18:44 by alpascal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def main():
    if len(sys.argv) != 2:
        print ("ERROR")
        return
    for character in sys.argv[1]:
        if character.isdigit() != 1:
            print ("ERROR")
            return
    num = int(sys.argv[1])
    if num == 0:
        print("I'm Zero.")
    elif num / 2 == num // 2:
        print("I'm Even.")
    elif num / 2 != num // 2:
        print("I'm Odd.")
    else:
        print("ERROR")

main()
