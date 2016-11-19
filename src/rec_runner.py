import graphlab as gl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def score(df_true, df_pred):
    """Look at 5% of most highly predicted jokes for each user.
    Return the average actual rating of those jokes.
    """
    #sample = pd.read_csv('data/sample_submission.csv')

    df = pd.concat([#sample,
                    df_pred,
                    df_true], axis=1)

    g = df.groupby('user_id')

    top_5 = g.pred_rating.apply(
        lambda x: x >= x.quantile(.95)
    )

    return df_true[top_5==1].mean()['true_rating']

def load_data():
    # Input data
    sf = gl.SFrame("data/ratings.dat", format='tsv')

    # Data to test predictions on
    df_sample = pd.read_csv("data/sample_submission.csv")
    sf_sample = gl.SFrame(df_sample)

    return sf, sf_sample, df_sample

def create_factorization_recommender(sf, num_factors, regularization = None):
    m = gl.recommender.ranking_factorization_recommender.create(observation_data=sf,
                                                     user_id="user_id",
                                                     item_id="joke_id",
                                                     target='rating',
                                                     solver='auto',
                                                     num_factors = num_factors,
                                                     regularization = regularization,
                                                     verbose = False,
                                                     random_seed = 42)
    return m

if __name__ == "__main__":
    sf, sf_sample, df_sample = load_data()

    training_data, validation_data = gl.recommender.util.random_split_by_user(sf, 'user_id', 'joke_id')

    df_true = pd.DataFrame()
    df_pred = pd.DataFrame()

    df_true['user_id'] = validation_data['user_id']
    df_true['joke_id'] = validation_data['joke_id']

    df_true['true_rating'] = validation_data['rating']

    # Plot scores vs num_factors
    num_factors = range(100)
    scores = []
    for n in num_factors:
        m = create_factorization_recommender(training_data, num_factors = n)
        df_pred['pred_rating'] = m.predict(validation_data)
        rc = score(df_true, df_pred)
        scores.append(rc)
        print 'Num Factors:', n, ' Score:', rc
    plt.plot(num_factors, scores)
    plt.xlabel('Number of Latent Features')
    plt.ylabel('Score')
    plt.title('Score vs Number of Latent Features')
    plt.show()

    # df_sample['rating'] = m.predict(sf_sample)
    # df_sample.to_csv("data/test_ratings.csv")



2.37327516234
2.02685335498
2.07007575758
2.21763392857
2.0877637987
2.26545589827
2.25892857143
2.23440882035
2.25740665584
2.18800730519
1.92268668831
2.11018668831
2.17884199134
2.04545454545
1.99438582251
2.00865800866
2.12719832251
2.17931547619
1.97338338745
2.13108766234
1.95704816017
1.95018262987
2.1350784632
2.015625
2.00551271645
1.91886498918
2.05086580087
1.8607616342
2.03794642857
2.05739312771
2.15158279221
1.88937364719
1.77394480519
1.868066829
1.68225784632
1.7858495671
1.663183171
1.81189123377
1.72155708874
1.79349296537
1.73677624459
1.68905573593
1.87195616883
1.59882305195
1.74242424242
1.57102272727
1.52651515152
1.53091179654
1.66233766234
1.31764069264
1.41622700216
1.32568993506
1.25571563853
1.06862148268
1.19876217532
1.22510822511
1.34260010823
Recsys training: model = ranking_factorization_recommender
Num Factors: 58  Score: 1.20353084416
Recsys training: model = ranking_factorization_recommender
Num Factors: 59  Score: 1.16169507576
Recsys training: model = ranking_factorization_recommender
Num Factors: 60  Score: 1.17180735931
Recsys training: model = ranking_factorization_recommender
