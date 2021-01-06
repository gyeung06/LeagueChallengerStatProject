from pantheon import pantheon
import asyncio

server = "na1"

#Put in own dev key to test
api_key = "RGAPI-xxx"


def requestLog(url, status, headers):
    print(url)
    print(status)
    print(headers)


panth = pantheon.Pantheon(server, api_key, errorHandling=True, requestsLoggingFunction=requestLog, debug=True)


async def getSummonerId(name):
    try:
        data = await panth.getSummonerByName(name)
        return data['id'], data['accountId']
    except Exception as e:
        print(e)


name = "FunOnDaBun"

loop = asyncio.get_event_loop()

(summonerId, accountId) = loop.run_until_complete(getSummonerId(name))

print(summonerId)
print(accountId)

