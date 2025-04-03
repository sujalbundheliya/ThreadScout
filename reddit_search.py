import praw
import os

def search_reddit(query, limit=10):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    results = []
    for submission in reddit.subreddit("all").search(query, sort="relevance", limit=limit):
        results.append({
            "source": "Reddit",
            "title": submission.title,
            "url": submission.url,
            "engagement": submission.num_comments
        })
    return results
