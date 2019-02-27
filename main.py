#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import titoovisu
import argparse

def main():
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  visu = titoovisu.TitooVisu()
  app.aboutToQuit.connect(visu.closing)
  visu.setupUi(MainWindow)
  visu.built()
  MainWindow.show()
  sys.exit(app.exec_())


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Titoo Visu !")
  #parser.add_argument('config_file', help="JSON configuration file")
  #args = parser.parse_args()
  #main(args.config_file)
  main()
