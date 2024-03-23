import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

class reader:
    def __init__(self, inputfile, picdir):
        self.inputfile = inputfile
        self.picdir = picdir

    def read_sheet(self):
        data = pd.read_csv(self.inputfile, encoding='ansi', header=None)
        self.title = data.loc[5,1]
        self.ax_x = data.loc[0:1, 2:4]
        self.ax_y = data.loc[2:4, 0:1]
        self.cont = data.loc[2:4, 2:4]
    
    def read_picture(self):
        self.lst_pic = []
        for i in range(0,3):
            self.lst_pic.append([])
            for j in range(0,3):
                try:
                    pic_readed = plt.imread("%s/a_%d%d.jpg" % (self.picdir, i+1, j+1))
                except:
                    pic_readed = plt.imread("backuppic.jpg")
                    
                self.lst_pic[i].append(pic_readed)
        
class ploter:
    def __init__(self, infofile):
        self.infofile = infofile
        self.info = pd.DataFrame([1024, 768, 24, 18, 12, 14],\
                                 index=['width','height', 'size_title', 'size_axis', 'size_axisdescrption', 'size_content'],\
                                 columns=[1])

        self.info = pd.read_csv(self.infofile, encoding='ansi', index_col=0, header=None)
        self.allfont = {'family': 'Microsoft Yahei'}
        plt.rc('font', **self.allfont)
        self.titlefont = {'fontsize': self.info.loc['size_title',1], 'fontweight': 'bold'}
        self.axisfont = {'fontsize': self.info.loc['size_axis',1], 'fontweight': 'bold'}
        self.axisdesfont = {'fontsize': self.info.loc['size_axisdescrption',1], 'fontweight': 'normal'}
        self.contfont = {'fontsize': self.info.loc['size_content',1], 'fontweight': 'bold'}

    def set_parts(self, title):
        width_byinch = self.info.loc['width',1]/96
        height_byinch = self.info.loc['height',1]/96

        self.fig = plt.figure(figsize=[width_byinch, height_byinch])
        plt.title(title, fontdict=self.titlefont)
        plt.axis('off')
        grid = gridspec.GridSpec(nrows=15, ncols=8, figure=self.fig)
        self.ax = []
        
        for j in range(2,8,2):
            self.ax.append(self.fig.add_subplot(grid[0:2,j:j+2], frameon=False, xticks=[], yticks=[]))
            self.ax.append(self.fig.add_subplot(grid[2:3,j:j+2], frameon=False, xticks=[], yticks=[]))

        for i in range(3,15,4):
            for j in range(0,8,2):
                self.ax.append(self.fig.add_subplot(grid[i:i+3,j:j+2], frameon=False, xticks=[], yticks=[]))
                self.ax.append(self.fig.add_subplot(grid[i+3:i+4,j:j+2], frameon=False, xticks=[], yticks=[]))

    def add_text(self, subplot_index, tex, fontdic, x_re=0.5, y_re=0.5):
        self.ax[subplot_index].text(x=x_re, y=y_re, s=tex, ha='center', va='center',\
                        transform=self.ax[subplot_index].transData, fontdict=fontdic)

    def plot_result(self, title, ax_x, ax_y, cont, lst_pic):
        self.set_parts(title)

        #add x-axis and y-axis title
        self.add_text(0, tex=ax_x.loc[0,2], fontdic=self.axisfont)
        self.add_text(2, tex=ax_x.loc[0,3], fontdic=self.axisfont)
        self.add_text(4, tex=ax_x.loc[0,4], fontdic=self.axisfont)

        self.add_text(6, tex=ax_y.loc[2,0], fontdic=self.axisfont)
        self.add_text(14, tex=ax_y.loc[3,0], fontdic=self.axisfont)
        self.add_text(22, tex=ax_y.loc[4,0], fontdic=self.axisfont)

        #add x_axis and y-axis description
        self.add_text(1, tex=ax_x.loc[1,2], fontdic=self.axisdesfont, y_re=1)
        self.add_text(3, tex=ax_x.loc[1,3], fontdic=self.axisdesfont, y_re=1)
        self.add_text(5, tex=ax_x.loc[1,4], fontdic=self.axisdesfont, y_re=1)

        self.add_text(7, tex=ax_y.loc[2,1], fontdic=self.axisdesfont, y_re=1)
        self.add_text(15, tex=ax_y.loc[3,1], fontdic=self.axisdesfont, y_re=1)
        self.add_text(23, tex=ax_y.loc[4,1], fontdic=self.axisdesfont, y_re=1)

        #add content description
        self.add_text(9, tex=cont.loc[2,2], fontdic=self.contfont)
        self.add_text(11, tex=cont.loc[2,3], fontdic=self.contfont)
        self.add_text(13, tex=cont.loc[2,4], fontdic=self.contfont)
        self.add_text(17, tex=cont.loc[3,2], fontdic=self.contfont)
        self.add_text(19, tex=cont.loc[3,3], fontdic=self.contfont)
        self.add_text(21, tex=cont.loc[3,4], fontdic=self.contfont)
        self.add_text(25, tex=cont.loc[4,2], fontdic=self.contfont)
        self.add_text(27, tex=cont.loc[4,3], fontdic=self.contfont)
        self.add_text(29, tex=cont.loc[4,4], fontdic=self.contfont)

        #add content picture
        self.ax[8].imshow(lst_pic[0][0], cmap=plt.cm.binary)
        self.ax[10].imshow(lst_pic[0][1], cmap=plt.cm.binary)
        self.ax[12].imshow(lst_pic[0][2], cmap=plt.cm.binary)
        self.ax[16].imshow(lst_pic[1][0], cmap=plt.cm.binary)
        self.ax[18].imshow(lst_pic[1][1], cmap=plt.cm.binary)
        self.ax[20].imshow(lst_pic[1][2], cmap=plt.cm.binary)
        self.ax[24].imshow(lst_pic[2][0], cmap=plt.cm.binary)
        self.ax[26].imshow(lst_pic[2][1], cmap=plt.cm.binary)
        self.ax[28].imshow(lst_pic[2][2], cmap=plt.cm.binary)

        self.fig.savefig(fname="result.jpg")
        plt.show()