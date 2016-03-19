import praw
import time
import datetime
from datetime import datetime

REDDIT_USERNAME = "" # username of the bot
REDDIT_PASS = "" # password of the bot
SUBREDDIT_NAME = "vennbot" # subreddit you wish to track
WAIT_TIME = 10 # seconds between checking the subreddit for picture links

def main():
    currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
    print(str(currentTime) + 'Logging in...')
    r = praw.Reddit(user_agent = 'nexus6PImageHawk v0.1')
    r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning = True)
    subToWatch = r.get_subreddit(SUBREDDIT_NAME)

    while True:
        if datetime.today().weekday() == 6:
            time.sleep(60 * 60) # sleeps an hour because eh, why not? At most, it would be 9 seconds late on Sunday at this point
        else:
            currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
            print(currentTime + "Scanning for image posts...")
            submissions = r.get_subreddit(SUBREDDIT_NAME).get_new(limit=30)

            for item in submissions:
                if item.url[-3:] in {"jpg", "png", "gif", "peg", "bmp"}:
                    currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
                    item.add_comment("Sorry /u/" + item.author.name + ", we only allow image submissions on Sunday Picture day. Otherwise, direct picture links are not allowed on /r/Nexus6P.")
                    print(currentTime + "Removing submission...")
                    item.remove()
            time.sleep(WAIT_TIME)

if __name__ == "__main__":
	main()
