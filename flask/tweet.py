import re

class Tweet:

	#fomatting data to fit flask apps

    def __init__(self, data):
        self.data = data

    def user_link(self):
        return "http://twitter.com/{}".format(self.data['username'])

    def filtered_text(self):
        return self.highlight_hashtags(self.filter_urls(self.data['#reopen']))

    def highlight_hashtags(self, text):
        hashtags = ["#reopening", "#reopen", "#Reopening", "#Reopen",]

        for hashtag in hashtags:
            if (hashtag in text):
                text = text.replace(hashtag, "<mark>{}</mark>".format(hashtag))
            else:
                continue

        return text

    def filter_urls(self, text):
        return re.sub("(https:\/\/\S+)", r'<a href="\1" target="_blank">\1</a>', text)
