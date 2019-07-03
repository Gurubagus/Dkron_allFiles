import paramiko	
import gitlab
import keyring
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
		ssh_client.connect(hostname='80.88.187.155',username='benemen',password=keyring.get_password("talend", "benemen"))
		stdin, stdout, stderr = ssh_client.exec_command("/usr/bin/bash -lc '/etl/cronjobs/monthly_push_jobs.sh' 1>/dev/null 2>/etl/logs/monthly_push_jobs.txt")
		out = stdout.read()
		print(out)
	except Exception as e:
		print('The following error has occurred during the XRM_Jobs dkron process')
		print(e.message)
	finally:
		if ssh_client:
			ssh_client.close()
		print('\nMonthly_Push_Jobs complete\n')

			
if __name__ == '__main__':
	try:
		with time_limit(600):
			main()
	except TimeoutException as e:
		print("monthly_push_jobs time has exceeded the safety limit.")
		emailer.raise_error("monthly_push_jobs ERROR","The monthly_push_jobsexecution time has exceeded the 10 minute safety limit")