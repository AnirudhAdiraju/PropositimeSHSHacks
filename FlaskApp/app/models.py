import time
import threading
from threading import Thread
everyusername = []
everyone = []
class User:
    def __init__(self, username, password, email):
        self.isLoggedIn = False
        self.username = username
        self.password = password
        self.email = email
        self.id = nextAvailableId()
        self.friends = []
        self.goals = []
        self.requests = []
        self.badges = BadgeSet()
        global everyone
        everyone.append(self)
        global everyusername
        everyusername.append(self.username)

    def login(self):
        isLoggedIn = True

    def getUsername(self):
        return self.username

    def logout(self):
        isLoggedIn = False

    def addGoal(self, goal, notifyTime, notifyUnits, goalLength, goalUnits, final, finalUnits):
        self.goals += Goal(goal, notifyTime, notifyUnits, goalUnits, goalLength, goalUnits, final, finalUnits)

    def addFriend(self, other):
        other.addRequest(self)

    def permaFriend(self, other):
        self.friends += other

    def addRequest(self, other):
        self.requests += other

    def removeRequest(self, other):
        self.requests.remove(other)

    def reply(self, other, want):
        if other in self.requests and want:
            self.permaFriend(other)
            other.permaFriend(self)
            self.removeRequest(other)
            other.removeRequest(self)
        elif other in self.requests and not want:
            self.removeRequest(other)
            other.removeRequest(self)

    def getPassword(self):
        return self.password


class Goal:
    def __init__(self, goal, notifyTime, notifyUnits, goalLength, goalUnits, final, finalUnits):
        self.goal = goal
        if goalUnits == 'seconds':
            self.seconds = goalLength*goalUnits

        elif goalUnits == 'minutes':
            self.seconds = goalLength*goalUnits*60

        elif goalUnits == 'hours':
            self.seconds = goalLength*goalUnits*3600

        elif goalUnits == 'days':
            self.seconds = goalLength*goalUnits*86400

        elif goalUnits == 'weeks':
            self.seconds = goalLength*goalUnits*604800

        elif goalUnits == 'months':
            self.seconds = goalLength*goalUnits*2592000

        elif goalUnits == 'years':
            self.seconds = goalLength*goalUnits*31536000

        else:
            self.seconds = goalLength*goalUnits*315360000

        self.timeLeft = self.seconds
        self.notifyTime = notifyTime
        self.notifyUnits = notifyUnits
        self.final = final
        self.finalUnits = finalUnits
        self.progress = 0
        self.startTime()

    def startTime(self):
        background_timer = Thread(target=self.timer, args=(self.seconds,))

    def timer(self):
        start = time.time()
        while (time.time() - start < self.seconds):
            self.timeLeft -= time.time() - start
            continue
        return "Time is up!"

    def makeProgress(self, units):
        self.progress += units

    def isGoalComplete(self):
        return self.progress == self.final

    def getGoal(self):
        return self.goal

    def getNotifyTime(self):
        return self.notifyTime

    def getNotifyUnits(self):
        return self.notifyUnits




class Badge:
    def __init__(self, path, name, description, isAwarded):
        self.path = path
        self.name = name
        self.description = description
        self.isAwarded = isAwarded

    def setIsAwarded(self, bool1):
        if bool1:
            self.isAwarded = True
        else:
            self.isAwarded = False

    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getIsAwarded(self):
        return self.isAwarded


class BadgeSet:
    def __init__(self):
        self.badgeList = [Badge("bmedal1.PNG", "Starting out", "set a goal", False),
                     Badge("bmedal2.PNG", "Friends!", "make a friend", False),
                     Badge("bmedal3.PNG", "Together We Start", "create a shared goal with your friends", False),
                     Badge("bmedal4.PNG", "More Goals", "set 10 goals", False),
                     Badge("bmedal5.PNG", "Reaching the Finish Line", "finish a goal", False),
                     Badge("bmedal6.PNG", "Marathon", "finish a goal that took longer than 26 hours", False),
                     Badge("bmedal7.PNG", "Friend Circle!", "make 5 friends", False),
                     Badge("bmedal8.PNG", "Sweet Victory", "win a competition", False),
                     Badge("bmedal9.PNG", "Room for Improvement", "lose a competition", False),
                     Badge("bmedal10.PNG", "Tournament Player", "participate in 10 competitions", False),
                     Badge("dmedal1.png", "Tough Luck", "lose 200 competitions", False),
                     Badge("dmedal2.png", "Finishing V", "finish 500 goals", False),
                     Badge("dmedal3.png", "Overpowered", "win 1000 competitions", False),
                     Badge("gmedal1.png", "Share the Wealth", "win 25 competitions with friends", False),
                     Badge("gmedal2.png", "Smart Setter", "set 100 goals", False),
                     Badge("gmedal3.png", "Finishing IV", "finish 100 goals", False),
                     Badge("gmedal4.png", "God Mode", "win 100 competitions", False),
                     Badge("gmedal5.png", "Insane Person", "place top 10 in daily goals challenge", False),
                     Badge("smedal1.png", "Finishing II", "set 10 goals", False),
                     Badge("smedal2.png", "Productive Person", "set 50 goals", False),
                     Badge("smedal3.png", "Marathon II", "finish a goal that took a month", False),
                     Badge("smedal4.png", "Popular Person", "make 20 friends", False),
                     Badge("smedal5.png", "Victorious", "win 20 competitions", False),
                     Badge("smedal6.png", "Hard Loser", "lose 10 competitions", False),
                     Badge("smedal7.png", "Finishing III", "finish 50 goals", False)]


    def awardBadge(self, badge):
        self.badgeList[badge-1].setIsAwarded(True)

def nextAvailableId():
    return len(everyone) + 1

