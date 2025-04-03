import requests
import os

def search_twitter(query, max_results=10):
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    headers = {"Authorization": f"Bearer {bearer_token}"}
    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "public_metrics"
    }

    response = requests.get("https://api.twitter.com/2/tweets/search/recent", headers=headers, params=params)
    tweets = response.json().get("data", [])
    results = []
    for tweet in tweets:
        results.append({
            "source": "Twitter",
            "title": tweet["text"][:100],
            "url": f"https://twitter.com/i/web/status/{tweet['id']}",
            "engagement": tweet["public_metrics"]["like_count"] + tweet["public_metrics"]["retweet_count"]
        })
    return results
