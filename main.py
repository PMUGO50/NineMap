from Classdef import reader
from Classdef import ploter

if __name__ == '__main__':
    myreader = reader(inputfile="input.csv", picdir="picture")
    myreader.read_sheet()
    myreader.read_picture()
    myploter = ploter(infofile="info.csv")
    myploter.plot_result(myreader.title, myreader.ax_x, myreader.ax_y, myreader.cont, myreader.lst_pic)
    