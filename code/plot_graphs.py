'''
Plotting and printing the results of functions
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


def print_statistics(first_month, second_month, third_month):
    print('\n---- Statistics for each month -----\n')
    print(f'January:\n\tMaximum = {first_month[0]}\n\tMinimum = {first_month[1]}\n\tMean = '\
        f'{first_month[2]}\n\tMedian = {first_month[3]}\n\tStandard Deviation = '\
            f'{first_month[4]}\n\tVariance = {first_month[5]}')
    print(f'February:\n\tMaximum = {second_month[0]}\n\tMinimum = {second_month[1]}\n\tMean = '\
        f'{second_month[2]}\n\tMedian = {second_month[3]}\n\tStandard Deviation = '\
            f'{second_month[4]}\n\tVariance = {second_month[5]}')
    print(f'March:\n\tMaximum = {third_month[0]}\n\tMinimum = {third_month[1]}\n\tMean = '\
        f'{third_month[2]}\n\tMedian = {third_month[3]}\n\tStandard Deviation = '\
            f'{third_month[4]}\n\tVariance = {third_month[5]}\n')


def print_longest_streak(first_month, second_month, third_month):
    print('\n---- Longest messages streak for each month -----\n')
    print(f'January: Messages Streak = {first_month[0]} and Date = {first_month[1]}')
    print(f'February: Messages Streak = {second_month[0]} and Date = {second_month[1]}')
    print(f'March: Messages Streak = {third_month[0]} and Date = {third_month[1]}\n')


def print_accuracy_automatic_spam_detect(accuracy):
    print('\n---- Accuracy of automatic spam detection -----\n')
    print(f'Accuracy: {accuracy}\n')
