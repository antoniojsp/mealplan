# from mongoengine import *
# from datetime import datetime
# from pytz import timezone
from extra import *


db = connect('Test')
db.drop_database('Test')
#create ona planner and add 3 days with meals.
meal_list = [['Breakfast', 'Lunch'],['Lunch', 'Snack', 'Dinner'],['Breakfast', 'Lunch', 'Dinner']]
create_mealplan("2020-10-10", "2020-10-12", "trip", "antonio", meal_list)
# add_meal("trip", "2020-10-11", "Breakfast")

add_dish("trip","2020-10-12", "Breakfast", "foodie")
add_dish("trip","2020-10-12", "Breakfast", "foodie1")
add_dish("trip","2020-10-12", "Breakfast", "foodie2")
add_dish("trip","2020-10-12", "Breakfast", "foodie3")

add_cook("trip","2020-10-12", "Breakfast", "cook")
add_cook("trip","2020-10-12", "Breakfast", "cook1")
add_cook("trip","2020-10-12", "Breakfast", "cook2")
add_cook("trip","2020-10-12", "Breakfast", "cook3")

MealPlanner()



