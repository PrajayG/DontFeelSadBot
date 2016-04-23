
import tweepy, time, random
from keys import keys
from phrases import phrases

 
CONSUMER_KEY = 	keys['consumer_key'] 
CONSUMER_SECRET = keys['consumer_secret'] 
ACCESS_TOKEN = keys['access_token_key'] 
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



twt = api.search(q="feeling down")

t = ['I\'m feeling down',
	'feeling down right now',
	'feeling down now',
	'feeling down today',
	'I am feeling down',
	'i am feeling down',
	'feeling so down',
	'feel so down',
	'still feeling down']

print 'Hello'
for s in twt:
	for i in t:
		if i in s.text:
			print 'Working..'
			sn = s.user.screen_name
			num = str(random.randint(1,8))
			phrase = phrases[num]
			m = "@%s %s" % (sn, phrase)
			print 'Posting..'
			api.update_status(status = m)
			print 'Success!'
			print api.get_status(s.text)
			

