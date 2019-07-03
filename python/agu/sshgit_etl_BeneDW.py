# FUTURE REFERENCE: set remote url to https://username(w/o "@.com"):password@gitlab.beneservices.com/BI_Labs/<dir>.git

import paramiko	
import gitlab
import keyring

ssh_client= None

def main():
	print('\n*************BeneDW pg_dump backup: Starting*************\n')
	try:
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname='80.88.187.33',username='gpadmin',password=keyring.get_password("etl","gpadmin"))
		ssh_client.exec_command('pg_dump -s BeneDW > /etl/pg_dump/BeneDW.dmp')
		stdin, stdout, stderr = ssh_client.exec_command('pg_dump -s BeneDW > /etl/pg_dump/BeneDW.dmp; cd /etl/pg_dump; git add .; git commit -m "auto-upload"; git push origin master')
		out = stdout.read()
		print(out)

	except Exception as e:
		print('The following error has occurred during the pg_dump backup process')
		print(e.message)
		
	finally:
		if ssh_client:
			ssh_client.close()
		print('\n*************BeneDW pg_dump backup: Complete*************\n')
			
if __name__ == '__main__':
	main()