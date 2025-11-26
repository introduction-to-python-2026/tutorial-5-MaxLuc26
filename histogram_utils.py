import histogram.ipynb

def build_histogram(data):
    histogram_dict = {}
    for i in  data: 
      if i in histogram_dict:
        histogram_dict[i] += 1
      else:
        histogram_dict[i] = 1
    return histogram_dict

def plot_histogram(histogram):
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Items')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


