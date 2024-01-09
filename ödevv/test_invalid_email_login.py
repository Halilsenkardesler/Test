from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_email_login():
    driver = webdriver.Chrome()
    driver.get("https://tobeto.com/giris")

    # Geçersiz e-posta ve şifre gir
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")

    email_input.send_keys("abc@tobete.com")
    password_input.send_keys("798456")

    # Giriş yap butonuna tıkla
    button = driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")
    button.click()

    # Uyarıyı kontrol et
    try:
        warning_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "popup"))
        ).text

        expected_result = "Geçersiz e-posta veya şifre"
        assert expected_result in warning_message, "Beklenen uyarı mesajı görüntülenmedi!"
        print("Geçersiz e-posta ile başarısız giriş testi başarılı!")
    except Exception as e:
        print(f"Uyarı mesajı bulunamadı veya bir hata oluştu: {e}")

    driver.quit()