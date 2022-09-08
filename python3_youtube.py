#lets now import all the required libraries
from bs4 import BeautifulSoup
import requests
import selenium
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException   #Importing Exceptions
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
page= requests.get('https://www.youtube.com/')
from selenium import webdriver
driver=webdriver.Chrome("chromedriver.exe") #for visible browser

# from selenium.webdriver.chrome.options import Options


# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
# driver=webdriver.Chrome("chromedriver.exe",chrome_options=options)


data=[]
upvote=[]

wait = WebDriverWait(driver,10)
driver.get("https://www.youtube.com/watch?v=bSAlE_WgHxY")
# driver.get(input("input youtube url for comments scraping:-")) #input url link


for item in range(7): #increase the range for more comment 1 page= 10 (5 pages for 50-60 comments) 
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
    time.sleep(2)

for comment in wait.until(EC.presence_of_all_elements_located(("xpath", "//div[@class='style-scope ytd-expander']"))):
    data.append(comment.text)
    
    
likes=driver.find_elements("xpath","//span[@class='style-scope ytd-comment-action-buttons-renderer'][2]")
for i in likes:
    try:
        like=driver.find_elements("xpath","//span[@class='style-scope ytd-comment-action-buttons-renderer'][2]")
        upvote.append(i.text)
    except:
        upvote.append("-")
        
time.sleep(3)     
driver.close()   
data.pop(0)
data.pop()

print(len(data))
print(len(upvote))
time.sleep(2)
df1=pd.DataFrame({})
df1['Comments']=data
df1['Upvotes']=upvote
yt_comments4=df1 #change file name
# time.sleep(1)
# writing to Excel
datatoexcel1 = pd.ExcelWriter('yt_comments4.xlsx')
# write DataFrame to excel
yt_comments4.to_excel(datatoexcel1)
# save the excel
datatoexcel1.save()
print('DataFrame1 is written to Excel File successfully.')
