import requests
from bs4 import BeautifulSoup
import pandas as pd


'''Choose page to extract data from --> the soup 'html.parser' soup var '''
def extract(page):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}  

  url = f'https://uk.indeed.com/jobs?q=Python%20Developer&l=chester&start={page}'
  r = requests.get(url, headers)
  soup = BeautifulSoup(r.content, 'html.parser')
  return soup

'''store as variable to give to next function, transform
  classes and types for each var found in inspect element HTML extract below
'''

def transform(soup):
  divs = soup.find_all('div', class_ = 'job_seen_beacon')
  for item in divs:
    title = item.find('h2').text.strip()
    location = item.find('div', class_ ='companyLocation').text.strip()
    company = item.find('span', class_ = 'companyName').text.strip()
    try:
      salary = item.find('aria-label', class_ ='salary-snippet').text.strip()
    except:
      salary = ''
    summary = item.find('div', class_ = 'job-snippet').text.strip().replace('\n', '')

    job = {
      'title': title,
      'location': location,
      'company': company,
      'salary': salary,
      'summary': summary,
    }
    joblist.append(job)
  return

'''creates blank list then appends it'''

joblist = []

'''range - 0 - 40 in intervals of ten'''

for i in range(0, 40, 10):
  print(f'Getting Page... {i}')
  c = extract(0)
  transform(c)

'''create df --> pandas dataframe'''

df = pd.DataFrame(joblist)

print(df)

df.to_csv('jobs.csv')






'''print(joblist)
  print (len(joblist))
'''

'''print(transform(c))'''


'''
html from inspect element

<div class="job_seen_beacon"><table class="jobCard_mainContent" cellpadding="0" cellspacing="0" role="presentation"><tbody><tr><td class="resultContent"><div class="heading4 color-text-primary singleLineTitle tapItem-gutter"><h2 class="jobTitle jobTitle-newJob"><div class="new topLeft holisticNewBlue desktop"><span class="label">new</span></div><span title="Junior Web Developer">Junior Web Developer</span></h2></div><div class="heading6 company_location tapItem-gutter"><pre><span class="companyName">Yellow Marketing</span><div class="companyLocation">Liverpool<!-- --> <!-- -->L19 2RF</div></pre></div><div class="heading6 tapItem-gutter metadataContainer"><div class="metadata salary-snippet-container"><div aria-label="£16,000 to £20,000 a year" class="salary-snippet"><span>£16,000 - £20,000 a year</span></div></div></div><div class="heading6 error-text tapItem-gutter"></div></td></tr></tbody></table><table class="jobCardShelfContainer" role="presentation"><tbody><tr class="jobCardShelf"><td class="shelfItem indeedApply"><span class="iaIcon"></span><span class="ialbl iaTextBlack">Easily apply to this job</span></td></tr><tr class="underShelfFooter"><td><div class="heading6 tapItem-gutter result-footer"><div class="job-snippet"><ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;"> 
 <li style="margin-bottom:0px;">The role involves working with account managers on various PPC campaigns and Web projects, as well as:</li>
 <li>Assisting in creation of new website projects.</li>
</ul></div><span class="date"><span class="visually-hidden">Posted</span>2 days ago</span></div></td></tr></tbody></table><div aria-live="polite"></div></div>'''