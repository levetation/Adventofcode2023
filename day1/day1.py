integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
intwordConvert = dict(zip(words, integers)) # word & number look-up table

def convertToInteger(val):
    if val in words: return int(intwordConvert[val])
    else: return int(val)

## Main function
def buildInt(string):
    db = {}
    
    # check for integers
    for position, integer in enumerate(string):
        if integer in integers:
            db[position] = integer

    # check for words
    for word in words:
        if word in string:
            wordPosition = string.find(word)
            db[wordPosition] = word

    # find lowest and highest positions and their assoc values
    first = convertToInteger(db[min(db)])
    last = convertToInteger(db[max(db)])  
    concat = f'{first}{last}'
    return int(concat)

if __name__ == '__main__':
  
    ## Test function works
    examples = {"two1nine":29,
    "eightwothree": 83,
    "abcone2threexyz": 13,
    "xtwone3four": 24,
    "4nineeightseven2": 42,
    "zoneight234": 14,
    "7pqrstsixteen": 76}

    passed = 0
    for string, value in examples.items():
        print(string)
        builtInt = buildInt(string)
        print(builtInt)
        if builtInt == value: print("Pass"); passed +=1

    ## Solve problem if func passes test
    if passed >= 7:
        print("Tests passed!")
        with open('day1/input.txt') as inputText:
            inputText = inputText.read().split('\n')
        for string in inputText: print(string); print(buildInt(string)) 
        print("Final answer:", sum([buildInt(row) for row in inputText]))