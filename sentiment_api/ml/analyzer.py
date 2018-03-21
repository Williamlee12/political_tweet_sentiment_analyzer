from sklearn.externals import joblib
import numpy as np
import os


class Analyzer(object):

    def analyze(self, list_of_tweets):
        list_of_tweets = [[tweet] for tweet in list_of_tweets]
        vect = joblib.load(os.environ['PICKLE_PATH'] + 'sentiment_api/ml/nb_vect.pkl')
        nb = joblib.load(os.environ['PICKLE_PATH'] + 'sentiment_api/ml/nb.pkl')
        analyzed_tweets = []
        for tweet in list_of_tweets:
            sentence = vect.transform(tweet)
            probability_array = nb.predict_proba(sentence)
            probability = np.array(probability_array).tolist()
            result_dict = {"neg": probability[0][0], "neu": probability[0][1], "pos": probability[0][2]}
            scores = [result_dict["neg"], result_dict["neu"], result_dict["pos"]]
            m = max(scores)
            winner = [i for i, j in enumerate(scores) if j == m][0]
            if winner == 0:
                sen = "negative"
            elif winner == 1:
                sen = "neutral"
            else:
                sen = "positive"
            x = [tweet[0], result_dict, sen]
            analyzed_tweets.append(x)
        return analyzed_tweets
