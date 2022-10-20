import sys
import tweetretrieval
import csvwriter
import config
import auth


if __name__ == '__main__':
    config = config.Config('config.ini')
    auth_ = auth.Authentication(config).authentication()

    screen_name = input("What is your Twitter username? ")
    headers = ['Twitter Username', 'Tweet', 'Number of Hashtag']
    count = 10

    try:
        tweets = tweetretrieval.TweetRetrieval(auth_).get_tweet(screen_name, count)
        csvwriter.CSVWriter(screen_name).store_data(headers, tweets)
    except Exception as exception:
        print(sys.exc_info()[0], 'occurred')