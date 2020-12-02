from mongoengine import *
from datetime import datetime
from pytz import timezone
from extra import *

class Meals(EmbeddedDocument):
    present = BooleanField(required=True, default=False)
    dishes = ListField(StringField(max_length=20))
    cooks = ListField(StringField(max_length=20))


class Day(EmbeddedDocument):
    date = StringField()
    meal = DictField(EmbeddedDocumentField(Meals))


class MealPlanner(Document):
    # Meal plan's date of creation
    creation_date = DateTimeField(default=datetime.now(timezone('US/Pacific')), required=True)
    # name of meal planner
    name_mealplan = StringField(max_length=20, unique=True)
    # User that created the meal planner
    user_name = StringField(max_length=20)
    # days inside of here
    days = DictField(EmbeddedDocumentField(Day))
    meta = {'collection': 'meal_plan'}
    # meta = {'allow_inheritance': False}


