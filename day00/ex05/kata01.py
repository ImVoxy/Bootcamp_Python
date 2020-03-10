# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 15:16:41 by alpascal          #+#    #+#              #
#    Updated: 2020/03/10 15:23:25 by alpascal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def main():
    languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
    print (f'Python was created by {languages["Python"]}')
    print (f'Ruby was created by {languages["Ruby"]}')
    print (f'PHP was created by {languages["PHP"]}')

main()
