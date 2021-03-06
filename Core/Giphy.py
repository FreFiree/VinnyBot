import json
import urllib
import urllib.request

async def harambe(message, client):
    data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/random?tag=silverback+gorilla&api_key=dc6zaTOxFJmzC").read().decode('utf-8'))
    data = json.loads(json.dumps(data['data']))
    await message.channel.send(data['url'])

async def giphy(message, client):
    with message.channel.typing():
        text = message.content[6:].replace(' ', '+')
        try:
            data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/random?tag="+text+"&api_key=dc6zaTOxFJmzC").read().decode('utf-8'))
            data = json.loads(json.dumps(data['data']))
            try:
                await message.channel.send(data['url'])
            except TypeError:
                await message.channel.send("No results returned :cry:")
        except UnicodeEncodeError:
            await message.channel.send("Error attempting to send giphy search. (Does the search have wierd characters or formatting?)")
