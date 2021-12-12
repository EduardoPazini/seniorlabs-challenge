'''
'''


import pandas as pd

import plot_graphs as plt

import sys


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
