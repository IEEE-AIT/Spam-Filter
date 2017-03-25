import email.parser 
import os, sys, stat

def ExtractSub(filename):
	'''
	Extract Subject of the email

	'''
	fp = open(filename)
	msg = email.message_from_file(fp)
	payload = msg.get_payload()
	if type(payload) == type(list()) :
		payload = payload[0] # only use the first part of payload
	sub = msg.get('subject')
	sub = str(sub)
	if type(payload) != type('') :
		payload = str(payload)
	
	temp = sub + payload
	text = temp.split("--")[0]
	specialChar = [";","_",",",")","(","/","\\",'-',">","<",":",".","@","#","*","?","+","=","^",'"',"1","2","3","4","5","6","7","8","9","0"]

	for i in specialChar:
		if i in text:
			text = text.replace(i,'')

	#text = temp.replace(' ','').replace(')','').replace('(','').replace('/','').replace('-','').replace('>','').replace('.','').replace(':','')
	return text

def Looptext(data):
	'''
	Write a function to build a Datastructure through which when i loop i get a stream of words


	'''
	return None



def Extractlabels(filename):

	'''
	Write a function to extract labels from SPAMTrain in the Dataset and return them corresponding to the file name

	'''

	return None


#eg. :
ExtractSub("...\Spam-Filter\Dataset\CSDMC2010_SPAM\CSDMC2010_SPAM\TRAINING\TRAINING_00001.eml")

