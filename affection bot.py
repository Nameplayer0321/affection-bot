import requests 

# "https://discord.com/channels/@me/1067590501940854946/messages"

payload = {
    'content': "Eli wants your attention"
}

header = {
    'authorization': 'NjgzNzg2Mjg2NzI4ODcxOTU5.GwwnWb.keog0S62JaRDu8P8-ghPlrQqgIG3deWOYNBFGw'
}

r = requests.post("https://discord.com/api/v9/channels/1067590501940854946/messages",
                    data=payload, headers=header)