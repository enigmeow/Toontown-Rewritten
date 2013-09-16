# 2013.08.22 22:15:59 Pacific Daylight Time
# Embedded file name: toontown.ai.CrashedLeaderBoardDecorator
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
import HolidayDecorator
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import Vec4, loadDNAFile, CSDefault, TransformState, NodePath, TransparencyAttrib
from toontown.hood import GSHood

class CrashedLeaderBoardDecorator(HolidayDecorator.HolidayDecorator):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('CrashedLeaderBoardDecorator')

    def __init__(self):
        HolidayDecorator.HolidayDecorator.__init__(self)

    def decorate(self):
        self.updateHoodDNAStore()
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()
        holidayIds = base.cr.newsManager.getDecorationHolidayId()
        if ToontownGlobals.CRASHED_LEADERBOARD not in holidayIds:
            return
        if base.config.GetBool('want-crashedLeaderBoard-Smoke', 1):
            self.startSmokeEffect()

    def startSmokeEffect(self):
        if isinstance(base.cr.playGame.getPlace().loader.hood, GSHood.GSHood):
            base.cr.playGame.getPlace().loader.startSmokeEffect()

    def stopSmokeEffect(self):
        if isinstance(base.cr.playGame.getPlace().loader.hood, GSHood.GSHood):
            base.cr.playGame.getPlace().loader.stopSmokeEffect()

    def undecorate(self):
        if base.config.GetBool('want-crashedLeaderBoard-Smoke', 1):
            self.stopSmokeEffect()
        holidayIds = base.cr.newsManager.getDecorationHolidayId()
        if len(holidayIds) > 0:
            self.decorate()
            return
        storageFile = base.cr.playGame.hood.storageDNAFile
        if storageFile:
            loadDNAFile(self.dnaStore, storageFile, CSDefault)
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\ai\CrashedLeaderBoardDecorator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:15:59 Pacific Daylight Time
