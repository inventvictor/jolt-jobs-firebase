import requests
import json
from bs4 import BeautifulSoup
from models.jobs import Jobs

def getJobs(keyword):
    headers = {	
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
        'referer': 'https://www.glassdoor.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
    }

    location_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.01',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
        'referer': 'https://www.glassdoor.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
    }

    data = {"term": "nigeria", "maxLocationsToReturn": 10}

    location_url = "https://www.glassdoor.co.in/findPopularLocationAjax.htm?"

    location_response = requests.post(location_url, headers=location_headers, data=data).json()
    place_id = location_response[0]['locationId']
    job_litsting_url = 'https://www.glassdoor.com/Job/jobs.htm'

    # Form data to get job results
    data = {
        'clickSource': 'searchBtn',
        'sc.keyword': keyword,
        'locT': 'C',
        #'locId': place_id,
        'jobType': ''
    }

    job_listings = []
    if place_id:
        response = requests.post(job_litsting_url, headers=headers, data=data)

    soup = BeautifulSoup(response.text, features='lxml')
    x = soup.find('ul',{'class': 'jlGrid hover'})
    lis = x.findAll('li')

    jobsList = []
    for i in range(len(lis)):
        try:
            jobs = Jobs(jobTitle=str(lis[i].attrs.get('data-normalize-job-title')).strip(), companyName=str(lis[i].div.next_sibling.a.div.text).strip(), location=str(lis[i].attrs.get('data-job-loc')).strip(), salary=''.join(lis[i].div.next_sibling.div.next_sibling.next_sibling.next_sibling.div.text).strip().replace(u'\xa0', ''), logoUrl=str(lis[i].div.span.img.attrs.get('data-original-2x')).strip(), jobUrl=str('www.glassdoor.com'+lis[i].div.a.attrs.get('href')).strip())
            jobsList.append(jobs)
        except:
            pass
        #print ('*******************************************')
    return jobsList

if __name__ == "__main__":
    print (getJobs('Design'))
