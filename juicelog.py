# Logger of Peeler - the scenemusic.net database rip engine.
# ©2016 Artur Szcześniak

import time
import datetime


class Juicelog:
    logfile = "logs/" + str(datetime.datetime.today())[0:10] + ".log"

    def logstart(self):
        with open(self.logfile, "a+") as log:
            log.write("[{}] Starting script!\n".format(time.ctime()))

    def logsong(self, songnumber):
        with open(self.logfile, "a+") as log:
            log.write("[{}] {}: Ripped song.\n".format(time.ctime(), songnumber))

    def logerror(self, what):
        with open(self.logfile, "a+") as log:
            log.write("[{}] {}\n".format(time.ctime(), what))
