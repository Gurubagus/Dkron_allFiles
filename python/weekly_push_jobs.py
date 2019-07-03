import paramiko	
import gitlab
import sys
sys.path.append("/home/benemenadmin/PyResources") # Directory for Python classes
import time_limit
from time_limit import *
import emailer

ssh_client= None

def main():
	try:
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname='80.88.187.155',username='benemen',password='HamR32XwLNd3!')
		stdin, stdout, stderr = ssh_client.exec_command("/usr/bin/bash -lc '/etl/cronjobs/weekly_push_jobs.sh' 1>/dev/null 2>/etl/logs/weekly_push_jobs.txt")
		out = stdout.read()
		print(out)
	except Exception as e:
		print('The following error has occurred during the XRM_Jobs dkron process')
		print(e.message)
	finally:
		if ssh_client:
			ssh_client.close()
		print('\nWeekly_Push_Jobs complete\n')

			
if __name__ == '__main__':
	try:
		with time_limit(600):
			main()
	except TimeoutException as e:
		print("weekly_push_jobs time has exceeded the safety limit.")
		emailer.raise_error("weekly_push_jobs ERROR","The weekly_push_jobs execution time has exceeded the 10 minute safety limit")