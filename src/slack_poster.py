import sys
import pandas as pd
#import graphlab as gl
from performotron import Comparer

class RecComparer(Comparer):
    def score(self, predictions):
        """Look at 5% of most highly predicted jokes for each user.
        Return the average actual rating of those jokes.
        """
        #sample = pd.read_csv('data/sample_submission.csv')

        df = pd.concat([#sample,
                        predictions,
                        self.target], axis=1)


        g = df.groupby('user_id')

        top_5 = g.rating.transform(
            lambda x: x >= x.quantile(.95)
        )

        return self.target[top_5==1].mean()

if __name__ == "__main__":
    sample_sub_fname = sys.argv[1]
    test=pd.read_csv('data/dont_use.csv')
    test.rating.name='test_rating'
    rc = RecComparer(test.rating, config_file='config.yaml')

    sample_sub = pd.read_csv(sample_sub_fname)
    if sample_sub.shape[0] != 522169:
        print " ".join(["Your matrix of predictions is the wrong size.",
        "It should provide ratings",
        " for 522169 entries (yours=%s)." % sample_sub.shape[0]])
    else:
        rc.report_to_slack(sample_sub)
