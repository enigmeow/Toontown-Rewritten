# 2013.08.22 22:24:18 Pacific Daylight Time
# Embedded file name: toontown.racing.PiejectileManager
from pandac.PandaModules import *
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import *
from toontown.racing import Piejectile

class PiejectileManager(DirectObject):
    __module__ = __name__
    pieCounter = 0

    def __init__(self):
        self.piejectileList = []

    def delete(self):
        for piejectile in self.piejectileList:
            self.__removePiejectile(piejectile)

    def addPiejectile(self, sourceId, targetId = 0, type = 0):
        name = 'PiejectileManager Pie %s' % PiejectileManager.pieCounter
        pie = Piejectile.Piejectile(sourceId, targetId, type, name)
        self.piejectileList.append(pie)
        PiejectileManager.pieCounter += 1

    def __removePiejectile(self, piejectile):
        self.piejectileList.remove(piejectile)
        piejectile.delete()
        piejectile = None
        return
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\racing\PiejectileManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:24:18 Pacific Daylight Time
