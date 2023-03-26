#Importation de l'url dans file.html
curl -s https://coinpaprika.com/coin/wbtc-wrapped-bitcoin/ -o projetGitLinuxPython/file.htm


#Importation du prix dans la variable price
price=$(grep "coinPrice" projetGitLinuxPython/file.html -A1 | tail -1)
echo $price

#Affichage date
date="$(date +"%Y-%m-%d %H:%M:%S")"

#Enregistrement du prix et date dans price.txt
echo "$price, $date" >> projetGitLinuxPython/prices.txt

