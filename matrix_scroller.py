#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


class Hist3D():
    def __init__(self, matrix, axis):
        self.axis = axis
        axis.set_title('Scroll to view slices')
        self.matrix = matrix
        nRows, nCols, self.nBins = matrix.shape
        self.index = self.nBins//2
        self.histogram = axis.imshow(self.matrix[:, :, self.index])
        self.update()

    def scroll(self, event):
        if event.button == 'up':
            self.index = (self.index + 1) % self.nBins
        else:
            self.index = (self.index - 1) % self.nBins
        self.update()

    def update(self):
        self.histogram.set_data(self.matrix[:, :, self.index])
        self.axis.set_ylabel('Slice {}'.format(self.index))
        self.histogram.axes.figure.canvas.draw()


def main():
    figure, axis = plt.subplots(1,1)
    matrix = np.random.rand(20, 20, 40)
    histogram_viewer = Hist3D(matrix, axis)
    figure.canvas.mpl_connect('scroll_event', histogram_viewer.scroll)
    plt.show()


if __name__ == "__main__":
    main()
