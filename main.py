from bs4 import BeautifulSoup
import requests
# import time

# Define the URL for job search
urls = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

def findJobs():
    # Initialize job count
    count = 0
    
    # Fetch HTML content from the specified URL
    html_text = requests.get(urls).text
    soup = BeautifulSoup(html_text, 'lxml')

    # Extract job details using BeautifulSoup
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    # Open a file to save the job details
    with open('posts/saved.txt', 'w') as f:
        # Iterate through each job and extract relevant information
        for index, job in enumerate(jobs):
            location = job.find('ul', class_="top-jd-dtl clearfix").span.text
            skills = job.find('ul', class_="list-job-dtl clearfix").span.text
            company = job.find('h3', class_="joblist-comp-name").text
            link = job.find('header', class_="clearfix").h2.a['href']

            # Add your condition for job filtering here
            if True:  # You may want to replace this condition with your logic
                # Increment the job count
                count += 1
                
                # Write job details to the file
                f.write(f"Company: {company.strip().replace('(More Jobs)','')}\n")
                f.write(f"Location: {location.strip()}\n")
                f.write(f"Skills: {skills.strip()}\n")
                f.write(f"Link: {link}\n\n")

    # Return the total count of new jobs
    return count

# Display the URL being used for job search
print(f'Fetching Data from\n{urls}\n.')

# Call the function to find and save jobs, and get the count of new jobs
x = findJobs()

# Display the number of new jobs updated
print(f'{x} new jobs updated.')

# Add a time delay if needed (uncomment the line below)
# time.sleep(60)
