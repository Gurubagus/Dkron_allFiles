import os 
import sys
from sys import argv
import requests
import keyring
from requests.auth import HTTPBasicAuth

#server_pass = keyring.get_password('dkron','BI_Labs')
server_pass = 'yd%VNP%0&S^S7Do!8dsHnurq3^!ra[4B'
def delete(name):

	#INSERT YOUR DKRON URL HERE WITH SYNTAX: 'http(s)://<localhost:port>/v1/jobs'
	url = 'http://127.0.0.1:8080/v1/jobs/'+name

	#INSERT ANY NECESSARY HEADERS HERE: e.g. authentications, application types, etc
	headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}

	#THIS CREATES THE API REQUEST, PLEASE DO NOT EDIT UNLESS KNOWLEDGABLE:
	out = requests.delete(url, data=name, auth=HTTPBasicAuth('BI_Labs', server_pass))
	decode(out,name)

def decode(out,name):
	
	if str(out) == "<Response [200]>":
		print ("%s deleted successfully") % name
	elif str(out) == "<Response [400]>":
		print ("Error: %s has a syntax error") % name
	elif str(out) == "<Response [401]>":
		print ("Error: You do not have the autorization to complete this action.") % name
	elif str(out) == "<Response [422]>":
		print ("Error: %s is unprocessable. Most likely one of the variables doesn't meet Dkron's criteria.") % name
	else:
		print("Unknown Error: %s") % out
		
def main(name):
	response = delete(name)
		
if __name__=="__main__":
	name = argv[1] # job name from command line argument (e.g. python JOBDELETE_dkron.py 1minute_jobs.json)
	main(name)
