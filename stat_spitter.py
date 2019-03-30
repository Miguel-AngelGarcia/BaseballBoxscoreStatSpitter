from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import itertools

my_url = 'http://www.espn.com/mlb/boxscore?gameId=401074743'

# grabbing the page
uClient = uReq(my_url)

# offloads content into variable
page_html = uClient.read()

uClient.close()

# does html parsing
page_soup = soup(page_html, "html.parser")

test = page_soup.findAll("tbody", {"class":"athletes"})
player_num = len(test)
range_end = player_num + 1

# t = test[0]


index = [2,3,4,5,6,7,9,10,11]
stats = {2:'AB', 3: 'R', 4: 'H', 5:'RBI', 6:'BB', 7:'K', 9:'AVG', 10:'OBP', 11:'SLG'}

filename = "angels_stats.csv"
f = open(filename, "w")

headers = "Player Name, AB, R, H, RBI, BB, K, AVG, OBP, SLG\n"

f.write(headers)

# for y in range(0, range_end):
for y in range(0, range_end):

    player = test[y]
# for t in stats:
    print(player.span.contents[0])
    f.write(player.span.contents[0] + " , ")
    for x in index:
        f.write(player.tr.contents[x].text + ", ")
        print(player.tr.contents[x].text, end=' ')
        print(stats[x])

    f.write("\n")
    print("")


for x in index:
    print(player.tr.contents[x].text, end=' ')
    print(stats[x])

    print("")

f.close()