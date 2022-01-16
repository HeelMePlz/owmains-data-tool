import os
import auth

reddit = auth.request()

os.system("clear")


def get_subreddits():

    subreddit_list = []

    # use my multireddit to get the overwatch mains subreddits
    subreddits = reddit.multireddit("HeelMePlz", "OverwatchMains").subreddits

    # add the name of each subreddit to the list
    for subreddit in subreddits:
        name = subreddit.display_name.capitalize()
        subreddit_list.append(name)

    # sort the list in alphabetical order
    subreddit_list.sort()

    return subreddit_list

def get_subcounts():
    
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

    return subcounts

subcounts = get_subcounts()

for subcount in subcounts:
    print(subcount)
