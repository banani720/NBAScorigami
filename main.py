import tweepy as twpy
import pandas as pd
from nba_api.stats.endpoints import teamgamelog as games
import json
import numpy as np
# Set up keys and secrets for twitter API
api_consumer_key = "OJdv9UD3PdE6PYujpnKtdZHx2"
api_secret = "wpgAhU2fXqmOpYm4uO8bbVCQGjJlRNX2g4MMSc4LVjv7OU4NQV"
access_token = "1356769772776558593-YgivhZ3eC5gFOMZ2IVPanfIuQwSFDw"
access_secret = "JB4oJadsuZS7Ks1BRlbyX4VuuHoieMFAschbClmhQNS4U"

auth = twpy.OAuthHandler(api_consumer_key, api_secret)
auth.set_access_token(access_token, access_secret)

# Auth the twitter API
api = twpy.API(auth)

hawks_data = games.TeamGameLog(team_id=1610612737, season="2002-03").get_json()
hawks_json = json.loads(hawks_data)

df = pd.json_normalize(hawks_json)

result_set_array = df["resultSets"].to_numpy()

for i in result_set_array:
    for j in i:
        results_json = json.dumps(j, indent=2)
print(results_json)






