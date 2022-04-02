class Calculator:
    val1 = 0
    val2 = 0

    def adder(self):
        print(self.val1 + self.val2)

    def subber(self):
        print(self.val1 - self.val2)

    def multi(self):
        print(self.val1 * self.val2)

    def divi(self):
        print(self.val1 /self.val2)

    def clear(self):
        val1 = 0
        val2 = 0
        print("Values cleared")

class clockTime:
    hours = 0
    minutes = 0
    seconds = 0
    def setHours(self, x):
        if x > 23:
            x = 23
        self.hours = x

    def setMins(self, x):
        if x > 59:
            x = 59
        self.minutes = x

    def setSecs(self, x):
        if x > 59:
            x = 59
        self.seconds = x

    def setTime(self, x, y, z):
        self.setHours(x)
        self.setMins(y)
        self.setSecs(z)

    def showTime(self):
        print("{}:{}:{}".format(self.hours, self.minutes, self.seconds))

#Question 1
myCalc = Calculator()
print('Insert value 1')
myCalc.val1 = int(input())
print("insert value 2")
myCalc.val2 = int(input())
myCalc.adder()
myCalc.subber()
myCalc.multi()
myCalc.divi()
myCalc.clear()

#Question 2
myClock = clockTime()
print('Insert Hours')
x = int(input())
myClock.setHours(x)
print("insert Minutes")
x = int(input())
myClock.setMins(x)
print("insert Seconds")
x = int(input())
myClock.setSecs(x)
myClock.showTime()
