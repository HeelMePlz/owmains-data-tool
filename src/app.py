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
        name = subreddit.display_name.lower()
        subreddit_list.append(name)

    # sort the list in alphabetical order
    subreddit_list.sort()

    return subreddit_list
