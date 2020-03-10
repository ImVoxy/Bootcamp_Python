# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 16:13:13 by alpascal          #+#    #+#              #
#    Updated: 2020/03/10 18:40:20 by alpascal         ###   ########.fr        #
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

def delete_recipe(recipe):
    del cookbook[recipe]

def add_recipe(recipe, ingredients, meal, prep_time):
    cookbook[recipe] = {'ingredients' : ingredients, 'meal' : meal, 'prep_time' : prep_time}

def print_book():
    print ('List of available recipes:\n')
    for recipe in cookbook:
        print('- %s' % recipe)

def main():
    cookbook = {
               'sandwich' : {    'ingredients' : ['ham', 'bred', 'cheese', 'tomatoes'],
                                'meal' : 'lunch', 'prep_time' : 10},
                'cake' :     {   'ingredients' : ['flour', 'sugar', 'eggs'],
                                'meal' : 'dessert', 'prep_time' : 60},
                'salad' :    {    'ingredients' : ['avocao', 'arugula', 'tomatoes', 'spinach'],
                                'meal' : 'lunch', 'prep_time' : 15}
            }

    print('     Cookbook\n')
    print('What can i do for you ? \n')
    print('1 - Add a new recipe')
    print('2 - Delete a recipe')
    print('3 - Recipe list')
    print('4 - See the whole cookbook')
    print('5 - See a recipe')
    print('6 - Quit')
    num = input('>>')

    if num == 1:
        print('Name of recipe :')
    print (num)

main()
