from main_const import SESSIONDATABASE


def _fromUtf8(s): return s


import datetime
import time
import math
import sqlite3 as db

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui


class SessionDatabase(object):
    def __init__(self, mainwindow):
        self.main = mainwindow
        self.conn = db.connect(SESSIONDATABASE)
        now = datetime.datetime.now()
        self.sessiondate = now.strftime("%m/%d/%Y")
        self.tableid = int()
        self.sessiontotal = int()
        self.goalsset = False
        self.completedgoalsset = False
        with self.conn:
            self.cur = self.conn.cursor()
        self.newtable()

    def update(self, currentcut, cutshortduration=None):
        """Method To Update Progress Of One Individual Cut On The Current Session"""
        with self.conn:
            self.cur.execute("SELECT * FROM Sessions WHERE ID='%d'" % self.tableid)
            currentduration = self.cur.fetchone()[int(currentcut["number"]) + 2]
            if cutshortduration is not None:
                newduration = int(currentduration) + int(cutshortduration)
            else:
                if str(currentcut["name"]) in ["Presession", "Postsession"]:
                    newduration = int(currentduration) + int(currentcut["duration"]) + int(currentcut["ramp"])
                else:
                    newduration = int(currentduration) + int(currentcut["duration"])
            self.cur.execute("UPDATE Sessions SET '"+str(currentcut["name"])+"'="+str(newduration)+" WHERE ID='"+str(self.tableid)+"'")
            self.cur.execute("SELECT TOTAL FROM Sessions WHERE ID = '%d'" % self.tableid)
            totalduration = self.cur.fetchone()[0]
            if cutshortduration is not None:
                totalduration += int(cutshortduration)
            else:
                if str(currentcut["name"]) in ["Presession", "Postsession"]:
                    totalduration += int(currentcut["duration"]) + int(currentcut["ramp"])
                else:
                    totalduration += int(currentcut["duration"])
            self.cur.execute("UPDATE Sessions SET TOTAL=? WHERE ID=?", (int(totalduration), self.tableid))

    def deleteifsessionempty(self):
        self.cur.execute('''SELECT Rin, Kyo, Toh, Sha, Kai, Jin, Retsu, Zai, Zen FROM Sessions WHERE ID=?''', (self.tableid,))
        thissession = self.cur.fetchall()[0]
        deletesession = True
        for x, i in enumerate(thissession):
            if int(i) != 0:
                deletesession = False
        if deletesession:
            with self.conn:
                self.cur.execute('''DELETE FROM Sessions WHERE ID=?''', (self.tableid,))

    def insertest(self):
        # Insert Here
        self.checkifcompleted()

    def testifnosessions(self):
        self.cur.execute('''SELECT * FROM Sessions''')
        allsession = self.cur.fetchall()
        if allsession:
            return True
        else:
            return False

    def checkifcompleted(self):
        """Method To Check If A Goal Is Completed. If It Is, Delete It And Ask User For Another Goal"""
        idstomovetocompleted = list()
        currenthours = self.calculatetotalhours()
        if float(currenthours) > float(0):
            self.cur.execute(
                "SELECT Hours FROM Goals"
            )
            val = self.cur.fetchall()
            if val:
                for x, i in enumerate(val[0]):
                    if float(currenthours) >= float(i):
                        idstomovetocompleted.append(x + 1)
            if idstomovetocompleted:
                for i in idstomovetocompleted:
                    self.cur.execute("SELECT Hours FROM Goals WHERE ID='%d'" % i)
                    text = self.cur.fetchone()[0]
                    self.main.goalcompleted("%s Hours" % text)
                    self.movecurrentgoalstocompleted(i)
                if len(val[0]) == len(idstomovetocompleted):
                    self.main.newgoaldialog()

    def movecurrentgoalstocompleted(self, goalid):
        """Method To Get Info From The Goal Id, Delete In Goals Table, And Add To CompletedGoals Table"""
        self.cur.execute("SELECT * FROM Goals WHERE ID = '%d'" % goalid)
        goaltoextract = self.cur.fetchall()[0]
        goalhours = goaltoextract[1]
        todaysdate = time.strftime("%B %d, %Y")
        with self.conn:
            self.cur.execute("DELETE From Goals WHERE ID='%d'" % goalid)
            self.cur.execute(
                "INSERT INTO CompletedGoals "
                "( HOURS, DATECOMPLETED ) "
                "VALUES "
                "( ?, ? );", (goalhours, todaysdate))
        return True

    def goalpacing(self, daysaweekincluded):
        """Method To Display The Average The User Needs To Work A Day In Order To Achieve The Goal By The Due Date"""
        self.checkifcompleted()
        self.cur.execute("SELECT Hours, DUEDATE From Goals")
        val = self.cur.fetchall()
        currentgoal = val[0]
        currentgoalhours = currentgoal[0]
        currentgoalduedate = datetime.datetime.strptime(currentgoal[1], '%m/%d/%Y')
        datetillgoal = currentgoalduedate - datetime.datetime.today()
        daystillgoal = datetillgoal.days
        print("%s Days Till Goal" % daystillgoal)
        weeks = math.floor(daystillgoal / 7)
        daysleft = math.floor(daystillgoal % 7)
        totaldays = int()
        if weeks:
            for i in range(0, weeks):
                for x in range(0, daysaweekincluded):
                    totaldays += 1
        if daysleft:
            totaldays += daysleft
        rawhours = currentgoalhours / totaldays
        hours = math.floor(rawhours)
        if rawhours % 1:
            minutes = math.ceil(60 * (rawhours % 1))
        else:
            minutes = 0
        print("%s Is Equal To %d Hours And %s minutes" % (rawhours, hours, minutes))
        if minutes:
            average = "You Need To Practice For %s Hours And %s Minutes Each Day %s Times A Week To Reach Your Goal" % (hours, minutes, daysaweekincluded)
        else:
            average = "You Need To Practice For %s Hours %s Times A Week To Reach Your Goal" % (hours, daysaweekincluded)
        return average

    def checknewgoals(self, duedate, goalhours):
        """Method To Check The Goals"""
        print("Called checknewgoals() In Session Database")
        tryagain = ". Please Try Again."
        print("Goal Hours Is %s" % goalhours)
        if goalhours > 0:
            if duedate > datetime.datetime.now():
                self.cur.execute("SELECT Hours FROM Goals")
                hourslist = self.cur.fetchall()
                currenthours = self.calculatetotalhours()
                #  print("%s Should Be Greater Than Your Current Hours %s" % (goalhours, currenthours))
                if math.ceil(float(currenthours)) < goalhours:
                    if hourslist: # Setting Goals After First Goal
                        for i in hourslist:
                            if goalhours <= i[0]:
                                return "Goal Must Be Higher Than %s Goals%s" % (hourslist[-1][0], tryagain)
                        self.cur.execute("SELECT DUEDATE FROM Goals")
                        datelist = self.cur.fetchall()[0]
                        for x in datelist:
                            datetimex = datetime.datetime.strptime(x, '%m/%d/%Y')
                            if duedate.date() <= datetimex.date():
                                return "New Goal Must Be Set To Be Due After %s. Please Try Again" % x
                        return True
                    else: # Setting First Goal
                        return True
                else:
                    return "You Have Already Achieved Or Surpassed %s Hours, Select A Higher Goal" % goalhours
            else:
                return "Goal Must Be Set In The Future" + tryagain
        else:
            return "Goal Must Be Set For More Than 0 Hours" + tryagain

    def insertgoal(self, duedate, goalhours):
        with self.conn:
            duedateformatted = duedate.strftime('%m/%d/%Y')
            self.cur.execute(
                "INSERT INTO Goals "
                "( Hours, DUEDATE )"
                "VALUES"
                "( ?, ? )", (goalhours, duedateformatted)
            )

    def displaycurrentgoals(self):
        self.cur.execute("Select * From Goals")
        allgoals = self.cur.fetchall()
        rowcount = len(allgoals)
        currenthours = self.calculatetotalhours()
        if rowcount:
            self.cur.execute('''SELECT Hours, DUEDATE FROM GOALS''')
            listings = self.cur.fetchall()
            readablegoallist = list()
            for x, i in enumerate(listings):
                hours = i[0]
                duedate = i[1]
                percent = int(100 * (float(currenthours) / float(hours)))
                readablegoal = "Goal %d:  %d Hours Due By %s (%d" % (x + 1, hours, duedate, percent)
                readablegoal += "% Complete)"
                readablegoallist.append(readablegoal)
            DisplayGoalsTemplate("Current Goals", "CURRENT GOALS:", readablegoallist)
            return True

    def displaycompletedgoals(self):
        self.cur.execute("Select * From CompletedGoals")
        allgoals = self.cur.fetchall()
        rowcount = len(allgoals)
        if rowcount:
            self.cur.execute('''SELECT HOURS, DATECOMPLETED FROM CompletedGoals''')
            listings = self.cur.fetchall()
            readablegoallist = list()
            for x, i in enumerate(listings):
                hours = i[0]
                duedate = i[1]
                readablegoal = "%d:  %d Hours Completed On %s" % (x + 1, hours, duedate)
                readablegoallist.append(readablegoal)
            DisplayGoalsTemplate("Completed Goals", "COMPLETED GOALS:", readablegoallist)
            return True

    def calculatetotalhours(self):
        """Method To Add All Times From All Sessions From RIN - ZEN"""
        minutes = int()
        cuts = ['Rin', 'Kyo', 'Toh', 'Sha', 'Kai', 'Jin', 'Retsu', 'Zai', 'Zen']
        for x, i in enumerate(cuts):
            self.cur.execute("SELECT "+str(i)+" FROM Sessions")
            val = self.cur.fetchall()
            for t in val:
                minutes += int(t[0])
        hours = "%0.1f" % (minutes / 60)
        return hours

    def calculatetotalhoursandminutes(self):
        minutes = int()
        cuts = ['Rin', 'Kyo', 'Toh', 'Sha', 'Kai', 'Jin', 'Retsu', 'Zai', 'Zen']
        for x, i in enumerate(cuts):
            self.cur.execute("SELECT "+str(i)+" FROM Sessions")
            val = self.cur.fetchall()
            for t in val:
                minutes += int(t[0])
        hours = math.floor(minutes / 60)
        mins = minutes % 60
        return hours, mins

    def getgoalstatus(self):
        """Method To Get Current Goal, And Return str() Goal Current, int() Percentage, str() Goal Total"""
        self.cur.execute("SELECT Hours FROM CompletedGoals")
        completeval = self.cur.fetchall()
        if completeval:
            self.completedgoalsset = True
        self.cur.execute("SELECT Hours FROM Goals")
        val = self.cur.fetchall()
        if val:
            self.goalsset = True
            goalset = val[0]
            goalhours = goalset[-1]
            currenthours = self.calculatetotalhours()
            if currenthours != 0:
                percent = int(100 * (float(currenthours) / float(goalhours)))
                if percent >= 100:
                    # Call Completed Goals Here
                    percentage = 100
                else:
                    percentage = percent
            else:
                percentage = 0
            goaltotal = str(goalhours) + " hrs"
            goalcurrent = str(currenthours) + " hrs" # Append Integer Value To hrs and return
            return goalcurrent, percentage, goaltotal
        else:
            return None, None, None

    def newtable(self):
        """Method To Create The Tables For The Session If They Don't Already Exist"""
        with self.conn:
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS Sessions ("
                "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                "DATEPRACTICED VARCHAR(10), "
                "Presession INTEGER, "
                "Rin INTEGER, "
                "Kyo INTEGER, "
                "Toh INTEGER, "
                "Sha INTEGER, "
                "Kai INTEGER, "
                "Jin INTEGER, "
                "Retsu INTEGER, "
                "Zai INTEGER, "
                "Zen INTEGER, "
                "Postsession INTEGER, "
                "TOTAL INTEGER)"
            )
        with self.conn:
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS PrematureEndings ("
                "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                "DATEPRACTICED TEXT, "
                "CUT TEXT, "
                "SESSIONNAME TEXT, "
                "REASON TEXT)"
            )
        with self.conn:
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS Goals ("
                "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                "HOURS INTEGER, "
                "DUEDATE TEXT)"
            )
        with self.conn:
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS CompletedGoals ("
                "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                "HOURS INTEGER, "
                "DATECOMPLETED TEXT)"
            )

    def deleteallgoals(self):
        self.cur.execute("DROP TABLE Goals")

    def calculatetotalminutesforindividualcut(self, cutnumber, listofguiobjectsdayshoursminutes):
        """Method To Convert Minutes To Days, Hours And Minutes And Display In The GUI"""
        cuts = ['Rin', 'Kyo', 'Toh', 'Sha', 'Kai', 'Jin', 'Retsu', 'Zai', 'Zen']
        thiscut = cuts[cutnumber]
        self.cur.execute("SELECT "+str(thiscut)+" FROM Sessions")
        val = self.cur.fetchall()
        rawminutes = int()
        for t in val:
            rawminutes += int(t[0])
        # if rawminutes >= 1440:
        #     days = math.trunc((rawminutes / 24) / 60)
        #     rawminutes -= ((days * 24) * 60)
        # else: days = 0
        if rawminutes >= 60:
            hours = math.trunc(rawminutes / 60)
            rawminutes -= (hours * 60)
        else: hours = 0
        minutes = rawminutes
        currentlist = listofguiobjectsdayshoursminutes
        durations = [hours, minutes]
        for x, i in enumerate(currentlist):
            i.display(durations[x])
        return True

    def createnewsession(self):
        """Method To Create A New Session And Add It To The Table"""
        with self.conn:
            self.cur.execute(
                "INSERT INTO Sessions "
                "( DATEPRACTICED, Presession, Rin, Kyo, Toh, Sha, Kai, Jin, Retsu, Zai, Zen, Postsession, TOTAL ) "
                "VALUES "
                "( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );", (self.sessiondate, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            self.cur.execute("SELECT max(ID) From Sessions")
            self.tableid = self.cur.fetchone()[0]

    def closeconnection(self):
        self.conn.close()

    def writeprematureending(self, cut, sessiontimeslist, reason):
        with self.conn:
            txt = str()
            for x, i in enumerate(sessiontimeslist):
                txt += i
                if x != (len(sessiontimeslist) - 1):
                    txt += ", "
            self.cur.execute(
                "INSERT INTO PrematureEndings "
                "( DATEPRACTICED, CUT, SESSIONNAME, REASON ) "
                "VALUES "
                "( ?, ?, ?, ? );", (self.sessiondate, str(cut), txt, str(reason)))


class DisplaySessionList(QDialog):
    def __init__(self, parent, SessionDatabase):
        QWidget.__init__(self, parent)
        self.sessiondb = SessionDatabase
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(0, 0, 1150, 815))
        self.setWindowTitle("Session List")

        self.sessiondb.cur.execute('''SELECT * FROM Sessions''')
        allsession = self.sessiondb.cur.fetchall()
        rowcount = len(allsession)
        if rowcount:
            self.tableWidget.setRowCount(rowcount)
            self.sessiondb.cur.execute('''SELECT DATEPRACTICED, Rin, Kyo, Toh, Sha, Kai, Jin, Retsu, Zai, Zen, TOTAL FROM Sessions''')
            listings = self.sessiondb.cur.fetchall()
            columncount = len(listings[0])
            self.tableWidget.setColumnCount(columncount)
            self.tableWidget.setHorizontalHeaderLabels(['Date', 'Rin', 'Kyo', 'Toh', "Sha", 'Kai', 'Jin', 'Retsu', 'Zai', 'Zen', 'Total'])
            for row, form in enumerate(listings):
                for column, item in enumerate(form):
                    if column == 0:
                        it = QTableWidgetItem(str(item))
                        self.tableWidget.setItem(row, column, it)
                        it.setTextAlignment(Qt.AlignCenter)
                        it.setFlags(QtCore.Qt.ItemIsEnabled)
                    else:
                        if int(item) < 60:
                            if int(item) == 0:
                                it = QtGui.QTableWidgetItem('-')
                            else:
                                it = QtGui.QTableWidgetItem(str(item) + " min")
                            self.tableWidget.setItem(row, column, it)
                            it.setTextAlignment(QtCore.Qt.AlignCenter)
                            it.setFlags(QtCore.Qt.ItemIsEnabled)
                        else:
                            hours = math.trunc(int(item) / 60)
                            minutes = math.trunc(int(item) % 60)
                            if hours > 1: hourslabel = " hrs "
                            else: hourslabel = " hr "
                            if minutes != 0:
                                it = QtGui.QTableWidgetItem(str(hours) + hourslabel + str(minutes) + " min")
                            else:
                                it = QtGui.QTableWidgetItem(str(hours) + hourslabel)
                            self.tableWidget.setItem(row, column, it)
                            it.setTextAlignment(QtCore.Qt.AlignCenter)
                            it.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.show()
            self.exec_()


class DisplayPrematureEndings(QDialog):
    def __init__(self, parent, SessionDatabase):
        QWidget.__init__(self, parent)
        self.sessiondb = SessionDatabase
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(0, 0, 1150, 815))
        self.setWindowTitle("Premature Endings List")
        self.sessiondb.cur.execute('''SELECT * FROM PrematureEndings''')
        allsession = self.sessiondb.cur.fetchall()
        self.rowcount = len(allsession)

    def testforprematureendings(self):
        if self.rowcount:
            self.tableWidget.setRowCount(self.rowcount)
            self.sessiondb.cur.execute('''SELECT DATEPRACTICED, CUT, SESSIONNAME, REASON FROM PrematureEndings''')
            listings = self.sessiondb.cur.fetchall()
            columncount = len(listings[0])
            self.tableWidget.setColumnCount(columncount)
            self.tableWidget.setHorizontalHeaderLabels(['Date Practiced',
                                                        'Last Cut Practiced Before Ending Early',
                                                        'Session Expected To Be Completed',
                                                        'Reason For Ending This Session Early'])
            for row, form in enumerate(listings):
                for column, item in enumerate(form):
                    it = QtGui.QTableWidgetItem(str(item))
                    self.tableWidget.setItem(row, column, it)
                    self.tableWidget.resizeColumnsToContents()
                    it.setTextAlignment(QtCore.Qt.AlignCenter)
                    it.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.show()
            self.exec_()
            return True
        else:
            return False


