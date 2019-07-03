import os
import gitlab
	
def gitupload():
	
	os.system("git add -A")
	os.system('git commit -m "auto upload"')
	os.system('git push origin master')
	
def main():

	try:
		print('\n*************DKRON backup: Starting*************\n')
		cwd = os.getcwd()
		os.chdir('/home/benemenadmin/dkron_jobs')
		gl = gitlab.Gitlab.from_config('BAP',['/etc/python-gitlab.cfg'])
		x = gitupload()
		
		os.chdir(cwd)
	except Exception as e:
		print('The following error has occurred during the DKRON backup process')
		print(e.message)
	
	finally:
		print('\n*************DKRON backup: Complete*************\n')
	
if __name__ == '__main__':
	
	main()
	
	