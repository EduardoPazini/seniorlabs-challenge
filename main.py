'''
'''


import pandas as pd

import plot_graphs as plt

import sys


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


if __name__ == "__main__":
    dataframe = get_sms_file()
    
    words_frequency = sum_words_frequency(dataframe)
    plt.plot_bar_horizontal(words_frequency)

    jan = dataframe.loc[(
        dataframe['Date'] > '2017-01-01 00:00:01') & (dataframe['Date'] <= '2017-01-31 23:59:59')]
    fev = dataframe.loc[(
        dataframe['Date'] > '2017-02-01 00:00:01') & (dataframe['Date'] <= '2017-02-31 23:59:59')]
    mar = dataframe.loc[(
        dataframe['Date'] > '2017-03-01 00:00:01') & (dataframe['Date'] <= '2017-03-31 23:59:59')]
    jan_list = sum_msgs_months(jan)
    fev_list = sum_msgs_months(fev)
    mar_list = sum_msgs_months(mar)
    plt.plot_grouped_bar_vertical(jan_list, fev_list, mar_list)
