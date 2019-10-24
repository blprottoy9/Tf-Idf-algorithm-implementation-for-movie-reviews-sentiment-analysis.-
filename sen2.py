from string import punctuation
import emot
from math import *
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
import os

def training():
	file_content =[]
	dir = "/home/ash/Desktop/sentia/aclImdb/train/pos/"
	for file in os.listdir( dir ):
		if file.endswith( ".txt" ):
			fd=open(dir+file).read()
			#with open( os.path.join( dir, file ) ,"r") as fd:
			file_content.append( [fd,str(1)] )
	dir = "/home/ash/Desktop/sentia/aclImdb/train/neg/"
	for file in os.listdir( dir ):
		if file.endswith( ".txt" ):
			fd=open(dir+file).read()
			#with open( os.path.join( dir, file ) ,"r") as fd:
			file_content.append( [fd,str(0)] )
	unique=[]
	ps = PorterStemmer()
	#stock_word=open("/home/ash/Desktop/sentia/aclImdb/stop_word.txt").read().split('\n')
	filtered_sentence = []
	#fd=open('a.txt','w')
	tokenizer = RegexpTokenizer(r'\w+')		
	stop_words = set(stopwords.words('english'))
	print(stop_words)
	#print(stock_word)
	file_content2=[]
	#del stock_word[len(stock_word)-1]
	#print(stock_word)
	a=1
	ab={}
	for tweet in file_content:
		tweet1=tweet[0].lower()
		ab=emot.emoticons(tweet1)
		print(len(ab))
		if len(ab)==1:
			if ab[0]['flag']==True:
				#emotions=ab[0]['value']
				print(ab[0]['flag'])
		else:
			if ab['flag']==True:
				#emotions=ab[0]['value']
				print(ab['flag'])		
		tweet1=tweet1.replace('<br /><br />',' ')
		word_tokens = tokenizer.tokenize(tweet1)
		for w in word_tokens:
			if w not in stop_words:
				w1=ps.stem(w)
				filtered_sentence.append(w1)
		if len(ab)==1:
			if ab[0]['flag']==True: 
				for ii in ab[0]['value']:
					filtered_sentence.append(ii)
		else:
			if ab['flag']==True: 
				for ii in ab['value']:
						filtered_sentence.append(ii)
		unique=set(unique) | set(filtered_sentence)		 
		#for w in example_words:
		#print(filtered_sentence)
		print(a)
		filtered_sentence2=[]
		
		for ii in filtered_sentence:
			filtered_sentence2.append(ii)
		 

		file_content2.append([filtered_sentence2,tweet[1]])	
		filtered_sentence=[]
		a+=1
	print(file_content2)
	print(len(unique))
	i=0
	unique=list(unique)
	while i<len(unique):
		s=''
		try:
			float(unique[i])
			s=True
		except ValueError:
			s=False
			i+=1
		if s==True:
			del unique[i]
	count_idf=[]
	
	for j in range(len(unique)):
		count=0
		for i in file_content2:
			if unique[j] in i[0]:
				count+=1
		
		count_idf.append(log((len(file_content2)/count),10))
		
				
		
	fdd=open("/home/ash/Desktop/sentia/aclImdb/unique.txt",'w')
	for i in unique:
		fdd.write(i)
		fdd.write(',')
		print(i)
	dir = "/home/ash/Desktop/sentia/aclImdb/dtr2"			
	#fdd=open(dir+'/dt.txt','w')		 
	print(len(unique))
	dataset=[]
	ind=0
	for i in file_content2:
		fdd=open(dir+'/dt'+str(ind)+'.txt','w')
		dataset.append([])
		for j in range(len(unique)):
			if unique[j] in i[0]:
				
				count=(i[0].count(unique[j])/len(i[0]))*count_idf[j]
				print(count)
				print(unique[j])
				fdd.write(str(count))
				fdd.write(',')				
				'''fdd.write(unique[j])
				fdd.write(',')
				fdd.write(str(count))
				fdd.write(',')'''
				#dataset[ind].append([j,unique[j],count])
			else:
				fdd.write(str(0))
				fdd.write(',')			
		#dataset[ind].append(i[1])
		fdd.write(str(i[1]))
		fdd.write('\n')
		print(ind+1)
		ind+=1


