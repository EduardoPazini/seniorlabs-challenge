'''
'''

import functions as fun

from unittest import TestCase


class TestUnitary(TestCase):
    def test_result_sum_words_frequency_one(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.sum_words_frequency(df)
        self.assertEqual(result[0][0], 'call')

    def test_result_sum_words_frequency_two(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.sum_words_frequency(df)
        self.assertEqual(int(result[0][1]), 581)

    def test_result_sum_msgs_total_one(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.sum_msgs_months(df)
        self.assertEqual(int(result[0]), 4827)

    def test_result_sum_msgs_total_two(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.sum_msgs_months(df)
        self.assertEqual(int(result[1]), 747)
    
    def test_result_get_statistics_total_one(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.get_statistics(df)
        self.assertEqual(int(result[0]), 190)

    def test_result_get_statistics_total_two(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.get_statistics(df)
        self.assertEqual(int(result[1]), 2)

    def test_result_get_statistics_total_three(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.get_statistics(df)
        self.assertEqual(float(result[2]), 16.222640832436312)
    
    def test_result_get_statistics_total_four(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.get_statistics(df)
        self.assertEqual(int(result[3]), 13)
    
    def test_result_get_statistics_total_five(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.get_statistics(df)
        self.assertEqual(float(result[4]), 11.767262023956693)
    
    def test_result_get_statistics_total_six(self):
        df = fun.get_sms_file('input/sms_senior.csv')
        result = fun.get_statistics(df)
        self.assertEqual(float(result[5]), 138.46845554045336)


def test_get_correct_dataframe():
    file = 'input/sms_senior.csv'
    df = fun.get_sms_file(file)
    type_df = "<class 'pandas.core.frame.DataFrame'>"
    assert(str(type(df))) == type_df


def test_fail_get_dataframe():
    file = ''
    try:
        df = fun.get_sms_file(file)
        assert False
    except:
        assert True


def test_type_sum_words_frequency():
    df = fun.get_sms_file('input/sms_senior.csv')
    result = fun.sum_words_frequency(df)
    assert type(result) is list


def test_type_result_sum_words_frequency():
    df = fun.get_sms_file('input/sms_senior.csv')
    result = fun.sum_words_frequency(df)
    assert type(result[0][0]) is str


def test_type_sum_msgs_months():
    df = fun.get_sms_file('input/sms_senior.csv')
    result = fun.sum_msgs_months(df)
    assert type(result) is list


def test_type_get_statistics():
    df = fun.get_sms_file('input/sms_senior.csv')
    result = fun.get_statistics(df)
    assert type(result) is list


def test_type_longest_common_streak():
    df = fun.get_sms_file('input/sms_senior.csv')
    jan = df.loc[(df['Date'] > '2017-01-01 00:00:01') & (df['Date'] <= '2017-01-31 23:59:59')]
    result = fun.longest_common_streak(jan, '01', 31)
    assert type(result) is list


def test_fail_longest_common_streak():
    df = fun.get_sms_file('input/sms_senior.csv')
    jan = df.loc[(df['Date'] > '2017-01-01 00:00:01') & (df['Date'] <= '2017-01-31 23:59:59')]
    try:
        result = fun.longest_common_streak(jan, '00', 00)
        assert False
    except:
        assert True
