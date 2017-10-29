from operator import itemgetter

code_in = "xureveoulrefknpavberweqwuegwceappergvleovlrazfbevdfaewmedfbwubjvbyenpfalusfeabdensavlvbyenav" \
          "becalexwsbeabdevecvppeyvtfeqwueaejwonpfrfeajjwubrewmergfelqlrfoeabdefknwubdergfeajruaperfajg" \
          "vbylewmergfeysfarefknpwsfsewmergfersurgergfeoalrfsexuvpdfsewmeguoabegannvbfll"

engdict = open("dict/engmix.txt").read()

def createAlphabet():

    alpha_list = {}
    for c in range(ord('a'), ord('z') + 1):
        alpha_list[chr(c)] = 0
    alpha_list[' '] = 0
    print(alpha_list)

    return alpha_list


def sortByFrequency(code):

    frequency_list = createAlphabet()
    for x in frequency_list:
        for c in code:
            if x == c:
                frequency_list[c] += 1
    frequency_list = sorted(frequency_list.items(), key = itemgetter(1), reverse = True)

    return frequency_list

def existsInDict(word):

    if word in engdict:
        return True

    return False

def allInDict(code):

    for s in code.split(' '):
        if s in engdict:
            decoded = True;
        else:
            decoded = False
            break

    return decoded

def replaceByFrequency(code):

    frequency_list = sortByFrequency(code)
    print(frequency_list)


def decode(code):

    return code

replaceByFrequency(code_in)