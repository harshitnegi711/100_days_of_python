menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 13,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15,
    }
}
profit=0.00
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_coffee(drink_name,order_ingerdients):
    '''the gole of this function is to deduct the amount of ingredients from the machine'''
    for item in order_ingerdients:
        resources[item]-=order_ingerdients[item]
    print(f"here is your {drink_name} ☕")




def check_amount(amount):
    '''return true when order can be made and false when order cannot be made'''
    for item in amount:
        if resources[item]<=amount[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def process_coins():
    '''returns the total amount of coins inserted into the coffee machine'''
    print("Please insert the coins")
    total=int(input("how many 1 Rs coin :"))*1
    total+=int(input("how many 2 Rs coin :"))*2
    total+=int(input("how many 5 Rs coin :"))*5
    total+=int(input("how many 10 Rs coin :"))*10
    return total

def calculate_change(money, drink_cost):
    '''returns true when amount inserted is suffeicent otherwise retuen false'''
    if money>drink_cost:
        change=round(money - drink_cost, 2)
        print(f"here is your {change} Rs change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry amount is insuffient , Refunded")
        return False



is_on=True
while is_on:
    choice=input(print("what would you like to have ? (Espresso/Latte/Cappuccino) : "))
    if choice=="off":
        is_on=False
    elif choice=="report":
       print(f"water ={resources['water']}ml")
       print(f"milk ={resources['milk']}ml")
       print(f"coffee ={resources['coffee']}gm")
       print(f"money ={profit}Rs")
    else:
        drink=menu[choice]
        print(drink)
        if check_amount(drink["ingredients"]):
            payment=process_coins()
            if calculate_change(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])
