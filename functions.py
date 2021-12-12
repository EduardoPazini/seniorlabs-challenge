'''
'''


import pandas as pd

import sys


def longest_common_streak(month_df, month, number_days):
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


def get_statistics(month_df):
    max = month_df['Word_Count'].max()
    min = month_df['Word_Count'].min()
    mean = month_df['Word_Count'].mean()
    median = month_df['Word_Count'].median()
    std = month_df['Word_Count'].std()
    var = month_df['Word_Count'].var()
    
    result = [max, min, mean, median, std, var]
    return result


def sum_msgs_months(month_df):
    count_common = 0
    count_spam = 0
    
    for index, row in month_df.iterrows():
        if(row['IsSpam'] == 'no'):
            count_common = count_common + 1
        else:
            count_spam = count_spam + 1

    result = [count_common, count_spam]
    return result


def sum_words_frequency(df):
    header = list(df.columns.values)
    
    # Removing the headers to keep only the words between 'got' and 'wan' in the list
    pop_index = [153, 152, 151, 150, 0]
    for index in pop_index:
        header.pop(index)
    
    total = []
    for word in header:
        total.append(df[word].sum())

    zipped = list(zip(header, total))
    sort_words = sorted(zipped, key=lambda tup: tup[1], reverse=True)
    return sort_words


def get_sms_file():
    file = 'input/sms_senior.csv'
    
    try:
        dt = pd.read_csv(file, encoding='unicode_escape')
        return dt
    except OSError as e:
        print(f'No such file or directory:', file)
        sys.exit()
    except IOError as e:
        print(f'Could not read/write file:', file)    
        sys.exit()
