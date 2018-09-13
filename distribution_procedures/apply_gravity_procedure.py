"""
 -----------------------------------------------------------------------------------------------------------
 Package:    AequilibraE

 Name:       Applying Gravity model
 Purpose:    Applies synthetic gravity model

 Original Author:  Pedro Camargo (c@margo.co)
 Contributors:
 Last edited by: Pedro Camargo

 Website:    www.AequilibraE.com
 Repository:  https://github.com/AequilibraE/AequilibraE

 Created:    2016-10-03
 Updated:    2018-08-08
 Copyright:   (c) AequilibraE authors
 Licence:     See LICENSE.TXT
 -----------------------------------------------------------------------------------------------------------
 """

from qgis.PyQt.QtCore import *
from ..common_tools import WorkerThread
from aequilibrae.distribution import GravityApplication


class ApplyGravityProcedure(WorkerThread):
    def __init__(self, parentThread, **kwargs):
        WorkerThread.__init__(self, parentThread)
        self.gravity = GravityApplication(**kwargs)
        self.error = None

    def doWork(self):
        self.gravity.apply()
        self.report = self.gravity.report
        self.finished_threaded_procedure.emit(0)
