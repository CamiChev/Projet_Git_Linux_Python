#Telechargement des donnees
curl -s https://coinpaprika.com/coin/wbtc-wrapped-bitcoin/ -o /home/camche/Projet/file.html
#Visualiser
#more file.html


#Recuperer prix et creation nouveau dossier (on cherche le prix a la ligne "coinPrice" et on cherche la ligne juste apres pour avoir le prix seulement)
price=$(grep "coinPrice" /home/camche/Projet/file.html -A1 | tail -1)

#Affichage date et temps
date="$(date +"%Y-%m-%d %H:%M:%S")"

echo "$price, $date" >> /home/camche/Projet/prices.txt

crontab -e */5 * * * * /home/camche/Projet/script.sh
