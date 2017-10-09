#coding:utf-8

from random import randint

name = 'hekang'
age = randint(18,25) #产生随机数，范围是[18,25]

# print 'Who do you think i am?'
try:
    x = raw_input('Who do you think i am?\n')
    if x == name:
        print 'Oh,yes!'
    else:
        print 'Sorry,my name is hekang.'
except:
    print 'warning!'

print "Guess how old I am? You've got a three chance.(Tip:between [18,25] )"
for i in range(3):
    y = input()
    bingo = False
    if y == age:
        if i == 1:
            print "So crazy,you are right!"
        else:
            print "Bingo!"
        bingo = True
        break
    elif y > age:
        print "%d is too big!"%y
    else:
        print "%d is too small!"%y
    if i == 2 and bingo == False:
        print "You are weak! I'am %d." % age

