from Services import whatsapp_api
from Services import instagram_api

tokens = ['1f9bf78b9a18ce6d46a0cd2b0b86df9da', '2f9bf78b9a18ce6d46a0cd2b0b86df9db']

# Whatsapp integration:
# 1. init app with generated token (from database or unique in time)
wapp = whatsapp_api.Whatsapp(token=tokens[1])
# 2. set contact to send message in 10-signed format
# 3. add the message
wapp.sendMessage(phone='9999999999', message='this is a test!')
# 4. close the session
wapp.quit()


# Instagram integration:
# 1. init app with generated token (from database or unique in time)
insta = instagram_api.Instagram(username='example.user', password='example.pass', token=tokens[0], headless=False)
# 2. set contact to send message in 10-signed format
# 3. add the message
insta.sendMessage(user='example.1884', message='this is a test!')
# 4. close the session
insta.quit()


