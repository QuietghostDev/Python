import random

def main():
	f = open('5-letter words.txt','r')
	r = f.readlines()
	for i in range(3):
		num = random.randint(0,len(r))
		word = r[num]
		print word
	raw_input()
main()