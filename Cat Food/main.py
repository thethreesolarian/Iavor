cats_count = int(input())
food_per_day = 0.0
food_price = 12.45

# Тук създавам речник(dictionary). Ще прегледаш видеото от линка
# за да разбереш как работят речниците: https://www.youtube.com/watch?v=U7NcF8lsPo4&ab_channel=HackBulgaria
# Речникъ има три ключа, носещи името на всяка група и начална 
# стойност 0, където ще трупаме броя на котките
cats_groups = {"Group 1:": 0,
               "Group 2:": 0,
               "Group 3:": 0}

for cats in range(cats_count):
    
    food_amount = int(input())
    
    # Спрямо количеството храна за дадена котка
    # разпределям всяка котка, според предписанието по групи
    if food_amount >= 100 and food_amount < 200:
       cats_groups['Group 1:'] += 1 
    elif food_amount >= 200 and food_amount < 300:
       cats_groups['Group 2:'] += 1 
    elif food_amount >= 300 and food_amount < 400:
       cats_groups['Group 3:'] += 1 
            
    food_per_day += food_amount

# Принтирам за всяка група броят на котките в групата, 
# взимайки този брой от речника. В речника, срещу всеки 
# ключ, в случая всеки ключ носи името на група, има 
# стойност, която стойност е броя на котките в нея.
for group in cats_groups:
    print(group, cats_groups[group], "cats.")
    
food_per_day = (food_per_day/1000) * food_price
print(f'Price for food per day: {round(food_per_day, 2)}lv.')