from selenium import webdriver
import time

from selenium.webdriver.common.by import By
import urllib.request

animalList = dict()
animalList["고양이"] = "cat_image"
animalList["강아지"] = "dog_image"
animalList["돼지"] = "pig_image"
animalList["말"] = "horse_image"
animalList["쥐"] = "mouse_image"
animalList["호랑이"] = "tiger_image"
animalList["사자"] = "lion_image"

driver = webdriver.Chrome()
number = 15
for ani in animalList:
    driver.get(f'https://www.google.com/search?q={ani}&tbm=isch&tbs=il:ol&hl=ko&sa=X&ved=0CAAQ1vwEahcKEwiwtKrW2tGDAxUAAAAAHQAAAAAQAg&biw=1878&bih=979')


    firstImage = driver.find_element(By.CSS_SELECTOR, '#islrg > div.islrc > div:nth-child(2) > a.FRuiCf.islib.nfEiy > div.fR600b.islir > img')
    firstImage.click()
    for i in range(number):
        try:
            time.sleep(3)
            image = driver.find_element(By.CSS_SELECTOR, '#Sva75c > div.A8mJGd.NDuZHe.CMiV2d.OGftbe-N7Eqid-H9tDt > div.dFMRD > div.AQyBn > div.tvh9oe.BIB1wf.hVa2Fd > c-wiz > div > div > div > div > div.v6bUne > div.p7sI2.PUxBg > a > img.sFlh5c.pT0Scc.iPVvYb')
            imageSrc = image.get_attribute('src')
            urllib.request.urlretrieve(imageSrc, f'{animalList[ani]}{str(i+1).zfill(2)}.jpg')

            # time.sleep(10)
        except Exception as e:
            print(e)
        finally:
            nextButton = driver.find_element(By.CSS_SELECTOR, '#Sva75c > div.A8mJGd.NDuZHe.CMiV2d.OGftbe-N7Eqid-H9tDt > div.dFMRD > div.AQyBn > div.tvh9oe.BIB1wf.hVa2Fd > c-wiz > div > div > div > div > div.s9n5ef.dZ5aUe > div > div.vbLSne > button:nth-child(2)')
            nextButton.click()







         
        

driver.quit()







#islrg > div.islrc > div:nth-child(2) > a.FRuiCf.islib.nfEiy > div.fR600b.islir > img