# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 16:13:13 by alpascal          #+#    #+#              #
#    Updated: 2020/03/11 11:36:46 by alpascal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def print_recipe(recipe):
    print(f'Recipe for {recipe}:')
    print(f'Ingredients list:' , end ='')
    print(cookbook[recipe]['ingredients'])
    print('to be eaten for ', end='')
    print(cookbook[recipe]['meal'])
    print('takes ', end='')
    print(cookbook[recipe]['prep_time'], end='')
    print(' minutes of cooking.')

def del_recipe(recipe):
    del cookbook[recipe]

def add_recipe(recipe, ingredients, meal, prep_time):
    cookbook[recipe] = {'ingredients' : ingredients, 'meal' : meal, 'prep_time' : prep_time}

def print_book():
    print ('List of available recipes:\n')
    for recipe in cookbook:
        print('- %s' % recipe)


def main():
    while 1:
        print('     Cookbook\n')
        print('What can i do for you ? \n')
        print('1 - Add a new recipe')
        print('2 - Delete a recipe')
        print('3 - Recipe list')
        print('4 - See the whole cookbook')
        print('5 - See a recipe')
        print('6 - Quit')
        num = int(input('>>'))
        ingredients = []
        if num == 1:
            name = input('Name of recipe >>')
            while num == 1:
                f = input('type an ingredient >>')
                ingredients.append(f)
                num = int(input('1 - Add ingredient\n2 - End of ingredient list\n>>'))
            meal = input('type of meal >>')
            prep_time = input('preparation time(min) >>')
            add_recipe(name, ingredients, meal, prep_time)
            num = 1

        if num == 2:
            print('name of recipe to delete')
            print_book()
            recipe = input('>>')
            del_recipe(recipe)

        if num == 3:
            print_book()

        if num == 4:
            for r in cookbook:
                print_recipe(r)

        if num == 5:
            print('Name of recipe you want to see')
            print_book()
            name = input('>>')
            print_recipe(name)

        if num == 6:
            print('See you later !')
            exit()


cookbook = {
              'sandwich' : {    'ingredients' : ['ham', 'bred', 'cheese', 'tomatoes'],
                                'meal' : 'lunch', 'prep_time' : 10},
              'cake' :     {   'ingredients' : ['flour', 'sugar', 'eggs'],
                                'meal' : 'dessert', 'prep_time' : 60},
              'salad' :    {    'ingredients' : ['avocao', 'arugula', 'tomatoes', 'spinach'],
                                'meal' : 'lunch', 'prep_time' : 15}
            }
main()
