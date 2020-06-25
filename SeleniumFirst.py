from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(executable_path='E:/abhi/driver/chromedriver.exe')
# driver.get("https://www.google.com/")
# driver.close()

list1= [1,2,3,4]

# print(list(reversed(list1)))

for i in reversed(list1):
    print(i)

with open('File.txt', 'r') as r:
    r.read(5)
    print("1")