'''
'''


import matplotlib.pyplot as plt


def plot_bar_horizontal(data):
    
    print('\n---- Frequency of the most used common words -----\n')
    print(data, '\n')

    words = []
    frequency = []
    for item in data:
        words.append(item[0])
        frequency.append(item[1])
    
    plt.barh(words, frequency, alpha = .6, color = "royalblue")
    plt.margins(0,0)
    plt.ylabel('Palavras')
    plt.xlabel('Quantidade de vezes usadas')
    plt.title('Frequência das palavras comuns mais utilizadas')
    plt.show()
