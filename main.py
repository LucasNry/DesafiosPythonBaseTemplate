import os

output_list = []
is_debugging = True

"""
This is the function in which you should solve the exercise
Do NOT print anything, add all your output lines as Strings in the variable output_list 
"""
def execute(is_debugging):
    inputList = getInput(is_debugging)
    # Add your code here...








#------------------------------------------------------------------------------
# DO NOT CHANGE ANY OF THE CODE BELOW
#------------------------------------------------------------------------------

def getInput(is_debugging):
    inputList = []
    if is_debugging:
        file = open("./assets/inputFile.txt", "r")
        inputList = file.readlines()
        for i in range(0, len(inputList)):
            inputList[i] = inputList[i].replace("\n", "")
    else:
        while True:
            try:
                line = input()
                inputList.append(line)
            except EOFError:
                break
    
    return inputList

def print_results():
    for line in output_list:
        print(line)

def write_results_to_file():
    for i in range(0, len(output_list)):
        output_list[i] += "\n"

    file = open("outputFile.txt", "w")
    file.writelines(output_list)
    file.close()

def debug():
    os.system("cd ../DesafiosDebugger && java DesafiosDebugger a")

if __name__ == "__main__":
    execute(is_debugging)
    write_results_to_file()
    if not is_debugging:
        print_results()
    else: 
        debug()