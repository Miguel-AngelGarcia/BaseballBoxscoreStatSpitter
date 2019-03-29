from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.espn.com/mlb/boxscore?gameId=401074743'

# grabbing the page
uClient = uReq(my_url)

# offloads content into variable
page_html = uClient.read()

uClient.close()

# does html parsing
page_soup = soup(page_html, "html.parser")

test = page_soup.findAll("tbody", {"class":"athletes"})
t = test[0]

index = range(2,9)
stats = {2:'AB', 3: 'R', 4: 'H', 5:'RBI', 6:'BB', 7:'K', 8:'AVG', 9:'OBP', 8:'SLG'}


# for t in stats:
print(t.span.contents[0])
for x in index:
    print(t.tr.contents[x].text)
    print(stats[x])
    