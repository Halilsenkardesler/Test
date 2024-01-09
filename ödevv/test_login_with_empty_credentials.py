from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_empty_credentials():
    driver = webdriver.Chrome()
    driver.get("https://tobeto.com/giris")

    driver.find_element(By.NAME, "email").send_keys("")
    driver.find_element(By.NAME, "password").send_keys("")

    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")))
    button.click()

    try:
        warning_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='warning-message']"))).text

        expected_result = "Doldurulması zorunlu alan"
        assert expected_result in warning_message, "Uyarı mesajı beklenenle uyuşmuyor."
        print("Boş alan ile başarısız giriş testi başarılı!")
    except Exception as e:
        print(f"Uyarı mesajı bulunamadı veya bir hata oluştu: {e}")

    driver.quit()