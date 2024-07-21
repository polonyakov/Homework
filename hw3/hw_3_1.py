try:
    with open('cities.txt' , 'r') as enter:
        text_1 = enter.readlines()
        text = sorted(text_1)
except FileNotFoundError:
    print('file is not founded')
n = input('enter min population')
with open('filtered_cities.txt' , 'w') as output:
    for i in text:
        cities_pop = i.split(':')
        cities_pop[0] = cities_pop[0].strip()
        cities_pop[1] = cities_pop[1].strip()
        if int(cities_pop[1]) > int(n):
            print(f'{str(cities_pop[0])} : {str(cities_pop[1])}',file=output)