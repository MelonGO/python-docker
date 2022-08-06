
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.baidu.com")
    print(driver.current_url)
    driver.close()
 
if __name__ == '__main__':
    main()