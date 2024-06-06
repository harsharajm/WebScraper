from bs4 import BeautifulSoup
import requests

urls = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

#Function to filter jobs
def filters(location, skills):
    #Replace with your preferred location and skills
    preferred_location = "Hyderabad"
    skill_set = "Python"
    if (preferred_location in location or preferred_location.lower() in location) and (skill_set in skills or skill_set.lower() in skills):
        return True
    return False

def findJobs():

    count = 0

    html_text = requests.get(urls).text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    with open('saved.txt', 'w') as f:
        for index, job in enumerate(jobs):
            location = job.find('ul', class_="top-jd-dtl clearfix").span.text
            skills = job.find('ul', class_="list-job-dtl clearfix").span.text
            company = job.find('h3', class_="joblist-comp-name").text
            link = job.find('header', class_="clearfix").h2.a['href']

            # Filtering Jobs
            if filters(location,skills):
                count += 1
                
                # Writing job details into text file
                f.write(f"Company: {company.strip().replace('(More Jobs)','')}\n")
                f.write(f"Location: {location.strip()}\n")
                f.write(f"Skills: {skills.strip()}\n")
                f.write(f"Link: {link}\n\n")
    #Returning Count so that we can know the number of Jobs found
    return count

# Displaying url so we know the Source and that code is runnning.
print(f'Fetching Data from : {urls}\n.')
x = findJobs()
print(f'{x} new jobs updated.')
