import csv
import re


class CSVWriter:
    def __init__(self, screen_name):
        self.screen_name = screen_name

    def store_data(self, headers, tweets):
        with open('twitter.csv', 'w', newline='', encoding='utf-8') as csvfile:
            write = csv.writer(csvfile)
            write.writerow(headers)
            for tweet in tweets:
                write.writerow(tweet_processor(tweet, self.screen_name))

            csvfile.close()


def remove_emojis(text):
    emojis = re.compile("["
                        u"\U0001F600-\U0001F64F"
                        u"\U0001F300-\U0001F5FF"
                        u"\U0001F680-\U0001F6FF"
                        u"\U0001F1E0-\U0001F1FF"
                        u"\U00002500-\U00002BEF"
                        u"\U00002702-\U000027B0"
                        u"\U00002702-\U000027B0"
                        u"\U000024C2-\U0001F251"
                        u"\U0001f926-\U0001f937"
                        u"\U00010000-\U0010ffff"
                        u"\u2640-\u2642"
                        u"\u2600-\u2B55"
                        u"\u200d"
                        u"\u23cf"
                        u"\u23e9"
                        u"\u231a"
                        u"\ufe0f"
                        u"\u3030"
                        "]+", re.UNICODE)
    return re.sub(emojis, '', text)


def tweet_processor(tweet, screen_name):
    name = '@{name}'.format(name=screen_name)
    clean_text = remove_emojis(tweet.text)
    clean_text = clean_text.replace("\n", " ")
    clean_text = clean_text.replace(",", " ")
    clean_text = clean_text.replace("…", " ")
    clean_text = " ".join(clean_text.split())
    hashtag_count = len(tweet.entities['hashtags'])
    return [name, clean_text, str(hashtag_count)]