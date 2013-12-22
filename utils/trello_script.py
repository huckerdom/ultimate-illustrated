from trello import TrelloApi
ns = {}
execfile('.trello-api-keys', ns)

client = TrelloApi(ns['key'])

client.boards.get_list('OWnNA1h1')

client.lists.new_card
client.get_token_url
# put token manually into file
execfile('.trello-api-keys', ns)
client.set_token(ns['token'])


for index, rule in enumerate(nns['rules']):
    client.lists.new_card('52b15e53abfcca855201ffd4', 'Rule #%d: %s' % (index+1, rule))