def testing():
	file_content =[]
	dir = "/home/ash/Desktop/sentia/aclImdb/test/pos/"
	for file in os.listdir( dir ):
		if file.endswith( ".txt" ):
			fd=open(dir+file).read()
			#with open( os.path.join( dir, file ) ,"r") as fd:
			file_content.append( [fd,str(1)] )
	dir = "/home/ash/Desktop/sentia/aclImdb/test/neg/"
	for file in os.listdir( dir ):
		if file.endswith( ".txt" ):
			fd=open(dir+file).read()
			#with open( os.path.join( dir, file ) ,"r") as fd:
			file_content.append( [fd,str(0)] )
	unique=open("/home/ash/Desktop/sentia/aclImdb/unique.txt").read().split(',')
	del unique[len(unique)-1]
	ps = PorterStemmer()
	#stock_word=open("/home/ash/Desktop/sentia/aclImdb/stop_word.txt").read().split('\n')
	filtered_sentence = []
	#fd=open('a.txt','w')
	tokenizer = RegexpTokenizer(r'\w+')		
	stop_words = set(stopwords.words('english'))
	print(stop_words)
	#print(stock_word)
	file_content2=[]
	#del stock_word[len(stock_word)-1]
	#print(stock_word)
	a=1
	ab={}
	for tweet in file_content:
		tweet1=tweet[0].lower()
		ab=emot.emoticons(tweet1)
		print(len(ab))
		if len(ab)==1:
			if ab[0]['flag']==True:
				#emotions=ab[0]['value']
				print(ab[0]['flag'])
		else:
			if ab['flag']==True:
				#emotions=ab[0]['value']
				print(ab['flag'])		
		tweet1=tweet1.replace('<br /><br />',' ')
		word_tokens = tokenizer.tokenize(tweet1)
		for w in word_tokens:
			if w not in stop_words:
				w1=ps.stem(w)
				filtered_sentence.append(w1)
		if len(ab)==1:
			if ab[0]['flag']==True: 
				for ii in ab[0]['value']:
					filtered_sentence.append(ii)
		else:
			if ab['flag']==True: 
				for ii in ab['value']:
						filtered_sentence.append(ii)
		#unique=set(unique) | set(filtered_sentence)		 
		#for w in example_words:
		#print(filtered_sentence)
		print(a)
		filtered_sentence2=[]
		
		for ii in filtered_sentence:
			filtered_sentence2.append(ii)
		 

		file_content2.append([filtered_sentence2,tweet[1]])	
		filtered_sentence=[]
		a+=1
	print(file_content2)
	print(len(unique))
	count_idf=[]
	
	for j in range(len(unique)):
		count=0
		for i in file_content2:
			if unique[j] in i[0]:
				count+=1
		
		count_idf.append(log((len(file_content2)/count),10))
	dir = "/home/ash/Desktop/sentia/aclImdb/dtes2"			
	#fdd=open(dir+'/dt.txt','w')		 
	print(len(unique))
	dataset=[]
	ind=0
	for i in file_content2:
		fdd=open(dir+'/dtse'+str(ind)+'.txt','w')
		dataset.append([])
		for j in range(len(unique)):
			if unique[j] in i[0]:
				
				count=i[0].count(unique[j])/len(i[0])*count_idf[j]
				print(count)
				print(unique[j])
				fdd.write(str(count))
				fdd.write(',')				

				#dataset[ind].append([j,unique[j],count])
			else:
				fdd.write(str(0))
				fdd.write(',')			
		#dataset[ind].append(i[1])
		fdd.write(str(i[1]))
		fdd.write('\n')
		print(ind+1)
		ind+=1

def knn():
	dir = "/home/ash/Desktop/sentia/aclImdb/dtes2"	
	dir1="/home/ash/Desktop/sentia/aclImdb/dtr2"	
	unique=open("/home/ash/Desktop/sentia/aclImdb/unique.txt").read().split(',')
	del unique[len(unique)-1]
	i=0
	kn=int(input("k:"))
	eres=[]
	classes=[1,0]
	ores=[]
	while i<25000:
		j=0
		tes=open(dir+'/dtse'+str(i)+'.txt').read().split(',')
		#print(tes)
		print(i)
		ores.append(float(tes[len(tes)-1]))
		des=[]
		list_of_ct=[]
		count_cls=[0,0]
		while j<25000:
			tr=open(dir1+'/dt'+str(j)+'.txt').read().split(',')
			k=0
			d=0
			print("j:",j)
			while k<len(unique):
				d+=pow(float(tes[k])-float(tr[k]),2)
				print("d:",d)
				print("k:",k)
				k+=1
			des.append(sqrt(d))
			list_of_ct.append(float(tr[len(tr)-1]))
			j+=1
		for jjj in range(len(des)-1):
			for kkk in range(jjj+1,len(des)):
				if(des[jjj]>des[kkk]):
					des[jjj],des[kkk]=des[kkk],des[jjj]
					list_of_ct[jjj],list_of_ct[kkk]=list_of_ct[kkk],list_of_ct[jjj]
		#for jjj in range(kn):
		count_cls[0]=list_of_ct[0:kn].count(classes[0])
		count_cls[1]=list_of_ct[0:kn].count(classes[1])
		max1=max(count_cls)
		ind=count_cls.index(max1)
		eres.append(classes[ind])
		i+=1
	#print(ores)
training()
testing()
knn()

