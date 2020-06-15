

""" The Web API provided by StockTwits https://api.stocktwits.com/developers/docs/api#streams-symbol-docs
Search for symbols or users
1. Get message streams in the form of JSON
2. NLP for messages
3. Create timeline (dataframe)
"""
import importlib
import StockTwitsAPI
importlib.reload(StockTwitsAPI)
import json
import datetime as dt
import time
import pandas as pd
from StockTwitsAPI import StockTwitsApi    # create module NewsAPI for object class "NewsApi"
import preprocessing as pre             # create preprocessing class for NLP
importlib.reload(pre)



def collect_symbol(symbol, access_token):
    """Download cur-related messages that are older than the oldest in database.
      """
    api = StockTwitsApi(access_token)
    stream = api.stream_symbol(symbol=Symbol).json()
    status = stream["response"]["status"]
    with open("stream{}.json".format(symbol), "w", encoding="utf-8") as f:
        json.dump(stream, f)

def collect_user(userID, access_token):
    """Download cur-related messages that are older than the oldest in database.
      """
    api = StockTwitsApi(access_token)
    stream = api.stream_user(user_id=userID).json()
    status = stream["response"]["status"]
    print(status)
    default_stream = {'response': {'status': 200}, 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28567, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'cursor': {'more': True, 'since': 199293496, 'max': 197875637}, 'messages': [{'id': 199293496, 'body': '@mockstarket yes ! I buy each 4 week market price', 'created_at': '2020-03-10T12:37:24Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'conversation': {'parent_message_id': 199291731, 'in_reply_to_message_id': 199293080, 'parent': False, 'replies': 3}, 'likes': {'total': 4, 'user_ids': [1419576, 1027976, 411344, 969971]}, 'mentioned_users': ['@mockstarket'], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 15, 'official_api': True}}, {'id': 199291731, 'body': '$BTC.X $XRP.X $GBTC moooooooon candle time', 'created_at': '2020-03-10T12:27:54Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28554, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 154989}, {'id': 12649, 'symbol': 'GBTC', 'title': 'Grayscale Bitcoin Trust', 'aliases': [], 'is_following': False, 'watchlist_count': 30534}, {'id': 13528, 'symbol': 'XRP.X', 'title': 'Ripple', 'aliases': ['XRPUSD'], 'is_following': False, 'watchlist_count': 61736}], 'conversation': {'parent_message_id': 199291731, 'in_reply_to_message_id': None, 'parent': True, 'replies': 3}, 'likes': {'total': 6, 'user_ids': [3058123, 1630266, 1027976, 1419576, 411344, 969971]}, 'mentioned_users': [], 'entities': {'chart': {'thumb': 'https://charts.stocktwits.com/production/small_199291731.png', 'large': 'https://charts.stocktwits.com/production/large_199291731.png', 'original': 'https://charts.stocktwits.com/production/original_199291731.png', 'url': 'https://charts.stocktwits.com/production/original_199291731.png'}, 'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 14, 'official_api': True}}, {'id': 199224942, 'body': '$BTC.X they will print cash. Buy bitcoin. They cant print it', 'created_at': '2020-03-09T23:46:38Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28567, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 155040}], 'conversation': {'parent_message_id': 199224942, 'in_reply_to_message_id': None, 'parent': True, 'replies': 1}, 'likes': {'total': 3, 'user_ids': [969971, 774160, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 14, 'official_api': True}}, {'id': 199224858, 'body': '$BTC.X moooooooooon', 'created_at': '2020-03-09T23:46:12Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28567, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 155040}], 'likes': {'total': 2, 'user_ids': [969971, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 13, 'official_api': True}}, {'id': 199178204, 'body': '$BTC.X $GBTC buy the fear', 'created_at': '2020-03-09T20:21:34Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28567, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 155040}, {'id': 12649, 'symbol': 'GBTC', 'title': 'Grayscale Bitcoin Trust', 'aliases': [], 'is_following': False, 'watchlist_count': 30541}], 'likes': {'total': 9, 'user_ids': [3058123, 3049102, 969971, 1226488, 2997561, 1368012, 3136413, 1978952, 411344]}, 'mentioned_users': [], 'entities': {'chart': {'thumb': 'https://charts.stocktwits.com/production/small_199178204.png', 'large': 'https://charts.stocktwits.com/production/large_199178204.png', 'original': 'https://charts.stocktwits.com/production/original_199178204.png', 'url': 'https://charts.stocktwits.com/production/original_199178204.png'}, 'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 12, 'official_api': True}}, {'id': 199178027, 'body': '@DrunkJimmy not selling. But I buy', 'created_at': '2020-03-09T20:20:57Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'conversation': {'parent_message_id': 199173618, 'in_reply_to_message_id': 199177049, 'parent': False, 'replies': 2}, 'likes': {'total': 3, 'user_ids': [969971, 411344, 1027976]}, 'mentioned_users': ['@DrunkJimmy'], 'entities': {'chart': {'thumb': 'https://charts.stocktwits.com/production/small_199178027.png', 'large': 'https://charts.stocktwits.com/production/large_199178027.png', 'original': 'https://charts.stocktwits.com/production/original_199178027.png', 'url': 'https://charts.stocktwits.com/production/original_199178027.png'}, 'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 11, 'official_api': True}}, {'id': 199173618, 'body': '$BTC.X poor bear. Buy the fear', 'created_at': '2020-03-09T20:07:02Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28567, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 155040}], 'conversation': {'parent_message_id': 199173618, 'in_reply_to_message_id': None, 'parent': True, 'replies': 2}, 'likes': {'total': 3, 'user_ids': [1961522, 969971, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 10, 'official_api': True}}, {'id': 199109162, 'body': '@Taiex lol..', 'created_at': '2020-03-09T16:28:25Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'conversation': {'parent_message_id': 199100240, 'in_reply_to_message_id': 199101998, 'parent': False, 'replies': 4}, 'likes': {'total': 2, 'user_ids': [969971, 411344]}, 'mentioned_users': ['@Taiex'], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 9, 'official_api': True}}, {'id': 199101543, 'body': '$BBD.B.CA', 'created_at': '2020-03-09T15:59:19Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 9826, 'symbol': 'BBD.B.CA', 'title': 'Bombardier Cl B Sv', 'aliases': [], 'is_following': False, 'watchlist_count': 3457}], 'likes': {'total': 4, 'user_ids': [194351, 969971, 2260511, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 8, 'official_api': True}}, {'id': 199101504, 'body': '@Taiex Im 21. I dont care hahaha', 'created_at': '2020-03-09T15:59:09Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28567, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'conversation': {'parent_message_id': 199100240, 'in_reply_to_message_id': 199100576, 'parent': False, 'replies': 4}, 'likes': {'total': 3, 'user_ids': [969971, 2062788, 411344]}, 'mentioned_users': ['@Taiex'], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 7, 'official_api': True}}, {'id': 199100240, 'body': '$AC.CA Im in', 'created_at': '2020-03-09T15:54:53Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28567, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 9734, 'symbol': 'AC.CA', 'title': 'Air Canada Cl B', 'aliases': ['AC.B.CA', 'AC.A.CA'], 'is_following': False, 'watchlist_count': 1959}], 'conversation': {'parent_message_id': 199100240, 'in_reply_to_message_id': None, 'parent': True, 'replies': 4}, 'likes': {'total': 4, 'user_ids': [261708, 969971, 411344, 1071021]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 6, 'official_api': True}}, {'id': 199067817, 'body': '$XRP.X buy it', 'created_at': '2020-03-09T14:18:16Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 167, 'following': 96, 'ideas': 6891, 'watchlist_stocks_count': 7, 'like_count': 28549, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 13528, 'symbol': 'XRP.X', 'title': 'Ripple', 'aliases': ['XRPUSD'], 'is_following': False, 'watchlist_count': 61734}], 'conversation': {'parent_message_id': 199067817, 'in_reply_to_message_id': None, 'parent': True, 'replies': 2}, 'likes': {'total': 4, 'user_ids': [1693782, 969971, 411344, 1027976]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 5, 'official_api': True}}, {'id': 199067755, 'body': '$GBTC buy the fear !!', 'created_at': '2020-03-09T14:18:09Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28555, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 12649, 'symbol': 'GBTC', 'title': 'Grayscale Bitcoin Trust', 'aliases': [], 'is_following': False, 'watchlist_count': 30534}], 'conversation': {'parent_message_id': 199067755, 'in_reply_to_message_id': None, 'parent': True, 'replies': 1}, 'likes': {'total': 5, 'user_ids': [2133319, 845279, 969971, 411344, 1027976]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 4, 'official_api': True}}, {'id': 199067674, 'body': '$BTC.X buy the fear', 'created_at': '2020-03-09T14:18:00Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28549, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 154977}], 'likes': {'total': 4, 'user_ids': [2002271, 969971, 411344, 1027976]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 3, 'official_api': True}}, {'id': 199056217, 'body': '$BTC.X print cash time lool', 'created_at': '2020-03-09T13:51:54Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28566, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 155007}], 'likes': {'total': 2, 'user_ids': [969971, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 2, 'official_api': True}}, {'id': 198948728, 'body': '$BTC.X wow ! Nice dip. Well play trader', 'created_at': '2020-03-08T23:48:02Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28566, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 155007}], 'likes': {'total': 2, 'user_ids': [969971, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 1, 'official_api': True}}, {'id': 198654422, 'body': '@mat3181 all marker is red. Buy crypto', 'created_at': '2020-03-06T15:19:31Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'conversation': {'parent_message_id': 198641027, 'in_reply_to_message_id': 198641027, 'parent': False, 'replies': 1}, 'likes': {'total': 2, 'user_ids': [411344, 969971]}, 'mentioned_users': ['@mat3181'], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 5, 'official_api': True}}, {'id': 198640770, 'body': '$BBD.B.CA dead money until coronavirus fear stop', 'created_at': '2020-03-06T14:43:28Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28567, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 9826, 'symbol': 'BBD.B.CA', 'title': 'Bombardier Cl B Sv', 'aliases': [], 'is_following': False, 'watchlist_count': 3459}], 'conversation': {'parent_message_id': 198640770, 'in_reply_to_message_id': None, 'parent': True, 'replies': 2}, 'likes': {'total': 4, 'user_ids': [371242, 3056090, 411344, 969971]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 4, 'official_api': True}}, {'id': 198416932, 'body': '$GBTC a gift', 'created_at': '2020-03-05T15:59:14Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 12649, 'symbol': 'GBTC', 'title': 'Grayscale Bitcoin Trust', 'aliases': [], 'is_following': False, 'watchlist_count': 30533}], 'likes': {'total': 4, 'user_ids': [411344, 1008472, 969971, 1027976]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 4, 'official_api': True}}, {'id': 198416615, 'body': '$XRP.X buy', 'created_at': '2020-03-05T15:58:18Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 13528, 'symbol': 'XRP.X', 'title': 'Ripple', 'aliases': ['XRPUSD'], 'is_following': False, 'watchlist_count': 61732}], 'likes': {'total': 3, 'user_ids': [411344, 969971, 1027976]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 3, 'official_api': True}}, {'id': 198415559, 'body': '$BTC.X buy the fear', 'created_at': '2020-03-05T15:54:43Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28549, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 154986}], 'likes': {'total': 5, 'user_ids': [2133319, 411344, 1693782, 969971, 1027976]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 2, 'official_api': True}}, {'id': 198200412, 'body': '$BBD.B.CA buy it.. over sold', 'created_at': '2020-03-04T17:49:30Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28554, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 9826, 'symbol': 'BBD.B.CA', 'title': 'Bombardier Cl B Sv', 'aliases': [], 'is_following': False, 'watchlist_count': 3457}], 'conversation': {'parent_message_id': 198200412, 'in_reply_to_message_id': None, 'parent': True, 'replies': 1}, 'likes': {'total': 7, 'user_ids': [3056090, 1891928, 969971, 411344, 3105710, 1249337, 1321416]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 3, 'official_api': True}}, {'id': 198166011, 'body': '$XRP.X buy', 'created_at': '2020-03-04T15:48:55Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 13528, 'symbol': 'XRP.X', 'title': 'Ripple', 'aliases': ['XRPUSD'], 'is_following': False, 'watchlist_count': 61732}], 'likes': {'total': 4, 'user_ids': [411344, 499776, 969971, 1027976]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 2, 'official_api': True}}, {'id': 198165948, 'body': '$BTC.X', 'created_at': '2020-03-04T15:48:41Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28567, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 155025}], 'likes': {'total': 2, 'user_ids': [411344, 969971]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 1, 'official_api': True}}, {'id': 197916328, 'body': '$BTC.X lol', 'created_at': '2020-03-03T15:06:06Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28549, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 11418, 'symbol': 'BTC.X', 'title': 'Bitcoin BTC/USD', 'aliases': ['BTCUSD'], 'is_following': False, 'watchlist_count': 154983}], 'likes': {'total': 2, 'user_ids': [969971, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 11, 'official_api': True}}, {'id': 197887729, 'body': '@SwingReaper @SulUpSolide oui je parles français et anglais', 'created_at': '2020-03-03T13:25:25Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'conversation': {'parent_message_id': 197875665, 'in_reply_to_message_id': 197886202, 'parent': False, 'replies': 4}, 'likes': {'total': 2, 'user_ids': [969971, 411344]}, 'mentioned_users': ['@SwingReaper', '@SulUpSolide'], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 10, 'official_api': True}}, {'id': 197879883, 'body': '@SulUpSolide bon plan', 'created_at': '2020-03-03T12:39:01Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'conversation': {'parent_message_id': 197875665, 'in_reply_to_message_id': 197878413, 'parent': False, 'replies': 4}, 'likes': {'total': 3, 'user_ids': [2919924, 969971, 411344]}, 'mentioned_users': ['@SulUpSolide'], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 14, 'official_api': True}}, {'id': 197875665, 'body': '$LPTX 5$', 'created_at': '2020-03-03T12:08:12Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 12116, 'symbol': 'LPTX', 'title': 'Leap Therapeutics, INC.', 'aliases': [], 'is_following': False, 'watchlist_count': 7476}], 'conversation': {'parent_message_id': 197875665, 'in_reply_to_message_id': None, 'parent': True, 'replies': 4}, 'likes': {'total': 3, 'user_ids': [1201998, 969971, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 13, 'official_api': True}}, {'id': 197875648, 'body': '$BBD.B.CA nice', 'created_at': '2020-03-03T12:08:06Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 9826, 'symbol': 'BBD.B.CA', 'title': 'Bombardier Cl B Sv', 'aliases': [], 'is_following': False, 'watchlist_count': 3457}], 'likes': {'total': 2, 'user_ids': [969971, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 12, 'official_api': True}}, {'id': 197875637, 'body': '$XRP.X', 'created_at': '2020-03-03T12:08:00Z', 'user': {'id': 1479436, 'username': 'HoldStrong', 'name': 'MAD', 'avatar_url': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/1479436/thumb-1557434989.png', 'join_date': '2018-04-24', 'official': False, 'identity': 'User', 'classification': [], 'followers': 168, 'following': 97, 'ideas': 6893, 'watchlist_stocks_count': 7, 'like_count': 28562, 'plus_tier': '', 'premium_room': '', 'trade_app': False}, 'source': {'id': 2095, 'title': 'StockTwits For Android ', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 13528, 'symbol': 'XRP.X', 'title': 'Ripple', 'aliases': ['XRPUSD'], 'is_following': False, 'watchlist_count': 61732}], 'likes': {'total': 4, 'user_ids': [1693782, 863754, 969971, 411344]}, 'mentioned_users': [], 'entities': {'sentiment': {'basic': 'Bullish'}}, 'filters': {'day_counts': 11, 'official_api': True}}]}
    if status == 200:
        return (stream)
    else:
        return (default_stream)
    # with open("streamUSER{}.json".format(userID), "w", encoding="utf-8") as f:
    #     json.dump(stream, f)


def main():

    with open("access_token_stockTwits.txt", "r") as f:
        access_token = f.read()[:-1]
    start = dt.datetime.now()
    Symbol='IBB'
    collect_symbol(symbol=Symbol, access_token=access_token)   # single request
    # cumcollect(symbol=Symbol, access_token=access_token)    # rate of limit: 400 requests
    print("Making timeline...")
    pre.make_timeline(symbol=Symbol)
    # pre.make_cum_timeline(symbol=Symbol)

    # get streams of specific users
    users = list(pd.read_csv("userID_BTC.csv", index_col=0).index)   # BTC users
    # users = list(pd.read_csv("userID_AAPL.csv", index_col=0).index)  # AAPL users
    mydata = []
    for user in users:
        rst = collect_user(userID=user, access_token=access_token)
        mydata.append({'id': user, 'followers': rst['user']['followers'], 'ideas': rst['user']['ideas'],
                       'like_count': rst['user']['like_count']})

    users_DF = pd.DataFrame(mydata)
    users_DF['followers_rank'] = users_DF['followers'].rank(pct=True)
    users_DF['ideas_rank'] = users_DF['ideas'].rank(pct=True)
    users_DF['likes_rank'] = users_DF['like_count'].rank(pct=True)
    # users_DF['followers_rank'] = users_DF['followers'].rank(ascending=False)
    # users_DF['ideas_rank'] = users_DF['ideas'].rank(ascending=False)
    # users_DF['likes_rank'] = users_DF['like_count'].rank(ascending=False)
    # users_DF.to_csv('Users_Info_AAPL_Rank.csv', columns=['id', 'followers', 'ideas', 'like_count', 'followers_rank', 'ideas_rank', 'likes_rank'])
    users_DF.to_csv('Users_Info_BTC_Rank.csv',
                    columns=['id', 'followers', 'ideas', 'like_count', 'followers_rank', 'ideas_rank', 'likes_rank'])


main()