class DisplayGoalsTemplate(QDialog):
    def __init__(self, windowtitle, toplabel, listofreadablegoals):
        QDialog.__init__(self)
        self.resize(417, 353)
        self.setStyleSheet("background-color:#212526;")
        self.goallabel = QLabel(self)
        self.goallabel.setGeometry(QRect(40, 20, 341, 20))
        self.goalsList = QListWidget(self)
        self.goalsList.setStyleSheet(("color: #98A6A8;\n"
"background-color: rgb(42, 52, 53);"))
        self.goalsList.setGeometry(QRect(30, 50, 351, 251))
        self.goallabel.setAlignment(Qt.AlignCenter)
        self.goalslistOKButton = QPushButton(self)
        self.goalslistOKButton.setGeometry(QRect(320, 310, 84, 30))
        self.setWindowTitle(windowtitle)
        self.goallabel.setText(toplabel)
        self.goallabel.setStyleSheet("color: #98A6A8;")
        self.goalslistOKButton.setText("OK")
        self.goalslistOKButton.setStyleSheet("color: #98A6A8; background-color: rgb(53, 63, 68);")
        QObject.connect(self.goalslistOKButton, SIGNAL("clicked()"), self.accept)
        for i in listofreadablegoals:
            item = QListWidgetItem()
            item.setText(i)
            self.goalsList.addItem(item)
        self.exec_()