from PyQt5 import QtCore, QtWidgets, QtGui
from ui.visu_ui import Ui_MainWindow
import numpy as np
import colour as cl
from typing import Dict, Tuple
import sys
import os

#sys.path.append(os.environ["PAPARAZZI_HOME"] + '/sw/ext/pprzlink/lib/v2.0/python')
sys.path.append('/home/fabien/paparazzi' + '/sw/ext/pprzlink/lib/v2.0/python')

from ivy.std_api import *
import pprzlink.ivy

import pprzlink.messages_xml_map as messages_xml_map
import pprzlink.message as message

SAMPLING_STEP = 10

DEFAULT_BUS = '127.0.0.1:2010'
GPS_REGEX = "(.*NAVIGATION.*)"

class TitooVisu(Ui_MainWindow, QtCore.QObject):

    uav_pos_changed = QtCore.pyqtSignal(tuple)

    def __init__(self, parent=None):
        Ui_MainWindow.__init__(self)
        QtCore.QObject.__init__(self)

        # Creation of the ivy interface
        self.ivy = pprzlink.ivy.IvyMessagesInterface(
            agent_name="Titoo Visu",            # Ivy agent name
            start_ivy=False,                    # Do not start the ivy bus now
            ivy_bus="127.255.255.255:2010")     # address of the ivy bus
        self.ivy.start()
        self.ivy.subscribe(self.update_gps, message.PprzMessage("telemetry", "NAVIGATION"))

        self.scene = QtWidgets.QGraphicsScene()
        self.points = {}    # {(x, y, z): 12, (x2, y2, Z2): 42}
        # self.points = {(50, 50, 0): 12,
        #                (100, 100, 0): 23,
        #                (200, 160, 10): 34}
        self.points_items = {} # {(x, y, z): Item1, (x2, y2, Z2): Item2}
        self.uav_pos = None
        self.uav_item = None
        self.uav_pos_changed.connect(self.update_uav_pos)


    def built(self):
        self.zAutoCheckbox.stateChanged.connect(self.set_z_auto)
        self.graphicsView.setScene(self.scene)
        self.zSlider.valueChanged.connect(self.filter_z)

        self.load_cloud("data/lwc_cloud.npy")
        for point, value in self.points.items():
            self.add_point(point, value)

        pass

    def add_point(self, point, value):
        x, y, z = point
        val_col = (value-0.3)/(1.2)
        col = cl.Color(hue=val_col, saturation=1, luminance=0.5)
        col_hex = col.get_hex()
        color = QtGui.QColor(col_hex)
        self.points_items[point] = self.scene.addEllipse(x, y, 5, 5, color, color)

    def filter_z(self, z_filter):
        for point, item in self.points_items.items():
            x, y, z = point
            if z == z_filter:
                item.show()
            else:
                item.hide()

    def closing(self):
        self.ivy.shutdown()
        pass

    def set_z_auto(self, state):
        if state:
            self.zSpinbox.setReadOnly(True)
            self.zSlider.setEnabled(False)
        else:
            self.zSpinbox.setReadOnly(False)
            self.zSlider.setEnabled(True)

    def update_uav_pos(self, pos):
        self.uav_pos = pos
        ac_id, x, y = pos
        if self.uav_item is None:
            polygon = QtGui.QPolygonF([QtCore.QPoint(-10, -7.5), QtCore.QPoint(0, 2.5), QtCore.QPoint(10, -7.5), QtCore.QPoint(0, 7.5)])
            self.uav_item = self.scene.addPolygon(polygon)

            #self.uav_item = self.scene.addRect(int(x), int(y), 15, 5)   #type: QtWidgets.QGraphicsRectItem
        else:
            self.uav_item.setPos(int(x), int(y))

    def update_uav_alt(self, alt):
        print(alt)

    def update_gps(self, ac_id, pprzMsg):
        x= float(pprzMsg.pos_x)
        y= float(pprzMsg.pos_y)
        self.uav_pos_changed.emit((ac_id, x, y))

    def load_cloud(self, filename):
        cloud_array = np.load(filename)
        for i in range(len(cloud_array)):
            for j in range(len(cloud_array[i])):
                for k in range(len(cloud_array[i][j])):
                    if not np.isnan(cloud_array[i][j][k]):
                        self.points[(SAMPLING_STEP * k, SAMPLING_STEP * j, i - 70)] = cloud_array[i][j][k]
