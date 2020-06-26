from glassdoor_job_scraper import *
from firebase_post import *
from utils.utils import *
from models.jobs import *

administrationJobsList = []
businessJobsList = []
designJobsList = []
hardwareJobsList = []
hrJobsList = []
marketingJobsList = []
productJobsList = []
softwareJobsList = []

print ('***Fetching Jobs***')
for i in JOLT_JOB_CATEGORIES:
    if i == 'Administration':
        administrationJobsList = getJobs(i)
    if i == 'Business':
        businessJobsList = getJobs(i)
    if i== 'Design':
        designJobsList = getJobs(i)
    if i == 'Hardware':
        hardwareJobsList = getJobs(i)
    if i == 'HR':
        hrJobsList = getJobs(i)
    if i == 'Marketing':
        marketingJobsList = getJobs(i)
    if i == 'Product':
        productJobsList = getJobs(i)
    if i == 'Software':
        softwareJobsList = getJobs(i)

# print (administrationJobsList)
# print (businessJobsList)
# print (designJobsList)
# print (hardwareJobsList)
# print (hrJobsList)
# print (marketingJobsList)
# print (productJobsList)
# print (softwareJobsList)

print ('***Posting Administration Jobs***')
num = 0
for i in administrationJobsList:
    num += 1
    firebasePost = FirebasePost(desc=i.getCompanyName(), iconUrl=i.getLogoUrl(), location=i.getLocation(), salary=i.getSalary(), title=i.getJobTitle(), url=i.getJobUrl(), companyName=i.getCompanyName())
    firebasePost.administrationPost('adm'+("%03d" % (num,)))

print ('***Posting Business Jobs***')
num = 0
for i in businessJobsList:
    num += 1
    firebasePost = FirebasePost(desc=i.getCompanyName(), iconUrl=i.getLogoUrl(), location=i.getLocation(), salary=i.getSalary(), title=i.getJobTitle(), url=i.getJobUrl(), companyName=i.getCompanyName())
    firebasePost.businessPost('bus'+("%03d" % (num,)))

print ('***Posting Design Jobs***')
num = 0
for i in designJobsList:
    num += 1
    firebasePost = FirebasePost(desc=i.getCompanyName(), iconUrl=i.getLogoUrl(), location=i.getLocation(), salary=i.getSalary(), title=i.getJobTitle(), url=i.getJobUrl(), companyName=i.getCompanyName())
    firebasePost.designPost('des'+("%03d" % (num,)))

print ('***Posting Hardware Jobs***')
num = 0
for i in hardwareJobsList:
    num += 1
    firebasePost = FirebasePost(desc=i.getCompanyName(), iconUrl=i.getLogoUrl(), location=i.getLocation(), salary=i.getSalary(), title=i.getJobTitle(), url=i.getJobUrl(), companyName=i.getCompanyName())
    firebasePost.hardwarePost('har'+("%03d" % (num,)))

print ('***Posting HR Jobs***')
num = 0
for i in hrJobsList:
    num += 1
    firebasePost = FirebasePost(desc=i.getCompanyName(), iconUrl=i.getLogoUrl(), location=i.getLocation(), salary=i.getSalary(), title=i.getJobTitle(), url=i.getJobUrl(), companyName=i.getCompanyName())
    firebasePost.hrPost('hre'+("%03d" % (num,)))

print ('***Posting Marketing Jobs***')
num = 0
for i in marketingJobsList:
    num += 1
    firebasePost = FirebasePost(desc=i.getCompanyName(), iconUrl=i.getLogoUrl(), location=i.getLocation(), salary=i.getSalary(), title=i.getJobTitle(), url=i.getJobUrl(), companyName=i.getCompanyName())
    firebasePost.marketingPost('mar'+("%03d" % (num,)))

print ('***Posting Product Jobs***')
num = 0
for i in productJobsList:
    num += 1
    firebasePost = FirebasePost(desc=i.getCompanyName(), iconUrl=i.getLogoUrl(), location=i.getLocation(), salary=i.getSalary(), title=i.getJobTitle(), url=i.getJobUrl(), companyName=i.getCompanyName())
    firebasePost.productPost('pro'+("%03d" % (num,)))

print ('***Posting Software Jobs***')
num = 0
for i in softwareJobsList:
    num += 1
    firebasePost = FirebasePost(desc=i.getCompanyName(), iconUrl=i.getLogoUrl(), location=i.getLocation(), salary=i.getSalary(), title=i.getJobTitle(), url=i.getJobUrl(), companyName=i.getCompanyName())
    firebasePost.softwarePost('sof'+("%03d" % (num,)))


    


