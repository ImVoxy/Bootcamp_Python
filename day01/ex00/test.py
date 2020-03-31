# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 12:08:40 by alpascal          #+#    #+#              #
#    Updated: 2020/03/11 12:08:58 by alpascal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

def main():
    book_list = []
    print("Welcome to the Cookbook manager\nWhat can I do for you ?")
    while 1:
        num = int(input('1 - Chose an available Book\n2 - Create a new Book\n3 - Delete an existing Book\n4 - Quit\n>>'))
        if num == 1:
            for i in book_list:
                print('{:0>2} - {}'.format(i, book_list[i].name))
                test = i
            while 1:
                select = int(input('>>'))
                if select < 0 or select > test:
                    print('Please chose in the folowing list')
                else:
                    break
            print('what\'s next ?')
            while 1:
                num = int(input('1 - See the recipe list\n2 - See a recipe\n3 - Add a recipe\n4 - Back\n>>'))
                if num == 1 or num == 2:
                    for i in book_list:
                        print('{:0>2} - {}'.format(i, book_list[select][i].name))
                        test = i
                    if num == 2:
                        while 1:
                            select = int(input('>>'))
                            if select < 0 or select > test:
                                print('Please chose in the folowing list')
                            else:
                                break
        elif num == 2:
            name = input('Enter the name of your book !\n>>')
            name = Book('name')
            book_list.append(name)
        elif num == 3:
            for i in book_list:
                print('{:0>2} - {}'.format(i, book_list[i].name))
                test = i
            while 1:
                select = int(input('>>'))
                if select < 0 or select > test:
                    print('Please chose in the folowing list')
                else:
                    break
            book_list[select].add_recipe
        elif num == 4:
            print('All datas erased...\nSee you later !')
            exit()
        else:
            print('C`\'mon chose between the 4 possibilities..')

main()
