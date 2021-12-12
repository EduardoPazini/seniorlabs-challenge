'''
'''


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm 

import sys


def automatic_spam_detect(df):
    # Keeping only the columns 'Full_Text' and 'IsSpam' on dataframe
    text_spam = df.drop(df.columns[list(range(1, 153))], axis=1)

    z = text_spam['Full_Text']
    y = text_spam['IsSpam']

    # Divides columns 'z' and 'y' into 'z_train' for training inputs, 'y_train' for training labels, 'z_test' for testing inputs, and 'y_test' for testing labels
    z_train, z_test, y_train, y_test = train_test_split(z, y, test_size = 0.2)

    # Randomly assigns a number to each word, the number of occurrences of each word is saved in cv
    cv = CountVectorizer()
    features = cv.fit_transform(z_train)

    # Trains the model with 'features' and 'y_train'. Then, it checks the prediction against the 'y_train' label and adjusts its parameters until it reaches the highest possible accuracy
    model = svm.SVC()
    model.fit(features, y_train)

    # Scores the prediction of 'features_test' against the actual labels in 'y_test'
    features_test = cv.transform(z_test)
    accuracy = model.score(features_test, y_test)
    return accuracy


def longest_common_streak(month_df, month, number_days) -> list:
    days = ["%.2d" % i for i in range(number_days + 1)]

    k = 0
    count_common = 0
    max_streak = 0
    day_streak = ''
    
    while k < number_days:
        day = month_df.loc[(month_df['Date'] > '2017-{}-{} 00:00:01'.format(month, days[k+1])) & (month_df['Date'] <= '2017-{}-{} 23:59:59'. format(month, days[k+1]))]
        for index, row in day.iterrows():
            if(row['IsSpam'] == 'no'):
                count_common = count_common + 1
                if(count_common > max_streak):
                    max_streak = count_common
                    day_streak = (day['Date'].iloc[0]).split(' ')[0]
            else:
                count_common = 0
        count_common = 0
        k = k + 1
    
    result = [max_streak, day_streak]
    return result


def get_statistics(month_df) -> list:
    max = month_df['Word_Count'].max()
    min = month_df['Word_Count'].min()
    mean = month_df['Word_Count'].mean()
    median = month_df['Word_Count'].median()
    std = month_df['Word_Count'].std()
    var = month_df['Word_Count'].var()
    
    result = [max, min, mean, median, std, var]
    return result


def sum_msgs_months(month_df) -> list:
    count_common = 0
    count_spam = 0
    
    for index, row in month_df.iterrows():
        if(row['IsSpam'] == 'no'):
            count_common = count_common + 1
        else:
            count_spam = count_spam + 1

    result = [count_common, count_spam]
    return result


def sum_words_frequency(df) -> list:
    header = list(df.columns.values)

    # Removing the headers to keep only the words between 'got' and 'wan' in the list
    pop_index = [153, 152, 151, 150, 0]
    for index in pop_index:
        header.pop(index)

    total = []
    for word in header:
        total.append(df[word].sum())

    zipped = list(zip(header, total))
    sorted_words = sorted(zipped, key=lambda tup: tup[1], reverse=True)
    return sorted_words


def get_sms_file(file):
    try:
        dt = pd.read_csv(file, encoding='unicode_escape')
        return dt
    except OSError as e:
        print(f'No such file or directory:', file)
        sys.exit()
    except IOError as e:
        print(f'Could not read/write file:', file)    
        sys.exit()
