import matplotlib.pyplot as plt
import pickle
import argparse

class PlotData(object):
    def __init__(self, filename):
        self.DATA = []
        self.Filename = filename

    def append(self, score):
        self.DATA.append(score)

    def dump(self):
        with open(self.Filename,"wb") as output:
            pickle.dump(self.DATA, output, pickle.HIGHEST_PROTOCOL)
    
    def load(self):
        with open(self.Filename,"rb") as input:
                self.DATA = pickle.load(input)

    def iterations(self):
        return range(0, len(self.DATA))



def main():
    parser = argparse.ArgumentParser("learn.py")
    parser.add_argument('data', type=str, help='path to [score] output pkl file for plotting.')
    args = parser.parse_args()

    plot_data = PlotData(args.data)
    plot_data.load()

    l = plt.plot(plot_data.iterations(), plot_data.DATA, 'ro')
    plt.setp(l, markersize = 5)
    plt.setp(l, markerfacecolor='C0')
    plt.xlabel('Iterations')
    plt.ylabel('Score')
    plt.show()

if __name__ == '__main__':
    main()
