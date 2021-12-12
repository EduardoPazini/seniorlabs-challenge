'''
'''


import functions as fun
import plot_graphs as plt


if __name__ == "__main__":
    dataframe = fun.get_sms_file()
    
    jan = dataframe.loc[(
        dataframe['Date'] > '2017-01-01 00:00:01') & (dataframe['Date'] <= '2017-01-31 23:59:59')]
    fev = dataframe.loc[(
        dataframe['Date'] > '2017-02-01 00:00:01') & (dataframe['Date'] <= '2017-02-31 23:59:59')]
    mar = dataframe.loc[(
        dataframe['Date'] > '2017-03-01 00:00:01') & (dataframe['Date'] <= '2017-03-31 23:59:59')]

    words_frequency = fun.sum_words_frequency(dataframe)
    plt.plot_bar_horizontal(words_frequency)
    
    jan_list = fun.sum_msgs_months(jan)
    fev_list = fun.sum_msgs_months(fev)
    mar_list = fun.sum_msgs_months(mar)
    plt.plot_grouped_bar_vertical(jan_list, fev_list, mar_list)

    jan_stats_list = fun.get_statistics(jan)
    fev_stats_list = fun.get_statistics(fev)
    mar_stats_list = fun.get_statistics(mar)
    plt.print_statistics(jan_stats_list, fev_stats_list, mar_stats_list)

    jan_streak_list = fun.longest_common_streak(jan, '01', 31)
    fev_streak_list = fun.longest_common_streak(fev, '02', 28)
    mar_streak_list = fun.longest_common_streak(mar, '03', 31)
    plt.print_longest_streak(jan_streak_list, fev_streak_list, mar_streak_list)

    accuracy = fun.automatic_spam_detect(dataframe)
    plt.print_accuracy_automatic_spam_detect(accuracy)
