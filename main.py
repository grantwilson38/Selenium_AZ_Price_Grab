from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Funko-Pop-Train-Fighter-Exclusive/dp/B0B82T82SQ/ref=sr_1_2_sspa?crid=1TNUHO2ZO4CBI"
           "&keywords=darth+vader+bobblehead&qid=1699045816&sprefix=darth+vader+bob%2Caps%2C139&sr=8-2-spons&sp_csd"
           "=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.quit()
