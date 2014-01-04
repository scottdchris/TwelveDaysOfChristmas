"""
Twelve Days of Christmas by Christopher Scott
http://www.scottdchris.com/

Because it's Christmas 2013 and my true love is coding.
"""

import NumToWords

DaysOfChristmas = [
"Merry Christmas!",
"a partridge in a pear tree!",
"two turtle doves",
"three french hens",
"four colly birds",
"FIVE GOLDEN RINGS!!!!!",
"six geese-a-laying",
"seven swans-a-swimming",
"eight maids-a-milking",
"nine ladies dancing",
"ten lords-a-leaping",
"eleven pipers piping",
"twelve drummers drumming"
]

def song(day):
	if (day>1):
		DaysOfChristmas[1] = 'and ' + DaysOfChristmas[1]
	print "On the %s day of Christmas, my true love sent to me..." % (NumToWords.numToPlace(day))
	while (day>=0):
		print '%s' % (DaysOfChristmas[day])
		day-=1

def chooseADay(day): #User specifies day. Prints item of the day.
	print "On the %s day of Christmas, my true love sent to me: %s" % (NumToWords.numToPlace(day), DaysOfChristmas[day])

def main(day, function='both'):
	if (function == 'both'):
		song(day)
		chooseADay(day)
	elif (function == 'song' or function == 1):
		song(day)
	elif (function == 'chooseADay' or function == 2):
		chooseADay(userInput)
	else:
		print 'Invalid input. Running main(%s, both)' % (day)

main(input('Please enter a number: '))