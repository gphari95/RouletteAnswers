
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tabulate import tabulate

x=input("Enter the Roulette bet value: ")

def execute():
    if x.isnumeric():
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
        driver.get("https://csgoempire.com/roulette")
        print(driver.title)

        driver.maximize_window()
        driver.implicitly_wait(10)

    # Fetch Bet amount from user
        driver.find_element(By.XPATH,"//input[@placeholder='Enter bet amount...']").send_keys(x)
    #increments bet by +0.01
        driver.find_element(By.XPATH,"//button[normalize-space()='+ 0.01']").click()

        num=driver.find_element(By.XPATH, "//input[@placeholder='Enter bet amount...']").text
    #increments bet by +0.1
        driver.find_element(By.XPATH,"//button[normalize-space()='+ 0.1']").click()
    #increments bet by +1
        driver.find_element(By.XPATH, "//button[normalize-space()='+ 1']").click()
    #increments bet by +10
        driver.find_element(By.XPATH, "//button[normalize-space()='+ 10']").click()
    #increments bet by +100
        driver.find_element(By.XPATH, "//button[normalize-space()='+ 100']").click()
    #decrements bet by 1/2
        driver.find_element(By.XPATH, "//button[normalize-space()='1/ 2']").click()
    #multiplies bet by 2
        driver.find_element(By.XPATH, "//button[normalize-space()='x 2']").click()
    #To get screenshot of webpage and store in default path
        driver.get_screenshot_as_file("screenshot.png")

    # FetchdailyRoulettetable
        message1 = driver.find_element(By.XPATH, value="//table[@class='base-table rounded-lg alternate-row-colors']").text
        words = message1.split()
        print(tabulate([words], headers=['***']))
        print()
        print("The top award of 3500 coins goes to the player->", words[5].upper(), "with a wager of", words[6], "coins")
        print("The least wagered player in the 10th spot of the list is->", words[43].upper(), "with a wager of", words[44],"coins")
        driver.find_element(By.XPATH, "//p[@class='size-medium underline']").click()
        driver.implicitly_wait(3)
        gamerules = driver.find_element(By.XPATH,"//body/div[@id='app']/div[@id='app']/div/div/div[@role='dialog']/div/div/div/div[1]").text
        print(gamerules)
        message2 = driver.find_element(By.CSS_SELECTOR, ".size-medium.font-bold.ml-auto").text
        print("Hurry the Daily Roulette Race", message2)
        driver.close()

    else:
        print("Enter a valid bet value")
execute()




