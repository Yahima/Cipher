# coding=utf-8
from operator import itemgetter

code_in = "xureveoulrefknpavberweqwuegwceappergvleovlrazfbevdfaewmedfbwubjvbyenpfalusfeabdensavlvbyenav" \
          "becalexwsbeabdevecvppeyvtfeqwueaejwonpfrfeajjwubrewmergfelqlrfoeabdefknwubdergfeajruaperfajg" \
          "vbylewmergfeysfarefknpwsfsewmergfersurgergfeoalrfsexuvpdfsewmeguoabegannvbfll"

code_out = ""
code = {}

engdict = open('dict/engmix.txt').read()


# Erzeugt dictionary mit den erlaubten Zeichen als keys mit 0 als value.
def createAlphabet():
    alpha_list = {}
    for c in range(ord('a'), ord('z') + 1):
        alpha_list[chr(c)] = chr(c)
    alpha_list[' '] = ' '
    print(alpha_list)

    return alpha_list


# Erzeugt Liste mit den Zeichen in coded_input sorttiert nach Frequenz.
def sortByFrequency(coded_input):
    frequency_list = createAlphabet()
    for x in frequency_list:
        for c in coded_input:
            if x == c:
                frequency_list[c] += 1
    frequency_list = sorted(frequency_list.items(), key=itemgetter(1), reverse=True)

    return frequency_list


# Gibt true zurück wenn word im Worterbuch enthalten ist, sonst false.
def existsInDict(word):
    if word in engdict:
        return True

    return False


# Gibt true zurück wenn alle Wörter in coded_input im Worterbuch enthalten sind, sonst false.
def allInDict(coded_input):
    for s in coded_input.split(' '):
        if s in engdict:
            decoded = True;
        else:
            decoded = False
            break

    return decoded


# Ersstzt alle char Zeichen durch das Leerzeichen.
def setSpace(coded_input, char):
    return str.replace(coded_input, char, ' ')


# Ersetzt frequente Charaktere in code_code mit frequenten Charakteren in der Sprache.
def replaceByFrequency(coded_input, language_frequency_list):
    frequency_list = sortByFrequency(coded_input)
    for x in frequency_list:
        for y in language_frequency_list:
            for c in coded_input:
                if c == x:
                    coded_input.replace(c, y)

    return coded_input


# Ersetzt Charaktere in coded_input mit den korrespondiererenden value in code_list.
def replace(coded_input, code):
    coded_output = ""
    for c in coded_input:
        for key, value in code.items():
            if c == key:
                coded_output = str.replace(coded_input, c, value)
                break

    return coded_output


def setCode()

def decode(coded_input):
    alpha = createAlphabet()
    frequency_list = sortByFrequency(coded_input)
    while not allInDict(coded_input):
       for f in frequency_list:
                print str.replace(coded_input, c, a)


def cipher(coded_input):
    int cipher code

#print setSpace(code_in, sortByFrequency(code_in)[0][0])
print replace(code_in, createAlphabet())
