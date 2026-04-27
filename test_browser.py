from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os

def test_standard_browser():
    print("Standart brauzer ochishga harakat qilinmoqda...")
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    
    try:
        # Biz avvalroq yuklab olgan chromedriver.exe dan foydalanamiz
        service = Service(executable_path='chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=options)
        
        print("Brauzer ochildi!")
        driver.get('https://www.google.com')
        print("Google sahifasiga kirdi!")
        
        time.sleep(10)
        driver.quit()
        print("Test muvaffaqiyatli yakunlandi.")
        
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == '__main__':
    test_standard_browser()
