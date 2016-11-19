Dataset 2

Over 1.7 million continuous ratings (-10.00 to +10.00) of 150 jokes from 59,132 users: collected between November 2006 - May 2009

Save to disk, then unzip: jester_dataset_2.zip (7.7MB)

Format:

ratings.dat: Each row is formatted as [User ID] [Item ID] [Rating]
jokes.dat: Maps item ID's to jokes
Note that the ratings are real values ranging from -10.00 to +10.00. As of May 2009, the jokes {7, 8, 13, 15, 16, 17, 18, 19} are the "gauge set" (as discussed in the Eigentaste paper) and the jokes {1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 20, 27, 31, 43, 51, 52, 61, 73, 80, 100, 116} have been removed (i.e. they are never displayed or rated).

Dataset 2+

An updated version of Dataset 2 with over 500,000 new ratings from 79,681 total users: data collected from November 2006 - Nov 2012

Format:

In this dataset we stripped out users that did not respond to the gauge set of question. The data is formated as an excel file representing a 66336 x 151 matrix with rows as users and columns as jokes.
10 of the jokes don't have ratings, their ids are: { 1, 2, 3, 4, 6, 9, 10, 11, 12, 14 }.
Each rating is from (-10.00 to +10.00) and 99 corresponds to a null rating (user did not rate that joke).
Note that the ratings are real values ranging from -10.00 to +10.00. As of May 2009, the jokes {7, 8, 13, 15, 16, 17, 18, 19} are the "gauge set" (as discussed in the Eigentaste paper) and the jokes {1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 20, 27, 31, 43, 51, 52, 61, 73, 80, 100, 116} have been removed (i.e. they are never displayed or rated).
