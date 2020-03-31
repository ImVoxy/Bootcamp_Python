# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 12:28:51 by alpascal          #+#    #+#              #
#    Updated: 2020/03/11 15:50:06 by alpascal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import datetime
from datetime import date
from recipe import Recipe

class Book:

    def __init__(self, name):
        self.recipes_list = {
                          'starter' : {'recipes' : []},
                          'lunch' : {'recipes' : []},
                          'dessert' : {'recipes' : []}
                        }
        self.last_update = datetime.now()
        self.creation_date = date.today()
        self.name = name

    def add_recipe(self, recipe):
        self.last_update = datetime.now()
        newRecipe = Recipe(recipe)
        while 1:
            f = input('Type an ingredient >>')
            newRecipe.add_ingredient(f)
            num = int(input('1 - Add ingredient\n2 - End of ingredient list\n>>'))
            if num != 1:
                break
        while 1:
            num = int(input('Select the cooking level (1 to 5)\n>>'))
            if num >= 1 and num <= 5:
                newRecipe.cooking_lvl = num
                break
            print('Please select a valid level')
        num = int(input('What cooking time ?(min)\n>>'))
        newRecipe.cooking_time = num
        num = int(input('Press 1 to add a description\n>>'))
        if num == 1:
            txt = input('Enter your description\n>>')
            newRecipe.description = txt
        while 1:
            meal = int(input('Select the type of meal\n1 - starter\n2 - lunch\n3 - dessert\n>>'))
            if meal == 1:
                newRecipe.meal = 'starter'
                self.recipes_list['starter']['recipes'].append(newRecipe)
                break
            elif meal == 2:
                newRecipe.meal = 'lunch'
                self.recipes_list['lunch']['recipes'].append(newRecipe)
                break
            elif meal == 3:
                newRecipe.meal = 'dessert'
                self.recipes_list['dessert']['recipes'].append(newRecipe)
                break
            else:
                print('Please, enter a valid key')


#       print(livre.recipes_list['lunch']['recipes'][0].description)
