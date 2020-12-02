from models import *
import pandas as pd

# helper functions
def date_range(start, end):
    temp_range = pd.date_range(start=start, end=end) # return a datetimeindex
    date_rng = temp_range.date

    lista = []
    for i in date_rng:
        lista.append(i.strftime('%Y-%m-%d'))

    return lista

#add to mongodb
def create_mealplan(start_date:str, end_date:str, name_plan:str, user_name:str, meals:list):
    list_dates = date_range(start_date, end_date)
    mealplan_temp = MealPlanner(user_name=user_name, name_mealplan=name_plan)
    # meals1 = Meals(dishes=[], cooks=[])
    list_meals = ["Breakfast", "Brunch", "Lunch", "Snack", "Dinner"]

    for i, j in zip(list_dates, meals):
        day_temp = Day(date=i)
        for k in list_meals:
            if k in j:
                day_temp.meal[k] = Meals(present=True)
            else:
                day_temp.meal[k] = Meals(present=False)

        temp = i.replace("-", "_")
        mealplan_temp.days[temp] = day_temp

    mealplan_temp.save()

def add_day(name_plan:str, date:str, meals:list):
    day = Day(date=date)

    for i in meals:
        day.meal[i] = Meals(dishes=[], cooks=[])

    date = date.replace("-", "_")
    location = "set__days__" + date

    MealPlanner.objects(name_mealplan=name_plan).update(**{location : day})

def add_dish(name_plan:str, date:str, meal:str, dish:str):
    date = date.replace("-", "_")
    location = "push__days__" + date + "__meal__"+ meal +"__dishes"
    MealPlanner.objects(name_mealplan=name_plan).update(**{location : dish})

def add_cook(name_plan:str, date:str, meal:str, cook:str):
    date = date.replace("-", "_")
    location = "push__days__" + date + "__meal__"+ meal +"__cooks"
    MealPlanner.objects(name_mealplan=name_plan).update(**{location : cook})

def add_meal(name_plan:str, date:str, meal:str):
    date = date.replace("-", "_")
    location = "set__days__" + date + "__meal__"+ meal
    meal = Meals(dishes=[], cooks=[])
    MealPlanner.objects(name_mealplan=name_plan).update(**{location : meal})