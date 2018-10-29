import requests
token = "737435750:AAEqta-biTIdeqfOLkhGzNSEy_IoGmL36Rw"
method_name = "getupdates"
url = "https://api.telegram.org/bot{}/{}".format(token, method_name)

user_id = "759686210"
method_name = "sendmessage"
msg = "hello"
msg_url = "https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}".format(token, method_name, user_id, msg)
print (msg_url)
print (requests.get(msg_url))