from pantheon import pantheon
import pandas as pd
import asyncio

server = "na1"

#Put in own dev key to test
api_key = "RGAPI-7f7f0325-a14c-42ad-ba19-75068399ced7"


def requestLog(url, status, headers):
    print(url)
    print(status)
    print(headers)


panth = pantheon.Pantheon(server, api_key, errorHandling=True, requestsLoggingFunction=requestLog, debug=True)


async def getChall():
    try:
        data = await panth.getChallengerLeague("RANKED_SOLO_5x5")
        return data['entries']
    except Exception as e:
        print(e)


loop = asyncio.get_event_loop()

(entries) = loop.run_until_complete(getChall())

data = {}
i = 1

for summoner in entries:
    temp = []
    for item in summoner:
        temp.append(summoner[item])
    tempDict = {i: temp}
    i = i + 1
    data.update(tempDict)

print(data)
df = pd.DataFrame(data)
df = df.transpose()
df.columns = ['SummmonerID', 'SummonerName', 'Points', 'Rank', 'Wins', 'Losses', 'Veteran', 'Inactive', 'Freshblood', 'HotStreak']
df.info()
df.to_csv('testing.csv')





