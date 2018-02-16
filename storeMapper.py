#!/bin/python
import json

# with open("oremWinco.json") as infile:
#     jsonString = infile.readlines()
#     print jsonString 
#     store = json.loads(jsonString)

store = {
    "Produce": [
        "apples",
        "bananas",
        "onion",
        "lettuce",
        "carrots",
        "potatoes",
        "lime"
    ],
    "Bulk Foods": [
        "rice",
        "popcorn",
        "hot chocolate"
    ],
    "4": [
        "deodorant",
        "soap",
        "shampoo",
        "toothpaste",
        "floss",
        "razors"
    ], 
    "5" : [
        "juice",
        "ketchup",
        "ranch"
    ],
    "6" : [
        "tortillas",
        "ramen",
        "salsa",
        "broth",
        "soup",
        "mexican foods"
    ],
    "7" : [
        "tuna",
        "seasoning",
        "gravy packets",
        "pasta seasoning",
        "fajita seasoning",
        "pasta",
        "beans"
    ], 
    "8" : [
        "peanut butter",
        "jam",
        "jelly",
        "honey",
        "flour",
        "sugar",
        "brown sugar",
        "birthday candles",
        "syrup",
        "cake mix",
        "pepper"
    ],
    "9": [
        "cereal",
        "oatmeal",
        "granola bars",
        "granola"
    ],
    "Deli" : [
        "cheese",
        "beef",
        "sausage"
    ],
    "10" : [
        "toilet paper",
        "paper towels"
    ],
    "11" : [
        "frozen corn",
        "corn",
        "peas",
        "frozen peas",
        "chicken nuggets",
        "chicken patties"
    ],
    "12": [
        "fries",
        "hash browns"
    ],
    "13": [
        "butter",
        "milks",
        "yogurt"
    ],
    "14": [
        "pretzels",
        "tortilla chips"
    ],
    "15": [
        "gatorade"
    ]
}

# items = "pepper\nhot chocolate\ndeodorant \ncorn\nToilet paper\nToilet cleaner\nSandwich bags \nApples\nCereal\nGranola\nGatorade \nGranola bars\nCrackers\nOther healthy stuff\nMilk \nChicken patties\nTater tots\nSausage\nEggs\nrice\nFajita seasoning\nPepper \nTortilla Chips\nLime\nOnion \nBread\nTortillas\nCheese \nSpaghetti squash\nGravy"
# items = items.split('\n')
items = []
while True: 
    item = raw_input()
    if item == "done":
        break
    if item != "":
        items.append(item)

print "\n".join(items)

notPlaced = []
mappedItems = {}

# def isin(lst, item):
#     if item == "deodorant": 
#         print "wtf"
#     for l in lst:
#         if l == item:
#             return True
#     return False

for item in items:
    item = item.lower()
    # print item
    place = False
    for location in store:
        print "checking if ", item, " is in ", store[location]
        locationInventory = store[location]
        print item in locationInventory
        if item in locationInventory:
            print "found that ", item, " is in ", store[location]
            if location not in mappedItems:
                mappedItems[location] = []

            mappedItems[location].append(item)
            placed = True
            break

    if not placed:
        notPlaced.append(item)

print mappedItems
print notPlaced
print "\n"
for location in sorted(mappedItems):
    print location, ": "
    for item in mappedItems[location]:
        print item
    print "\n"

print "Not Placed: "
for item in notPlaced:
    print item