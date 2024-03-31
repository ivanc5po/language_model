from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
wb = webdriver.Chrome()

for i in range(23376, 100000):
    try:
        print(f"Step {i}\n")
        wb.get(f"https://writing.stackexchange.com/questions/{i}")
        time.sleep(2)
        open("train_data.txt", "a").write("question: "+wb.find_element(By.CLASS_NAME, 'question-hyperlink').text+"\n"+("\n".join(wb.find_element(By.ID, 'question').text.split("\n")[2:])).split("\nShare\n")[0]+"\nanswer: "+wb.find_element(By.CLASS_NAME, 'answercell').text.split("\nShare\n")[0]+"\n\n")
    except:
        pass
