class Collatz:

    def __init__(self, maxIterations: int = 6000):
        """Initalises this class.

    Parameters:
    maxIternations (int): Max number of iterations before deciding that the number does not align with Collatz Conjencture. Making this number big does not negatively impact the efficiency of other numbers with lower iterations needed."""

        self.maxIteration = maxIterations
    
    def check(self, number: int):
        """Checks if a particular numbers align with Collatz Conjecture (within maxIterations iterations)

    Parameters:
    number (int): the number to check if aligns with Collatz Conjecture.
    
    Returns:
    tuple: returns a tuple with the first value (boolean) representing whether the number aligns with Collatz Conjecture or not, and the second (int) is the number of steps (or iterations) needed to reach 1. If the number does not align with Collatz Conjecture within maxIterations steps, then maxIterations value is returned. 
    """

        isCollatz = False
        steps = self.maxIteration
        for i in range(self.maxIteration):
            if number == 1: # Base case
                isCollatz = True
                steps = i
                break # no need to continue as it will 4-2-1 loop again and again until maxIterations, so stop to improve efficiency.
            if (number % 2 == 0):
                number = number  // 2 # integer division since no floating point operations are needed, improving the efficiency.
            else:
                number = 3 * number + 1

        return isCollatz, steps
    
    def analyse(self, number: int):
        """Analyses a particular number, in terms of does it align with Collatz Conjecture, and if so how many steps are required, how many of which are even or odd, and what is the maximum number reached.

    Parameters:
    number (int): the number to analyse.
    
    Returns:
    Object: returns an Object with the following keys: "isCollatz" which will have a boolean value indicating whether the number aligns with Collatz Conjecture or not, "steps" which will have an integer value of the number of steps requried to reach 1, "moves" which will have a value of array of integers containing all the steps taken until 1, "maxReached" which will have an (int, int) tuple value, in which the first value is the maximum number reached and the second is the step number, and finally "evenSteps" and "oddSteps" which will have integer values representing the number of even or odd steps.
    """
        isCollatz = False
        steps = self.maxIteration # NB: even though other sources might consider steps = moves, the steps represnt the arthimetic steps taken to reach 1. Hence, the number of steps will always be 1 less than the moves. 
        moves = []
        maxNumberReached = (number, 0) # this is set so: moves[maxNumberReached[1]] = maxNumberReached[0]
        evenSteps, oddSteps = 0, 0
        for i in range(self.maxIteration):
            moves.append(number)
            if (number > maxNumberReached[0]):
                maxNumberReached = number, i
            if number == 1:
                isCollatz = True
                steps = i
                break
            if (number % 2 == 0):
                number = number // 2
                evenSteps += 1
            else:
                number = 3 * number  + 1
                oddSteps += 1
        return {
            "isCollatz": isCollatz,
            "steps": steps,
            "moves": moves,
            "maxReached": maxNumberReached,
            "evenSteps": evenSteps,
            "oddSteps": oddSteps
        }
    
    def checkUntil(self, testUntil: int, testFrom: int = 1):
        """Checks if all numbers within a range from testFrom (or 1) to testUntil align with Collatz Conjecture (within maxIterations iterations)

    Parameters:
    testUntil (int): the upper limit of the range of number to be checked (inclusive).
    [testFrom] (int): the lower limit of the range of numbers to be checked (inclusive). Unless otherwise is provided, then it is 1.
    
    Returns:
    tuple: Returns a tuple of type (boolean, int) in which the first value is boolean, which will only be true if all numbers within the range align with Collatz Conjecture, and the second is of type integer which indicates the first number that does not align with Collatz Conjecture in this range (within maxIterations iterations). If all numbers do so, then -1 is the second value.
    """
        testResult = True
        testFails = -1
        for number in range(testFrom, testUntil + 1):
            if self.check(number)[0] == False:
                testResult = False
                testFails = number
                break
        return testResult, testFails
    
    def analyseUntil(self, testUntil: int, testFrom: int = 1):
        """Analyses a range of numbers, in terms of whether they do align with Collatz Conjecture or not, and if so how many and what number needed most steps, what numbers needed each number of steps, how much and what number reached the highest number within its steps, and what numbers reached each value. 

    Parameters:
    testUntil (int): the upper limit of the range of number to be analysed (inclusive).
    [testFrom] (int): the lower limit of the range of numbers to be analysed (inclusive). Unless otherwise is provided, then it is 1.
    
    Returns:
    Object: returns an object with the following keys: "areCollatz" which will contain a boolean value which is to be true only if all numbers in the range align with Collatz Conjecture, "maxSteps" which will have a tuple value of type (int, int) in which the first is the maximum number of steps of all the numbers in the range and the second is the number which required that many steps (If many, the highest is returned), "maxStepsNumbers" will have an object as its value with the keys being the number of steps needed and the values (lists) are the numbers which needed each step. Similarly, "maxReached" is also a key in the returned object containing a tuple of type (int, int) with the first being the maximum reached number of all numbers in the range and the second is the number which had this highest reached number in its steps (If many, the highest is returned), and "maxReachedNumbers" which will contain an object with the keys of all maximum reached numbers of all the numbers in the range and values of the numbers which had each highest reached number.
    """
        obj = {
            "areCollatz": True,
            "maxSteps": (-1,-1), # (max reached, number)
            "maxStepsNumbers": {}, # each number must be in no more than one list in all the keys.
            "maxReached": (-1,-1), # (max reached, number)
            "maxReachedNumbers": {} # each number must be in no more than one list in all the keys.
        }
        for number in range(testFrom, testUntil + 1):
            analysis = self.analyse(number)
            if analysis["isCollatz"] == False:
                obj["areCollatz"] = False
                continue
            else:
                if analysis["steps"] in obj["maxStepsNumbers"]:
                    obj["maxStepsNumbers"][analysis["steps"]].append(number)
                else:
                    obj["maxStepsNumbers"][analysis["steps"]] = [number]
                if analysis["maxReached"][0] in obj["maxReachedNumbers"]:
                    obj["maxReachedNumbers"][analysis["maxReached"][0]].append(number)
                else:
                    obj["maxReachedNumbers"][analysis["maxReached"][0]] = [number]

        maxStep = sorted(obj["maxStepsNumbers"].items())[-1][0] # sorting the dict to get the highest key which will represent the maximum steps needed
        obj["maxSteps"] = (maxStep, obj["maxStepsNumbers"][maxStep][-1])
        maxReached = sorted(obj["maxReachedNumbers"].items())[-1][0] # sorting the dict to get the highest key which will represent the maximum number reached
        obj["maxReached"] = (maxReached, obj["maxReachedNumbers"][maxReached][-1])
        return obj
