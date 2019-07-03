# FUTURE REFERENCE: set remote url to https://username(w/o "@.com"):password@gitlab.beneservices.com/BI_Labs/<dir>.git

import paramiko	
import gitlab
import keyring

ssh_client= None

def main():
	print('\n*************ETL Development backup: Starting*************\n')
	try:
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname='80.88.187.155',username='benemen',password=keyring.get_password("talend", "benemen"))
		stdin, stdout, stderr = ssh_client.exec_command('cd /etl/development/BENEETL; export LD_LIBRARY_PATH=/lib64/:$LD_LIBRARY_PATH; git add -A ; git commit -m "auto-upload"; git push origin master')
		out = stdout.read()
		print(out)
	except Exception as e:
		print('The following error has occurred during the ETL Development backup process')
		print(e.message)
	finally:
		if ssh_client:
			ssh_client.close()
		print('\n*************ETL Development backup: Complete*************\n')

			
if __name__ == '__main__':
	main()