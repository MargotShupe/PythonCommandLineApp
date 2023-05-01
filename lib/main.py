from peewee import *


db = PostgresqlDatabase('countries', user='', password='',host='localhost', port=5432)

#Connect to the database
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Countries(BaseModel):
    country = CharField()
    capital = CharField()

#Create the table
db.drop_tables([Countries]) #first, drop the tables if they exist
db.create_tables([Countries]) #then, create the tables from scratch

card1 = Countries(country = 'Afghanistan', capital = 'Kabul')
card1.save()

card2 = Countries(country = 'Albania', capital = 'Tirana')
card2.save()

card3 = Countries(country = 'Algeria', capital = 'Algiers')
card3.save()

card4 = Countries(country = 'Andorra', capital = 'Andorra la Vella')
card4.save()

card5 = Countries(country = 'Angola', capital = 'Luanda')
card5.save()

card6 = Countries(country = 'Antigua & Barbuda', capital = 'Saint Johns')
card6.save()

card7 = Countries(country = 'Argentina', capital = 'Buenos Aires')
card7.save()

card8 = Countries(country = 'Armenia', capital = 'Yerevan')
card8.save()

card9= Countries(country = 'Australia', capital = 'Canberra')
card9.save()

card10 = Countries(country = 'Austria', capital = 'Vienna')
card10.save()

card11 = Countries(country = 'Azerbaijan', capital = 'Baku')
card11.save()

card12 = Countries(country = 'The Bahamas', capital = 'Nassau')
card12.save()

card13 = Countries(country = 'Bahrain', capital = 'Manama')
card13.save()

card14 = Countries(country = 'Bangladesh', capital = 'Dhaka')
card14.save()

card15 = Countries(country = 'Barbados', capital = 'Bridgetown')
card1.save()

card16 = Countries(country = 'Belarus', capital = 'Minsk')
card16.save()

card17 = Countries(country = 'Belgium', capital = 'Brussels')
card17.save()

card18 = Countries(country = 'Belize', capital = 'Belmopan')
card18.save()

card19 = Countries(country = 'Benin', capital = 'Porto-Novo')
card19.save()

card20 = Countries(country = 'Bhutan', capital = 'Thimphu')
card20.save()

card21 = Countries(country = 'Bolivia', capital = 'Sucre')
card21.save()

card22 = Countries(country = 'Bosnia & Herzegovina', capital = 'Sarajevo')
card22.save()

card23 = Countries(country = 'Botswana', capital = 'Gaborone')
card23.save()

card24 = Countries(country = 'Brazil', capital = 'Brasilia')
card24.save()

def game():
    print('Do you want to review the capitasl of the countries or create a new card')
    answer = input('Type: review or create')
    if answer == 'review':
        review()
    elif answer == 'create':
        create()
    else: 
        print('Invalid input')
        game()

def create():
    coun = input('Country: \n')
    cap = input('Capital: \n')
    new = Countries(country=coun, cap=capital)
    new.save()
    print(f'New country: {new.country} and capital:{new.capital}')
    game()

def review():
    correct = 0
    i = int(input("How many countries would you like to study? "))
    total = i
    for card in Countries.select():
        if i > 0:
            i -= 1
            if input(f"{card.country}\n") == card.capital:
                print(f"The answer is {card.capital}")
                correct += 1
                print(f"Score: {correct}/{total}")
            else:
                print(f"The answer is {card.capital}")
                print(f"Score: {correct}/{total}")
    percent = (correct/total)*100
    print(f"{percent}%")           
    play_again = str(input("Would you like to play again? Type yes or no "))
    if play_again == 'yes':
        review()
    else:
        game()
game()