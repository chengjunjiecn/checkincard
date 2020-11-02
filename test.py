from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
 
# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 驱动路径
path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
 
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)  # 参数添加
 
# 上网
url = 'https://health.tripaway.cn/'
browser.get(url)
time.sleep(3)
browser.find_element_by_name("staffName").send_keys("1")
browser.find_element_by_name("passwd").send_keys("1")
browser.find_element_by_class_name("sign").click()
time.sleep(3)
print(browser.get_cookies())

 
