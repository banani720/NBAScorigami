import tweepy as twpy
import pandas as pd
from nba_api.stats.endpoints import teamgamelog as games
from nba_api.stats.static import teams
import json

# Set up keys and secrets for twitter API
api_consumer_key = "OJdv9UD3PdE6PYujpnKtdZHx2"
api_secret = "wpgAhU2fXqmOpYm4uO8bbVCQGjJlRNX2g4MMSc4LVjv7OU4NQV"
access_token = "1356769772776558593-YgivhZ3eC5gFOMZ2IVPanfIuQwSFDw"
access_secret = "JB4oJadsuZS7Ks1BRlbyX4VuuHoieMFAschbClmhQNS4U"

auth = twpy.OAuthHandler(api_consumer_key, api_secret)
auth.set_access_token(access_token, access_secret)

# Auth the twitter API
api = twpy.API(auth)

all_teams = teams.get_teams()
teams = pd.DataFrame(all_teams)
gamelog_array = []
for id in teams.id:
    for i in range(2002, 2003):
        game_list = games.TeamGameLog(team_id=id, season=i).get_json()
        gamelog_array.append(game_list)
print(gamelog_array[0])
