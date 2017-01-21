

import random

'''
for i in range(0, 2):
		str    = "AAAA"
	url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, str)
	result = query(url)
	print result

	time.sleep(1)
'''





import urllib2
import time

def query(url):
	res = urllib2.urlopen(url)
	return res.read()

token = "GffGsL9mIYfbYFzyAAEH96Kyr5xC4pHT"

def getScore(str):
	url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, str)
	result = query(url)
	return int(result)




def genStr(fLen,len,str,patternDic,wordList):

	if len== fLen:
		wordList.append(str)

	else :

		if patternDic["A"] !=0:
			
			patternDic["A"] = patternDic["A"]-1
			genStr(fLen,len+1,str+"A",patternDic,wordList)
			patternDic["A"] = patternDic["A"]+1


		if patternDic["B"] !=0:
			
			patternDic["B"] = patternDic["B"]-1
			genStr(fLen,len+1,str+"B",patternDic,wordList)
			patternDic["B"] = patternDic["B"]+1

		if patternDic["C"] !=0:
			
			patternDic["C"] = patternDic["C"]-1
			genStr(fLen,len+1,str+"C",patternDic,wordList)
			patternDic["C"] = patternDic["C"]+1

		if patternDic["D"] !=0:
			
			patternDic["D"] = patternDic["D"]-1
			genStr(fLen,len+1,str+"D",patternDic,wordList)
			patternDic["D"] = patternDic["D"]+1








def patternGen(l,wordList):
	strl=l
	patternDic ={"A":strl,"B":strl,"C":strl,"D":strl}
	genStr(strl,0,"",patternDic,wordList)
	#print ansList



wordListLen1=[]
wordListLen2=[]
wordListLen3=[]
wordListLen4=[]
'''
A 4
AA 16
AAA 64
AAAA 256


'''


def genWordList():

		patternGen(1,wordListLen1)
		patternGen(2,wordListLen2)
		patternGen(3,wordListLen3)
		patternGen(4,wordListLen4)



def randFire():

	genWordList()

	print "init finish"
	bullet = ""
	used={}

	highestScore = 0

	goodChild=[]

	while True:

			


		if len(bullet) >= 47 and len(bullet)!=50:
			if len(bullet) == 47:
				w=wordListLen3[random.randint(0,len(wordListLen3)-1)]
				if used.get(w) !=True:
					used[w] =True
					bullet+=w

			if len(bullet) == 48:
				w=wordListLen2[random.randint(0,len(wordListLen2)-1)]
				if used.get(w) !=True:
					used[w] =True
					bullet+=w

			if len(bullet) == 49:
				w=wordListLen1[random.randint(0,len(wordListLen1)-1)]
				if used.get(w) !=True:
					used[w] =True
					bullet+=w
		


		elif len(bullet) == 50:
			highScore= getScore(bullet)
			time.sleep(1)
			print "FIRE"
			used={}

			if highScore > highestScore:
				highestScore= highScore
				highestScorePattern = bullet

				if highestScore > len(goodChild)*100:
					goodChild.append(highestScorePattern)

				#remove not good child
				


			if len(goodChild) >=2:
				head=random.randint(0,50)
				tail=random.randint(0,50)
				if head > tail:
					tmp=head
					head=tail
					tail=tmp
				bullet = goodChild[random.randint(0,len(goodChild)-1)][ head:tail]+goodChild[random.randint(0,len(goodChild)-1)][head:tail]
				
				bullet= bullet[0:tail]

				print "from good "+str(len(bullet))
			else:
				bullet=""

			print highScore

			

			

		else:

			w=wordListLen4[random.randint(0,len(wordListLen4)-1)]
			if used.get(w) !=True:
				used[w] =True
				bullet+=w
				




		
randFire()
	








