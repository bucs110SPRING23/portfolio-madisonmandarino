import MeatandBread
import CheeseandSauces
import requests
import json

def build_sandwich():
    answer = input("Do you want to build a random sandwich? 1. Yes 0. No ")
    if answer == "1":
        spoonacular_api = MeatandBread.MeatandBread("ddb9e053039b40b19e144778437d1bae")
        usda_api = CheeseandSauces.CheeseandSauces("7cfb7lTG7v0qded3dmZ20tE4MeiKsx2ZHejLmTox")

        try:
            meat = spoonacular_api.get_random_meat()
            bread = spoonacular_api.get_random_bread()
            cheese = usda_api.get_random_cheese()
            sauce = usda_api.get_random_sauce()
        except requests.exceptions.RequestException as e:
            print(f"Failed to get sandwich ingredients: {e}")
            return

        sandwich = {"bread": bread, "meat": meat, "cheese": cheese, "sauce": sauce}

        with open('response.json', 'w') as outfile:
            json.dump(sandwich, outfile)

        print(f"Your sandwich has {meat} on {bread} with {cheese} and {sauce}.")
        print(f"Bread: {bread}, Meat: {meat}, Cheese: {cheese}, Sauce: {sauce}")
    elif answer == "0":
        print("FINE THEN, HAVE A GOOD DAY!")
    else:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")


if __name__ == '__main__':
    build_sandwich()
