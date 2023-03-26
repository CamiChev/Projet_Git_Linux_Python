import pandas as pd
import dash
from dash import html

#Convertir le txt en csv
lines = pd.read_csv('projetGitLinuxPython/prices.txt', sep = ',', names = ['price', 'time'])

#Initialisation de deux listes
prices = []
dates = []

for row in lines.itertuples(index=False):
    price = float(str(row.price).replace('$', '').replace(',', '').replace(' ', ''))  #Nettoyage de la synthaxe pour le csv
    time = row.time

    #Ajout à la liste
    prices.append(price)
    dates.append(time)

df = pd.DataFrame({'price': prices, 'time': dates})
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')

# Génération du csv
df.to_csv('prices.csv', index=False)

#print (df)



#Calcul de open et close
df['date'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
prices_between_8h_17h30 = df.set_index('time').between_time('08:00:00', '17:30:00')

open_price = prices_between_8h_17h30.iloc[0]['price']
close_price = prices_between_8h_17h30.iloc[-1]['price']

#Calcul volatility et return
daily_return = (close_price - open_price) / open_price
daily_volatility = prices_between_8h_17h30['price'].std()

#Affichage des résultats
print('Open Price:', open_price)
print('Close Price:', close_price)
print('Daily Return:', daily_return)
print('Daily Volatility:', daily_volatility)

#Enregistrement des métriques dans un fichier txt
with open("metrics.txt", "w") as f:
    f.write(f"Open price: {open_price}\n")
    f.write(f"Close price: {close_price}\n")
    f.write(f"Daily return: {daily_return}\n")
    f.write(f"Daily volatility: {daily_volatility}\n")

