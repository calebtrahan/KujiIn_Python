import math
import os

from main_const import PREDIRECTORY, POSTDIRECTORY, MAINCUTDIRECTORY, REFERENCEFILESMAINDIRECTORY, TEMPDIRECTORY, \
    RAMPDIRECTORY, ERRORFILES


def _fromUtf8(s): return s


from pydub import AudioSegment
from PyQt4.QtCore import QThread, SIGNAL


class Entrainment():
    def __init__(self, mainprogram, gui):
        self.gui = gui
        self.main = mainprogram

    def checkentrainment(self):
        """Method To Verify That All Entrainment Files Are In Place"""
        error = int()
        for k, u in enumerate(self.main.cuts): # Check Entrainment Files
            if k == 0: # Presession
                if not os.path.isfile(os.path.join(PREDIRECTORY, "presession.mp3")):
                    error += 1
                    print("%s Is Missing" % u["name"])
            elif k == 10: # Postsession
                if not os.path.isfile(os.path.join(POSTDIRECTORY, "postsession.mp3")):
                    error += 1
                    print("%s Is Missing" % u["name"])
            else: # All Others
                if k == 3: # TOH
                    tohlist = ["in", "out", "outpostsession"]
                    for i in tohlist:
                        for t in range(0, 3):
                            file = "3%s%d.mp3" % (i, t + 1)
                            if not os.path.isfile(os.path.join(MAINCUTDIRECTORY, "tohramp", file)):
                                error += 1
                                print("%s Is Missing" % os.path.join(MAINCUTDIRECTORY, "tohramp", file))
                else:
                    fil = "%s01.mp3" % k
                    if not os.path.isfile(os.path.join(MAINCUTDIRECTORY, fil)):
                        error += 1
                        print("%s Is Missing" % os.path.join(MAINCUTDIRECTORY, fil))
        if error > 0: return False
        else: return True

    def checkcutfiles(self):
        error = int()
        for t in self.main.cuts: # Cut Display Files
            if not os.path.isfile(os.path.join(REFERENCEFILESMAINDIRECTORY, str(t["name"]) + ".html")):
                print("%s Missing" % os.path.join(REFERENCEFILESMAINDIRECTORY, str(t["name"]) + ".html"))
                error += 1


