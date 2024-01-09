from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login():
    driver = webdriver.Chrome()
    driver.get("https://tobeto.com/giris")

    # Geçerli e-posta ve şifre gir
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")

    email_input.send_keys("halil2310@hotmail.com")
    password_input.send_keys("Tweenrtrt10")

    # Giriş yap butonuna tıkla
    button = driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")
    button.click()

    # Giriş başarılı sayfasına yönlendirildiğini kontrol et
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='success-message']"))
        ).text

        expected_result = "Giriş başarılı"
        assert expected_result in success_message, "Başarılı giriş mesajı görüntülenmedi!"
        print("Başarılı kullanıcı girişi testi başarılı!")
    except Exception as e:
        print(f"Başarılı giriş mesajı bulunamadı veya bir hata oluştu: {e}")

    driver.quit()