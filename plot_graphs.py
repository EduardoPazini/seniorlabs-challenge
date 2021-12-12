'''
'''


import matplotlib.pyplot as plt
import numpy as np


def plot_bar_horizontal(data):
    print('\n---- Frequency of the most used common words -----\n')
    print(data, '\n')

    words = []
    frequency = []
    for item in data:
        words.append(item[0])
        frequency.append(item[1])
    
    plt.figure(figsize=(10,25))
    plt.barh(words, frequency, alpha = .6, color = 'royalblue')
    plt.title('Frequency of the most used common words')
    plt.margins(0,0)
    plt.ylabel('Words')
    plt.xlabel('Number of times used')
    plt.savefig('results/words_frequency_sorted.png', bbox_inches='tight')


def plot_grouped_bar_vertical(first_month, second_month, third_month):
    print('\n---- Frequency of message types per month -----\n')
    print(f'January: Common = {first_month[0]} and Spam = {first_month[1]}')
    print(f'February: Common = {second_month[0]} and Spam = {second_month[1]}')
    print(f'March: Common = {third_month[0]} and Spam = {third_month[1]}\n')
    
    common = [first_month[0], second_month[0], third_month[0]]
    spam = [first_month[1], second_month[1], third_month[1]]

    plt.figure(figsize=(10,5))

    bar_width = 0.25
    r1 = np.arange(len(common))
    r2 = [x + bar_width for x in r1]

    plt.bar(r1, common, color='royalblue', width=bar_width, label='Comum')
    plt.bar(r2, spam, color='purple', width=bar_width, label='Spam')
    plt.title('Frequency of message types per month')
    plt.ylabel('Number of messages')
    plt.xlabel('Months')
    plt.xticks([r + bar_width for r in range(len(common))], ['January', 'February', 'March'])
    plt.legend(loc="upper right")
    plt.savefig('results/message_type_month.png', bbox_inches='tight')
