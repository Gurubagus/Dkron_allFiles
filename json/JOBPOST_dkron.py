import os 
import sys
from sys import argv
import requests
import keyring
from requests.auth import HTTPBasicAuth

#server_pass = keyring.get_password('dkron','BI_Labs')
server_pass = 'yd%VNP%0&S^S7Do!8dsHnurq3^!ra[4B'

def upload(JOB):

	#INSERT YOUR DKRON URL HERE WITH SYNTAX: 'http(s)://<localhost:port>/v1/jobs'
	url = 'http://127.0.0.1:8080/v1/jobs'

	#INSERT ANY NECESSARY HEADERS HERE: e.g. authentications, application types, etc
	headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}

	#INSERT JOB JSON FILE NAME IN THE BRACKETS:
	job_to_upload = open(JOB, 'rb').read()

	#THIS CREATES THE API REQUEST, PLEASE DO NOT EDIT UNLESS KNOWLEDGABLE:
	out = requests.post(url, data=job_to_upload, headers=headers, auth=HTTPBasicAuth('BI_Labs', server_pass))
	decode(out,JOB)

def decode(out,JOB):
	
	if str(out) == "<Response [201]>":
		print ("%s uploaded successfully") % JOB
	elif str(out) == "<Response [400]>":
		print ("Error: %s has a syntax error") % JOB
	elif str(out) == "<Response [401]>":
		print ("Error: You do not have the autorization to complete this action.") % JOB
	elif str(out) == "<Response [422]>":
		print ("Error: %s is unprocessable. Most likely one of the variables doesn't meet Dkron's criteria.") % JOB
	else:
		print("Unknown Error: " + out)
		
def main(JOB):
	response = upload(JOB)
		
if __name__=="__main__":
	JOB = argv[1] # job name from command line argument (e.g. python JOBPOST_dkron.py 1minute_jobs.json)
	main(JOB)
