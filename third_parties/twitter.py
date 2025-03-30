import os
from dotenv import load_dotenv
import tweepy
import requests

# Load environment variables (used only if mock=False)
load_dotenv()

# Setup Twitter client (only if needed)
def get_twitter_client():
    return tweepy.Client(
        bearer_token=os.environ.get("TWITTER_BEARER_TOKEN"),
        consumer_key=os.environ.get("TWITTER_API_KEY"),
        consumer_secret=os.environ.get("TWITTER_API_KEY_SECRET"),
        access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
    )

def scrape_user_tweets(username, num_tweets=5, mock: bool = True):
    """
    Scrapes a Twitter user's original tweets.
    In mock mode, uses static data from a public gist.
    """
    tweet_list = []

    if mock:
        print("🧪 Running in mock mode.")
        SASHI_TWITTER_GIST = "https://gist.githubusercontent.com/sashi789/72686410e181edcfdeb414a9ac95dc53/raw/3aa298756930977de321b4ec206a96707b49a607/eden-marco-scrapin.json"
        try:
            response = requests.get(SASHI_TWITTER_GIST, timeout=5)
            response.raise_for_status()
            tweets = response.json()

            for tweet in tweets[:num_tweets]:
                tweet_dict = {
                    "text": tweet["text"],
                    "url": f"https://twitter.com/{username}/status/{tweet['id']}"
                }
                tweet_list.append(tweet_dict)

        except Exception as e:
            print("Failed to fetch mock tweets:", e)

    else:
        print("🌐 Running with real Twitter API.")
        try:
            twitter_client = get_twitter_client()
            user_id = twitter_client.get_user(username=username).data.id
            tweets = twitter_client.get_users_tweets(
                id=user_id,
                max_results=num_tweets,
                exclude=["retweets", "replies"]
            )

            for tweet in tweets.data:
                tweet_dict = {
                    "text": tweet.text,
                    "url": f"https://twitter.com/{username}/status/{tweet.id}"
                }
                tweet_list.append(tweet_dict)
        except Exception as e:
            print("Error using Twitter API:", e)

    return tweet_list


if __name__ == "__main__":
    # Set mock=True to avoid API calls
    tweets = scrape_user_tweets(username="Sashidhar Chary", mock=True)
    print(tweets)
