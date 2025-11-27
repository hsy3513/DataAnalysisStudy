# * 사전 작업
#   X 개발자 플랫폼에 회원가입하여 API 키 발급

# * ===== 주의사항! 아래 정보는 github, cloud에 올리지 말 것! ===== *
# CONSUMER API KEY
CONSUMER_KEY = 'BwVB74Jbf13U4vRItglvK4rTT'
CONSUMER_SECRET = 'Ab2xYOiuX8VWi29F8rn57gfz1ibcdCASipCWCzWPOwiXXl51Fr'

# ACCESS TOKEN
ACCESS_TOKEN = '1993489859521265666-wREPrPgfzPQiUFZGWCG9xZhZchLDLz'
ACCESS_SECRET = 'DMUkOVrg0SIHldF8K3m1Dr8LFS6D2lAOTXxkbPSzl9C8u'

# BEARER TOKEN
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAI%2BK5gEAAAAAhBAsHIJL70CMoIftEwNYk3M8p7g%3D6u6v7B5p7WK3vqa94raFuOE7siAKrl7x8GUNMlHVLAMGOxvd16'

# * ===================================================== *

# * tweepy 라이브러리(모듈)
#   > pip install tweepy
import tweepy

# Client 객체 -> 기능(API)을 함수 호출 방식으로 연동
def get_client_v1():
  return tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
    )

# * 인증 계정 정보 조회: get_me()
def get_user(client):
  response = client.get_me()
  print(response)
  username = response.data['username']
  print(f'인증 성공: 계정명 - {username}')

# * 트윗(작성): create_tweet()
def create_tweet(client):
  response = client.create_tweet(text='배가 고픔')
  print(response)

'''
# 계정 조회, 트윗 작성 테스트
client = get_client_v1()
get_user(client)
create_tweet(client)
'''
# ========================================================

# Client 객체 생성(Bearer token)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# * 최근 트윗(post) 검색 => search_recent_tweets()
keyword = '파이썬'
option = ' -is:retweet lang:ko'   # 리트윗 제외, 한국어
response = client.search_recent_tweets(query=keyword+option, max_results=10)
print(response)