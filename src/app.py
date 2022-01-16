import os
import auth

reddit = auth.request()

os.system("clear")

def get_owmains_subreddits():
    
    subcounts = []
    sub = {}

    # use my multireddit to get the overwatch mains subreddits
    subreddits = reddit.multireddit("HeelMePlz", "OverwatchMains").subreddits

    # get the name and subscriber count of each subreddit
    for subreddit in subreddits:
        sub = {
            "sub_name": subreddit.display_name.capitalize(),
            "sub_count": subreddit.subscribers,
        }
        subcounts.append(sub)

    # sort the list by name (subreddits starting in lowercase were at the end)
    subcounts = sorted(subcounts, key=lambda k: k["sub_name"])
