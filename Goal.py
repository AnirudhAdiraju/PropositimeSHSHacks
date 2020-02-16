'''
The Goal class is where the user defines there own goals.
Each goal has a string stating the goal, the notifying time, notifying units, goal length, and goal units.
'''
class Goal:
    def __init__(self, goal, notifyTime, notifyUnits, goalLength, goalUnits):
        self.goal = goal
        self.notifyTime = notifyTime
        self.notifyUnits = notifyUnits
        self.goalLength = goalLength
        self.goalUnits = goalUnits

    def setGoal(self, newGoal):
        self.goal = newGoal

    def setNotifyTime(self, newNotifyTime):
        self.notifyTime = newNotifyTime

    def setNotifyUnits(self, newNotifyUnits):
        self.notifyUnits = newNotifyUnits

    def setGoalLength(self, newGoalLength):
        self.goalLength = newGoalLength

    def setGoalUnits(self, newGoalUnits):
        self.goalUnits = newGoalUnits

    def getGoal(self):
        return self.goal

    def getNotifyTime(self):
        return self.notifyTime

    def getNotifyUnits(self):
        return self.notifyUnits

    def getGoalLength(self):
        return self.goalLength

    def getGoalUnits(self):
        return self.goalUnits