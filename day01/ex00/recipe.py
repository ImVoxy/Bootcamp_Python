# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alpascal <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 12:12:09 by alpascal          #+#    #+#              #
#    Updated: 2020/03/11 14:58:13 by alpascal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
    cooking_lvl = -1
    cooking_time = -1
    ingredients = []
    description = "No description yet"
    recipe_type = ""

    def __init__(self, name):
        self.name = name
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    def __str__(self):
        txt = ""
        return txt
