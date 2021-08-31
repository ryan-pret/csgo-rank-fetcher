from bs4 import BeautifulSoup
import requests
import cloudscraper
import sys

ranks = ["Silver 1", "Silver 2", "Silver 3", "Silver 4", "Silver Elite", "Silver Elite Master",
         "Gold Nova 1", "Gold Nova 2", "Gold Nova 3", "Gold Nova Master", "Master Guardian 1",
         "Master Guardian 2", "Master Guardian Elite", "DMG", "LE", "LEM", "Supreme", "Global"]

def scrape_csgostats(search_term):
    """Function for returning player rank"""
    url = "https://csgostats.gg/player/" + search_term
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    soup = BeautifulSoup(scraper.get(url).text, "html.parser")
    images = soup.find_all('img')
    count = 0
    rank = ""
    for image in images:
        if count == 1:
            rank = image['src']
            break
        count = count + 1
    return rank

csgo_ranks = scrape_csgostats(sys.argv[1])
next_count = 0
act_rank = ""
for word in csgo_ranks.split("/"):
    if next_count == 5:
        act_rank = word
    next_count = next_count + 1

act_rank = int(act_rank.split(".")[0])

print(ranks[act_rank-1])