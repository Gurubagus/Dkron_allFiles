"""
Script for auto updating gitlab.beneservices.com's repository for:

- BAP@80.88.187.129 /projects/BAP -> BAP.git
- Talend Server@80.88.187.155: /etl/talend_jobs -> talend_jobs.git
- Talend Server@80.88.187.155: /etl/development/BENEETL -> etl_development_BENEETL.git
- gpadmin@80.88.187.33: /etl/pg_dump/BeneDW.dmp -> benedw_schemas.git
- BENEG1\\Qlik_Admin@10.252.35.240: \inetpub\wwwroot\BeneReports -> benereports.git
- ESB@80.88.187.171 D:/TalendOS_ESB/Studio/workspace/BENE_ESB -> BENE_ESB.git
"""

import os
import paramiko
import sys
sys.path.insert(0,"/home/benemenadmin/dkron_jobs/python/agu")
import git_BAP
import sshgit_talend_jobs
import sshgit_etl_development
import sshgit_etl_BeneDW
import sshgit_QlikSense_BeneReports_development
import sshgit_QlikSense_BeneReports_production
import sshgit_esb_beneesb
import git_dkron
import sys
sys.path.append("/home/benemenadmin/PyResources") # Directory for Python classes
import time_limit
from time_limit import *
import emailer

def main():
	
	git_BAP.main()
	git_dkron.main()
	sshgit_talend_jobs.main()
	sshgit_etl_development.main()
	sshgit_etl_BeneDW.main()
	sshgit_QlikSense_BeneReports_development.main()
	sshgit_QlikSense_BeneReports_production.main()
	sshgit_esb_beneesb.main()
		
if __name__ == '__main__':
	try:
		with time_limit(300):
			main()
	except TimeoutException as e:
		print("Auto Gitlab Uploader time has exceeded the safety limit.")
		emailer.raise_error("Auto Gitlab Uploader ERROR","Auto Gitlab Uploader execution time has exceeded the 5 minute safety limit")