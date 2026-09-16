class Interpreter:
    def __init__(self, A, inputBuffer):
        self.pointer = 0
        self.A = A
        self.inputBuffer = inputBuffer

    def readInstruction(self):
        instructionData = self.A[self.pointer]
        instructionData, instructionType = divmod(instructionData, 100)

        myInstruction = None
        if instructionType == 1:
            myInstruction = InstructionAdd()
        elif instructionType == 2:
            myInstruction = InstructionMul()
        elif instructionType == 3:
            myInstruction = InstructionIn(self.inputBuffer.pop())
        elif instructionType == 4:
            myInstruction = InstructionOut()
        elif instructionType == 99:
            myInstruction = InstructionEnd()

        for i in range(1, myInstruction.paramCount+1):
            instructionData, paramMode = divmod(instructionData, 10)
            if paramMode == 0:
                if instructionType == 3:
                    myInstruction.params.append(self.A[self.pointer + i])
                else:
                    myInstruction.params.append(self.A[self.A[self.pointer + i]])
            elif paramMode == 1:
                myInstruction.params.append(self.A[self.pointer + i])
        
        val = myInstruction.execute()
        storage = myInstruction.store
        if storage is not None:
            self.A[storage] = val
        self.pointer += myInstruction.paramCount + 1

class Instruction:
    def __init__(self):
        self.paramCount = 0
        self.params = []
        self.store = None

class InstructionAdd(Instruction):
    def __init__(self):
        super().__init__()
        self.paramCount = 3

    def execute(self):
        self.store = self.params[2]
        return self.params[0] + self.params[1]

class InstructionMul(Instruction):
    def __init__(self):
        super().__init__()  
        self.paramCount = 3

    def execute(self):
        self.store = self.params[2]
        return self.params[0] * self.params[1]

class InstructionIn(Instruction):
    def __init__(self, inputNum):
        super().__init__()
        self.inputNum = inputNum
        self.paramCount = 1

    def execute(self):
        self.store = self.params[0]
        return self.inputNum

class InstructionOut(Instruction):
    def __init__(self):
        super().__init__()
        self.paramCount = 1

    def execute(self):
        print(self.params[0])


class InstructionEnd(Instruction):
    def __init__(self):
        super().__init__()
        self.paramCount = 0

    def execute(self):
        exit()

if __name__ == "__main__":
    #    0 1 2 3  4 5  6  7  8  9  10
    A = [3,225,1,225,6,6,1100,1,238,225,104,0,1001,92,74,224,1001,224,-85,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1101,14,63,225,102,19,83,224,101,-760,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,21,23,224,1001,224,-44,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1102,40,16,225,1102,6,15,225,1101,84,11,225,1102,22,25,225,2,35,96,224,1001,224,-350,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,56,43,225,101,11,192,224,1001,224,-37,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1002,122,61,224,1001,224,-2623,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1,195,87,224,1001,224,-12,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,75,26,225,1101,6,20,225,1102,26,60,224,101,-1560,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,226,224,102,2,223,223,1006,224,329,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,344,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,359,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,389,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,404,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,434,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,449,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,464,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,524,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,539,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,554,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,569,101,1,223,223,107,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,599,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,7,226,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,659,1001,223,1,223,1008,226,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]
    print(len(A))
    myInterpreter = Interpreter(A, [1])
    while True:
        myInterpreter.readInstruction()
