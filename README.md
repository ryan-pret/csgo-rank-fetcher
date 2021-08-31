# csgo-rank-fetcher
## Brief
This is a small python script I made which is able to retrieve a player's cs:go competitve rank. It scrapes the website (csgostats)[https://csgostats.gg/], to retrieve the user's rank information and the prints it to terminal.

## Usage:
install the requirements located in the `requirements.txt` file using pip (recommended to run in a virtual environment):
```
pip3 install -r requirements.txt
```

And then run the python script using the following arguements.
```
python3 csgo_stat.py <steam_id>
```

where `<steam_id>` is your STEAMID64, which you can find using the site (HERE)[https://www.steamidfinder.com/].

## Known Issues
Currently the module `cloudscraper` which was used to bypass the DDOS-protection on the website has upgraded some of it's features for premium users only, so the cloudscraper instance cannot bypass the DDOS-protection any longer. The program worked of 06/02/2021
