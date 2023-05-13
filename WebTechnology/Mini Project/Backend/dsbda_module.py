from textblob import TextBlob
import pandas as pd

class Sentiment:

    def train_on_data(self) -> None:
        df = pd.read_csv('Twitter_Data.csv')
        train_data = []
        for i, row in df.iterrows():
            train_data.append((row['clean_comment'], row['category']))
        model = TextBlob(str(train_data))

    def check_sentiment(self,user_input):
        prediction = TextBlob(user_input).polarity
        if prediction < 0:
            return -1
        return 1
