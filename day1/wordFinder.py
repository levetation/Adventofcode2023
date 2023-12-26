words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]



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

    ## Need to convert words into integers
    ## copy above function into main script...



if __name__ == '__main__':
    
    # examples
    examples = {
    "two1nine":29,
    "eighttwothree": 83,
    "abcone2threexyz" : 13,
    "ftgbfqrzslqrcmmeightnjjrrkvhntcv1djmbqztrklqfkshoneeightggd": 88,
    }

    for string, value in examples.items():
        print(string ,wordFinder(string))
    
    
