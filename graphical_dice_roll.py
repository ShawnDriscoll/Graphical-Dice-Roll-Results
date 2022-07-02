#
#   Graphical Dice Roll 0.1.0 Beta for Windows 10
#   Written for Python 3.9.11
#
##############################################################

"""
Graphical Dice Roll 0.1.0 Beta for Windows 10
--------------------------------------------------------

This program makes various dice rolls and calculates their graphs if needed.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow
from aboutdialog import Ui_aboutDialog
from alertdialog import Ui_alertDialog
from rpg_tools.PyDiceroll import roll
import sys
import time
import os
import numpy as np
from matplotlib import font_manager
import logging

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__app__ = 'Graphical Dice Roll 0.1.0 Beta'
__version__ = '0.1.0b'
__py_version__ = '3.9.11'
__expired_tag__ = False

die_types = ['D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D30', 'D66', 'D100']

class aboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self):
        '''
        Open the About dialog window
        '''
        super().__init__()
        log.info('PyQt5 aboutDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 aboutDialog initialized.')
        
    def acceptOKButtonClicked(self):
        '''
        Close the About dialog window
        '''
        log.info('PyQt5 aboutDialog closing...')
        self.close()

class alertDialog(QDialog, Ui_alertDialog):
    def __init__(self):
        '''
        Open the Alert dialog window
        '''
        super().__init__()
        log.info('PyQt5 alertDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 alertDialog initialized.')
        
    def acceptOKButtonClicked(self):
        '''
        Close the Alert dialog window
        '''
        log.info('PyQt5 alertDialog closing...')
        self.close()

class DiceWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        '''
        Display the dice roll window.
        Connect all the buttons to their functions.
        Initialize their value ranges.
        '''
        super().__init__()
        log.info('PyQt5 MainWindow initializing...')
        self.setupUi(self)
        
        self.diceCount.valueChanged.connect(self.diceCount_changed)
        
        for i in range(len(die_types)):
            self.diceType.addItem(die_types[i])
            
        self.dice_type = 'D6'
        self.diceType.setCurrentIndex(1)
        self.diceType.currentIndexChanged.connect(self.diceType_changed)
        
        self.diceDM.valueChanged.connect(self.diceDM_changed)
        
        self.rollButton.clicked.connect(self.rollButton_clicked)
        self.actionRoll_Dice.triggered.connect(self.rollButton_clicked)

        self.clear_graphButton.clicked.connect(self.clear_graphButton_clicked)
        self.actionClear_Graph.triggered.connect(self.clear_graphButton_clicked)
        
        self.clearButton.clicked.connect(self.clearButton_clicked)
        self.actionClear_All.triggered.connect(self.clearButton_clicked)
        
        self.actionAbout_Graphical_Dice_Roll.triggered.connect(self.actionAbout_triggered)
        
        # Set the About menu item
        self.popAboutDialog=aboutDialog()
        
        # Set the Alert menu item
        self.popAlertDialog=alertDialog()
        
        self.quitButton.clicked.connect(self.quitButton_clicked)
        self.actionQuit.triggered.connect(self.quitButton_clicked)
        
        self.rollInput.returnPressed.connect(self.manual_roll)
        
        self.dice_to_roll = ''
        self.clear_graph = False
        self.rolled_manually = False

        log.info('PyQt5 DiceWindow initialized.')
        
        if __expired_tag__ == True:
            '''
            Beta for this app has expired!
            '''
            log.warning(__app__ + ' expiration detected...')
            self.alert_window()
            '''
            display alert message and disable all the things
            '''
            self.diceCount.setDisabled(True)
            self.diceType.setDisabled(True)
            self.diceDM.setDisabled(True)
            self.rollButton.setDisabled(True)
            self.clear_graphButton.setDisabled(True)
            self.clearButton.setDisabled(True)
            self.rollInput.setDisabled(True)
            self.rollBrowser.setDisabled(True)
            self.actionAbout_Graphical_Dice_Roll.setDisabled(True)
            self.actionRoll_Dice.setDisabled(True)
            self.actionClear_Graph.setDisabled(True)
            self.actionClear_All.setDisabled(True)

    def diceCount_changed(self):
        '''
        Clear die modifier and last roll result
        '''
        self.diceDM.setValue(0)
        self.diceRoll.setText('')
        self.rollInput.clear()
        
    def diceType_changed(self):
        '''
        Enable/disable the dice count and die modifier fields
        depending on the dice type chosen.
        
        And clear fields as needed.
        '''
        self.dice_type = die_types[self.diceType.currentIndex()]
        if self.diceType.currentIndex() <= 5:
            self.countLabel.setEnabled(1)
            self.diceCount.setEnabled(1)
            self.dmLabel.setEnabled(1)
            self.diceDM.setEnabled(1)
        if self.diceType.currentIndex() == 6 or self.diceType.currentIndex() >= 8:
            self.diceCount.setValue(1)
            self.countLabel.setEnabled(0)
            self.diceCount.setEnabled(0)
            self.dmLabel.setEnabled(1)
            self.diceDM.setEnabled(1)
        if self.diceType.currentIndex() == 7:
            self.diceCount.setValue(1)
            self.countLabel.setEnabled(0)
            self.diceCount.setEnabled(0)
            self.dmLabel.setEnabled(0)
            self.diceDM.setEnabled(0)
        self.diceDM.setValue(0)
        self.diceRoll.setText('')
        self.rollInput.clear()
            
    def diceDM_changed(self):
        '''
        Clear last roll result if die modifier is changed
        '''
        self.diceRoll.setText('')
        self.rollInput.clear()
    
    def rollButton_clicked(self):
        '''
        Roll button was clicked.
        Construct the string argument needed for roll().
        '''
        if self.diceDM.value() >= 0:
            math_op = '+'
        else:
            math_op = ''
        if self.diceType.currentIndex() > 5:
            self.dice_to_roll = ''
        else:
            self.dice_to_roll = str(self.diceCount.value())
        self.dice_to_roll += self.dice_type
        if self.diceType.currentIndex() != 7:
            self.dice_to_roll += math_op + str(self.diceDM.value())
        self.roll_result = roll(self.dice_to_roll) 
        self.diceRoll.setText(str(self.roll_result))
        self.rollBrowser.append(self.dice_to_roll + ' = ' + self.diceRoll.text())
        self.rollInput.clear()
        self.draw_graph()
    
    def manual_roll(self):
        '''
        A roll was inputed manually
        '''
        dice_entered = self.rollInput.text()
        self.manual_dice_entered = dice_entered
        roll_returned = roll(dice_entered)
        log.debug('Rolling manually.')
        # Was the roll a valid one?
        if roll_returned == -9999:
            returned_line = dice_entered + ' = ' + '<span style=" color:#ff0000;">' + str(roll_returned) + '</span>'
        else:
            returned_line = dice_entered + ' = ' + str(roll_returned)
            
        # Display the roll result inside the text browser
        self.rollBrowser.append(returned_line)
        self.roll_result = roll_returned
        self.diceRoll.setText('')
        if self.roll_result == -9999:
            self.clear_graph = True
        self.rolled_manually = True
        self.draw_graph()
    
    def clear_graphButton_clicked(self):
        '''
        Clear the graph
        '''
        self.clear_graph = True
        self.draw_graph()

    def clearButton_clicked(self):
        '''
        Clear/reset all fields
        '''
        self.diceCount.setValue(1)
        self.diceDM.setValue(0)
        self.diceRoll.setText('')
        self.rollInput.clear()
        self.rollBrowser.clear()
        self.clear_graph = True
        self.draw_graph()
        
    def actionAbout_triggered(self):
        '''
        Display the About window
        '''
        self.popAboutDialog.show()
    
    def alert_window(self):
        '''
        open the Alert window
        '''
        log.warning(__app__ + ' show Beta expired PyQt5 alertDialog...')
        self.popAlertDialog.show()
    
    def draw_graph(self):
        '''
        Graph button was clicked.
        Construct the string argument needed for graphing (if valid roll type).
        '''
        if self.clear_graph:
            #print('clear graph')
            xper_range = ''
            yper_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            percent = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            bar_height = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            die_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            max_percent = len(yper_range)

            self.mpl.canvas.ax.clear()
            self.mpl.canvas.ax.bar(np.arange(len(die_range)), percent, width=0.6, alpha=.3, color='b')
            self.mpl.canvas.ax.set_xlim(xmin=-0.25, xmax=len(die_range)-0.75)
            self.mpl.canvas.ax.set_xticks(range(len(die_range)))
            self.mpl.canvas.ax.set_xticklabels(die_range)
            ticks_font = font_manager.FontProperties(family='Optima', style='normal', size=6, weight='normal', stretch='normal')
            for label in self.mpl.canvas.ax.get_xticklabels():
                label.set_fontproperties(ticks_font)
            title_font = font_manager.FontProperties(family='Optima', style='normal', size=10, weight='normal', stretch='normal')
            label = self.mpl.canvas.ax.set_title(xper_range)
            label.set_fontproperties(title_font)
            self.mpl.canvas.ax.set_yticks(range(0, max_percent, 1))
            self.mpl.canvas.ax.set_yticklabels(yper_range)
            ticks_font = font_manager.FontProperties(family='Optima', style='normal', size=6, weight='normal', stretch='normal')
            for label in self.mpl.canvas.ax.get_yticklabels():
                label.set_fontproperties(ticks_font)
            ylabel_font = font_manager.FontProperties(family='Optima', style='normal', size=10, weight='normal', stretch='normal')
            #self.mpl.canvas.ax.set_ylabel('Percentages')
            label = self.mpl.canvas.ax.set_ylabel('Percentages')
            label.set_fontproperties(ylabel_font)
            #self.mpl.canvas.ax.get_xaxis().grid(True)
            self.mpl.canvas.ax.get_yaxis().grid(True)
            
            self.mpl.canvas.draw()

            log.debug('Graph Cleared')
            self.clear_graph = False
            self.rolled_manually = False

        else:
            if not self.rolled_manually:
                if self.diceDM.value() >= 0:
                    math_op = '+'
                else:
                    math_op = ''
                if self.diceType.currentIndex() > 5:
                    self.dice_to_roll = ''
                else:
                    self.dice_to_roll = str(self.diceCount.value())
                self.dice_to_roll += self.dice_type
                if self.diceType.currentIndex() != 7:
                    self.dice_to_roll += math_op + str(self.diceDM.value())
            else:
                self.dice_to_roll = self.manual_dice_entered
                self.rolled_manually = False
            print('dice_to_roll:', self.dice_to_roll)
            
            die_range = []
            percent = []
            bar_height = []
            min_die_roll = 999
            max_die_roll = 0
            
            for i in range(10000):
                rolled_value = roll(self.dice_to_roll)
                if min_die_roll > rolled_value:
                    min_die_roll = rolled_value
                if max_die_roll < rolled_value:
                    max_die_roll = rolled_value
            print(min_die_roll, '-', max_die_roll)
            
            for i in range(min_die_roll, max_die_roll + 1):
                die_range.append(i)
                percent.append(0)
                bar_height.append(0)
            print('die_range:', die_range)
            
            n = 10000
            
            for i in range(n):
                percent[roll(self.dice_to_roll) - min_die_roll] += 1
            
            max_percent = 0
            
            for i in range(len(die_range)):
                percent[i] = percent[i] * 100. / n
                if percent[i] > max_percent:
                    max_percent = int(percent[i]) + 3
            
            #print(max_percent)
            yper_range = range(0, max_percent)
            print('yper_range:', list(yper_range))
            print('percent:', percent)
            
            log.debug('Generate ' + self.dice_to_roll + ' graph')
            
            xper_range = self.dice_to_roll

            for i in range(len(percent)):
                if i + min_die_roll == self.roll_result:
                    bar_height[i] = percent[i]
                    #print(i)
            print('bar_height:',bar_height)

            self.mpl.canvas.ax.clear()
            self.mpl.canvas.ax.bar(np.arange(len(die_range)), percent, width=0.6, alpha=.3, color='b')
            self.mpl.canvas.ax.set_xlim(xmin=-0.25, xmax=len(die_range)-0.75)
            self.mpl.canvas.ax.set_xticks(range(len(die_range)))
            self.mpl.canvas.ax.set_xticklabels(die_range)
            ticks_font = font_manager.FontProperties(family='Optima', style='normal', size=6, weight='normal', stretch='normal')
            for label in self.mpl.canvas.ax.get_xticklabels():
                label.set_fontproperties(ticks_font)
            title_font = font_manager.FontProperties(family='Optima', style='normal', size=10, weight='normal', stretch='normal')
            label = self.mpl.canvas.ax.set_title(xper_range)
            label.set_fontproperties(title_font)
            self.mpl.canvas.ax.set_yticks(range(0, max_percent, 1))
            self.mpl.canvas.ax.set_yticklabels(yper_range)
            ticks_font = font_manager.FontProperties(family='Optima', style='normal', size=6, weight='normal', stretch='normal')
            for label in self.mpl.canvas.ax.get_yticklabels():
                label.set_fontproperties(ticks_font)
            ylabel_font = font_manager.FontProperties(family='Optima', style='normal', size=10, weight='normal', stretch='normal')
            #self.mpl.canvas.ax.set_ylabel('Percentages')
            label = self.mpl.canvas.ax.set_ylabel('Percentages')
            label.set_fontproperties(ylabel_font)
            #self.mpl.canvas.ax.get_xaxis().grid(True)
            self.mpl.canvas.ax.get_yaxis().grid(True)

            self.mpl.canvas.ax.bar(np.arange(len(die_range)), bar_height, width=0.6, alpha=1.0, color='r')
            self.mpl.canvas.ax.set_xlim(xmin=-0.25, xmax=len(die_range)-0.75)
            self.mpl.canvas.ax.set_xticks(range(len(die_range)))
            self.mpl.canvas.ax.set_xticklabels(die_range)
            ticks_font = font_manager.FontProperties(family='Optima', style='normal', size=6, weight='normal', stretch='normal')
            for label in self.mpl.canvas.ax.get_xticklabels():
                label.set_fontproperties(ticks_font)
            title_font = font_manager.FontProperties(family='Optima', style='normal', size=10, weight='normal', stretch='normal')
            label = self.mpl.canvas.ax.set_title(xper_range)
            label.set_fontproperties(title_font)
            self.mpl.canvas.ax.set_yticks(range(0, max_percent, 1))
            self.mpl.canvas.ax.set_yticklabels(yper_range)
            ticks_font = font_manager.FontProperties(family='Optima', style='normal', size=6, weight='normal', stretch='normal')
            for label in self.mpl.canvas.ax.get_yticklabels():
                label.set_fontproperties(ticks_font)
            ylabel_font = font_manager.FontProperties(family='Optima', style='normal', size=10, weight='normal', stretch='normal')
            #self.mpl.canvas.ax.set_ylabel('Percentages')
            label = self.mpl.canvas.ax.set_ylabel('Percentages')
            label.set_fontproperties(ylabel_font)
            #self.mpl.canvas.ax.get_xaxis().grid(True)
            self.mpl.canvas.ax.get_yaxis().grid(True)
            
            self.mpl.canvas.draw()
            
    def quitButton_clicked(self):
        '''
        Exit this app
        '''
        self.close()
        
    def activate(self, reason):
        if reason == QSystemTrayIcon.Trigger:  # systray icon clicked.
            if self.isVisible():
                self.hide()
            else:
                self.show()
    
    def display_app(self, reason):
        self.show()
    
    def hide_app(self, reason):
        self.hide()
        
        
if __name__ == '__main__':

    '''
    Technically, this program starts right here when run.
    If this program is imported instead of run, none of the code below is executed.
    '''

#     logging.basicConfig(filename = 'graphical_dice_roll.log',
#                         level = logging.DEBUG,
#                         format = '%(asctime)s %(levelname)s %(name)s - %(message)s',
#                         datefmt='%a, %d %b %Y %H:%M:%S',
#                         filemode = 'w')

    log = logging.getLogger('graphical_dice_roll')
    log.setLevel(logging.DEBUG)

    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    
    fh = logging.FileHandler('Logs/graphical_dice_roll.log', 'w')
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s', datefmt = '%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    log.addHandler(fh)

    log.info('Logging started.')
    log.info(__app__ + ' starting...')

    trange = time.localtime()

    log.info(__app__ + ' started, and running...')
    
    if len(sys.argv) < 2:

        if trange[0] > 2022 or trange[1] > 11:
            __expired_tag__ = True
            __app__ += ' [EXPIRED]'

        app = QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)
        
        # Use print(QStyleFactory.keys()) to find a setStyle you like, instead of 'Fusion'
        
        # app.setStyle('Fusion')
        
        # darkPalette = QPalette()
        # darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
        # darkPalette.setColor(QPalette.WindowText, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
        # darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
        # darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
        # darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
        # darkPalette.setColor(QPalette.ToolTipText, Qt.white)
        # darkPalette.setColor(QPalette.Text, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
        # darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
        # darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        # darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
        # darkPalette.setColor(QPalette.ButtonText, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
        # darkPalette.setColor(QPalette.BrightText, Qt.red)
        # darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        # darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        # darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
        # darkPalette.setColor(QPalette.HighlightedText, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))
        
        MainApp = DiceWindow()
        MainApp.show()
        
        #app.setPalette(darkPalette)
        
        # Create the systray icon
        icon = QIcon(":/icons/die_icon.ico")
        
        # Create the systray
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)
        
        # Create the systray menu
        menu = QMenu()
        
        showApp = QAction("Show App")
        showApp.triggered.connect(MainApp.display_app)
        menu.addAction(showApp)
        
        hideApp = QAction("Hide App")
        hideApp.triggered.connect(MainApp.hide_app)
        menu.addAction(hideApp)

        quit = QAction("Quit")
        quit.triggered.connect(app.quit)
        menu.addAction(quit)
        
        tray.setToolTip("Graphical Dice Roll")
        
        # Add the menu to the tray
        tray.setContextMenu(menu)
        
        
        tray.activated.connect(MainApp.activate)
        
        app.exec_()
    
    elif trange[0] > 2022 or trange[1] > 11:
        __app__ += ' [EXPIRED]'
        '''
        Beta for this app has expired!
        '''
        log.warning(__app__)
        print()
        print(__app__)
        
    elif sys.argv[1] in ['-h', '/h', '--help', '-?', '/?']:
        print()
        print('     Using the CMD prompt to make dice rolls:')
        print("     C:\>graphical_dice_roll.py roll('2d6')")
        print()
        print('     Or just:')
        print('     C:\>graphical_dice_roll.py 2d6')
    elif sys.argv[1] in ['-v', '/v', '--version']:
        print()
        print('     graphical_dice_roll, release version ' + __version__ + ' for Python ' + __py_version__)
    else:
        print()
        dice = ''
        if len(sys.argv) > 2:
            for i in range(len(sys.argv)):
                if i > 0:
                    dice += sys.argv[i]
        else:
            dice = sys.argv[1]
        if "roll('" in dice:
            num = dice.find("')")
            if num != -1:
                dice = dice[6:num]
                dice = str(dice).upper().strip()
                num = roll(dice)
                if dice != 'TEST' and dice != 'INFO':
                    print("Your '%s' roll is %d." % (dice, num))
                    log.info("The direct call to graphical_dice_roll with '%s' resulted in %d." % (dice, num))
                elif dice == 'INFO':
                    print('graphical_dice_roll, release version ' + __version__ + ' for Python ' + __py_version__)
        else:
            dice = str(dice).upper().strip()
            num = roll(dice)
            if dice != 'TEST' and dice != 'INFO':
                print("Your '%s' roll is %d." % (dice, num))
                log.info("The direct call to graphical_dice_roll with '%s' resulted in %d." % (dice, num))
            elif dice == 'INFO':
                print('graphical_dice_roll, release version ' + __version__ + ' for Python ' + __py_version__)