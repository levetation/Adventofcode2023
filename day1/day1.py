integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
intwordConvert = dict(zip(words, integers)) # word & number look-up table

def convertToInteger(val):
    if val in words: return int(intwordConvert[val])
    else: return int(val)

def wordFinder(word_):
    word = word_.lower()
    dic = {}
    for w in words: 
        if w in word:
            # print(w)
            wordCount = word.count(w)
            # print("WordCount", wordCount)
            wordPos = word.find(w)
            # print("wordPos", wordPos)
            dic[wordPos] = w
            if wordCount > 1:
                loopCounter = wordCount - 1
                while loopCounter > 0:
                    # print("loopCounter", loopCounter)
                    pp = wordPos+len(w)
                    wordPos = word[pp::].find(w)
                    dic[wordPos+pp] = w
                    # print("wordPos", wordPos)
                    loopCounter -= 1
    return dic

## Main function
def buildInt(string):
    db = {}
    
    # check for integers
    for position, integer in enumerate(string):
        if integer in integers:
            db[position] = integer

    # check for words
    # for word in words:
    #     if word in string:
    #         # dealing with repeats: this is probs dumb
    #         if int(string.count(word)) > 1:
    #             print(f"repeat: {word}, count: {string.count(word)}")
    #             wordPosition = string.find(word)
    #             db[wordPosition] = word

    #             counter = string.count(word)
    #             position = wordPosition
    #             while counter > 0:
    #                 newString = string[position+len(word)::]
    #                 newPosition = newString.find(word)
    #                 db[position+newPosition] = word
    #                 position += newPosition
    #                 counter -= 1
    #         else:
    #             wordPosition = string.find(word)
    #             db[wordPosition] = word
    wordIntDic = wordFinder(string)
    db.update(wordIntDic)

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
    "7pqrstsixteen": 76,
    "ftgbfqrzslqrcmmeightnjjrrkvhntcv1djmbqztrkvlqfkshoneightggd": 88,
    }

    passed = 0
    for string, value in examples.items():
        builtInt = buildInt(string)
        print(string, builtInt)
        if builtInt == value: 
            print("Pass")
            passed +=1
        else:
            print(f"Fail: got {builtInt}, should be {examples[string]}")

    ## Solve problem if func passes test
    if passed >= 8:
        with open('input.txt') as inputText:
            inputText = inputText.read().split('\n')
        for string in inputText:
            print(string); print(buildInt(string)) 
        print("\nTests passed!")
        print("Final answer:", sum([buildInt(row) for row in inputText]))
    else:
        print("\nTests failed :(")
