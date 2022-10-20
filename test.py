import unittest
import config
import auth
import csvwriter
import tweetretrieval


class Test(unittest.TestCase):

    def test_get_valid_user(self):
        config_ = config.Config('config.ini')
        auth_ = auth.Authentication(config_).authentication()

        test_valid_user = tweetretrieval.TweetRetrieval(auth_).get_user("kingjames")
        self.assertTrue(test_valid_user)

    def test_invalid_user(self):
        config_ = config.Config('config.ini')
        auth_ = auth.Authentication(config_).authentication()

        test_invalid_user = tweetretrieval.TweetRetrieval(auth_).get_user("ehdnchklahdosdalskdjklzxlaksdjhaolskdalsd")
        self.assertFalse(test_invalid_user)

    def test_get_tweet(self):
        config_ = config.Config('config.ini')
        auth_ = auth.Authentication(config_).authentication()

        test_get_one_tweet = tweetretrieval.TweetRetrieval(auth_).get_tweet("kingjames", 1)
        print(test_get_one_tweet)

    def test_remove_emojis(self):
        text_with_emojis = "😀😀Hello World"
        text_without_emojis = csvwriter.remove_emojis(text_with_emojis)
        self.assertEqual(text_without_emojis, "Hello World")

    '''
    def test_tweet_processor(self):
        orginal_text = "😀😀Hello World\n\n\n\nHello Python, hello C++, hello Java, hello C"
        clean_text = csvwriter.tweet_processor(orginal_text, 'eva')
        self.assertEqual(clean_text, "Hello World Hello Python hello C++ hello Java hello C")
    '''

    def test_CSVWriter(self):
        fake_header = ["col1", "col2"]
        fake_tweets = ""
        create_empty_csv = csvwriter.CSVWriter("kingjames").store_data(fake_header, fake_tweets)

