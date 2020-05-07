from urllib.parse import urlencode

data_dict = {
    'response_type': 'code',
    'client_id': 'client_id',
    'redirect_uri': 'redirect_uri',
    'state': 'state'
}

# 构建url
qq_url = 'https://graph.qq.com/oauth2.0/authorize?' + urlencode(data_dict)

print(qq_url)