class CreateEntrainmentMp3(QThread):
    def __init__(self, cutsinsession, invocationduration):
        QThread.__init__(self)
        self.cutsinsession = cutsinsession
        self.invocationduration = invocationduration
        self.cutstoplay = list()
        self.done = False
        self.settoexit = False

    @staticmethod
    def deleteentrainment():
        [os.remove(os.path.join(TEMPDIRECTORY, x)) for x in os.listdir(TEMPDIRECTORY) if not os.path.isdir(os.path.join(TEMPDIRECTORY, x))]

    def run(self):
        self.deleteentrainment()
        for x, i in enumerate(self.cutsinsession):
            while True:
                if self.settoexit:
                    self.deleteentrainment()
                    break
                if x == 0: # PRESESSION
                    nextup = self.cutsinsession[x + 1]
                    if i["duration"] != 0:
                        times = i["duration"]
                        for r in range(0, int(times)):
                            prefile = os.path.join(PREDIRECTORY, "presession.mp3")
                            sound = AudioSegment.from_mp3(prefile)
                            if r == 0: exportlist = sound
                            else: exportlist += sound
                    ramp = os.path.join(RAMPDIRECTORY, "up", "ar" + str(nextup["number"]) + "2.mp3")
                    sound = AudioSegment.from_mp3(ramp)
                    print(len(ramp))
                    if i["duration"] != 0:
                        exportlist += sound
                    else:
                        exportlist = sound
                elif i == self.cutsinsession[-1]: # POSTSESSION
                    nextdown = self.cutsinsession[x - 1]
                    if int(nextdown["number"]) != 3:
                        ramp = os.path.join(RAMPDIRECTORY, "down", "zr" + str(nextdown["number"]) + "2.mp3")
                    else:
                        ramp = os.path.join(RAMPDIRECTORY, "down", "post2freq.mp3")
                    sound = AudioSegment.from_mp3(ramp)
                    exportlist = sound
                    if i["duration"] is not None:
                        times = i["duration"]
                        for r in range(0, int(times)):
                            postsession = os.path.join(POSTDIRECTORY, "postsession.mp3")
                            sound = AudioSegment.from_mp3(postsession)
                            exportlist += sound
                else:
                    if int(i["number"]) == 3: # TOH SPECIAL
                        nextup = self.cutsinsession[x + 1]
                        previouscut = self.cutsinsession[x - 1]
                        tohdirectory = os.path.join(MAINCUTDIRECTORY, "tohramp")
                        tohfreq = os.path.join(MAINCUTDIRECTORY, "301.mp3")
                        rampin1 = os.path.join(tohdirectory, "3in1.mp3")
                        rampin2 = os.path.join(tohdirectory, "3in2.mp3")
                        rampin3 = os.path.join(tohdirectory, "3in3.mp3")
                        rampout1 = os.path.join(tohdirectory, "3out1.mp3")
                        rampout2 = os.path.join(tohdirectory, "3out2.mp3")
                        rampout3 = os.path.join(tohdirectory, "3out3.mp3")
                        rampinspecial1 = os.path.join(tohdirectory, "3inpresession1.mp3")
                        rampinspecial2 = os.path.join(tohdirectory, "3inpresession2.mp3")
                        rampinspecial3 = os.path.join(tohdirectory, "3inpresession3.mp3")
                        rampoutspecial1 = os.path.join(tohdirectory, "3outpostsession1.mp3")
                        rampoutspecial2 = os.path.join(tohdirectory, "3outpostsession2.mp3")
                        rampoutspecial3 = os.path.join(tohdirectory, "3outpostsession3.mp3")
                        rampindeduction = int()
                        rampoutdeduction = int()
                        if previouscut["number"] == 0:  # Assign Ramp In
                            if 5 >= i["duration"] >= 3: rampin = rampinspecial1; rampindeduction += 1
                            elif 10 >= i["duration"] > 5: rampin = rampinspecial2; rampindeduction += 2
                            else: rampin = rampinspecial3; rampindeduction += 3
                        else:
                            if 5 >= i["duration"] >= 3: rampin = rampin1; rampindeduction += 1
                            elif 10 >= i["duration"] > 5: rampin = rampin2; rampindeduction += 2
                            else: rampin = rampin3; rampindeduction += 3
                        if nextup["number"] == 10:
                            if 5 >= i["duration"] >= 3: rampout = rampoutspecial1; rampoutdeduction += 1
                            elif 10 >= i["duration"] > 5: rampout = rampoutspecial2; rampindeduction += 2
                            else: rampout = rampoutspecial3; rampoutdeduction += 3
                        else:
                            if 5 >= i["duration"] >= 3: rampout = rampout1; rampoutdeduction += 1
                            elif 10 >= i["duration"] > 5: rampout = rampout2; rampoutdeduction += 2
                            else: rampout = rampout3; rampoutdeduction += 3
                        times = (i["duration"] - rampindeduction) - rampoutdeduction
                        for t in range(0, (times + 2)):# ACTUAL TOH EVENT LOOP
                            if t == 0:
                                exportlist = AudioSegment.from_mp3(rampin)
                            elif t == (times + 1): # i["duration"] - 1
                                exportlist += AudioSegment.from_mp3(rampout)
                            else:
                                exportlist += AudioSegment.from_mp3(tohfreq)
                    else: # EVERY OTHER CUT
                            times = i["duration"]
                            for r in range(0, int(times)):
                                nextcut = os.path.join(MAINCUTDIRECTORY, str(i["number"]) + "01.mp3")
                                sound = AudioSegment.from_mp3(nextcut)
                                if r == 0:
                                    exportlist = sound
                                else:
                                    exportlist += sound
                finalfile = os.path.join(TEMPDIRECTORY, str(i["name"]) + ".mp3")
                adjustedvolumelist = exportlist
                adjustedvolumelist.fade_in(5000)
                adjustedvolumelist.export(finalfile, format="mp3")
                testduration = i["duration"]
                if x == 0 or x == (len(self.cutsinsession) - 1):
                    testduration += 2
                completedfile = self.testsession(finalfile, testduration)
                if completedfile is not None:
                    self.cutstoplay.append(finalfile)
                    self.emit(SIGNAL("asignal"))
                    break
                else:
                    print("An Error Occured With File %s, Trying Again..." % finalfile)
                    continue
        self.done = True
        #self.emit(SIGNAL("done"))

    @staticmethod
    def testsession(filetotest, fileduration):
        try:
            filesize = os.stat(filetotest)
            if filesize.st_size < 100000:
                return None
            exportfile = AudioSegment.from_mp3(filetotest)
            exportfileminuteslength = math.floor((len(exportfile) / 1000) / 60)
            filedurationminuteslength = fileduration
            if exportfileminuteslength != filedurationminuteslength:
                with open(ERRORFILES, "a") as file:
                    file.writelines(filetotest)
                # self.emit(SIGNAL("resetpercent"))
                print("%s: %s Is Not Equal To %s" % (filetotest, exportfileminuteslength, filedurationminuteslength))
                return None
            else:
                return filetotest
        except Exception as e:
            print(e)
            return None


