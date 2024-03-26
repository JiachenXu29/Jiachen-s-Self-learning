import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=30&term=" + sys.argv[1])

# find the first song from this band 
# print(json.dumps(response.json(), indent=2))
#___


# get the first 30 songs from this band
o = response.json()
for result in o ["results"]:
    print(result["trackName"])


