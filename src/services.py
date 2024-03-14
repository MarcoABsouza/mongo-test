import tweepy
from src.secrets_1 import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_SECRET,
    ACCESS_TOKEN,
)
from src.connection import trends_collection
from src.constantes import BRAZIL_WOE_ID
from typing import Any
from typing import Dict
from typing import List


def _get_trends(woe_id: int) -> List[Dict[str, Any]]:
    """Get teending topics
    Args:
        woe_id(int): Identifier of loction
    Returns:
        list[dict[str,any]]: trends list
    """
    auth = tweepy.OAuthHandler(
        consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET
    )

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    trends = api.get_place_trends(woe_id)
    return trends[0]["trends"]


def get_trends_from_mongo() -> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)


def save_trends():
    trends = _get_trends(woe_id=BRAZIL_WOE_ID)
    trends_collection.insert_many(trends)
