import os
import gitlab
	
def gitupload():
	
	os.system("git add -A")
	os.system('git commit -m "auto upload"')
	os.system('git push origin master')
	
def main():

	try:
		print('\n*************BAP backup: Starting*************\n')
		cwd = os.getcwd()
		os.chdir('/home/benemenadmin/projects/BAP')
		gl = gitlab.Gitlab.from_config('BAP',['/etc/python-gitlab.cfg'])
		x = gitupload()
		
		os.chdir(cwd)
		print('\n*************BAP backup: Complete*************\n')
	except Exception as e:
		print('The following error has occurred during the BAP backup process')
		print(e.message)
	
if __name__ == '__main__':
	
	main()
	
	