#A program that manages a list of countries and their capital cities.
country_dict = dict({"Nepal":"Kathmandu","Canada":"Ottawa"})

while True:
    input_country = input("Enter the name of a country: ")
    country = input_country.lower().capitalize()
    
    if country in country_dict:
        print("The Capital of {} is {}.".format(country,country_dict[country]))
        
    else:
        print("The Capital of {} is not recorded.".format(country))
        
        new_city = input("Please enter the Capital city name: ")
        country_dict[country] = new_city.lower().capitalize()
        
        print("{} Has been updated as the Capital of {}".format(country_dict[country],country))