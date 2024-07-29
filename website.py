from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def log_status(step, status):
    print(f"{step}: {'PASSED' if status else 'FAILED'}")

# Initialize the WebDriver
driver = webdriver.Chrome()  

try:
    # Navigate to the login page
    driver.get("https://app.respond.io/user/login")

    # Find the email address field and enter your email
    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "field_2"))
        )
        email_field.send_keys("hamza1@yopmail.com") 
        log_status("Email field found and email entered", True)
    except TimeoutException:
        log_status("Email field found and email entered", False)

    # Find the password field and enter your password
    try:
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "field_3"))
        )
        password_field.send_keys("Click123@")  
        log_status("Password field found and password entered", True)
    except TimeoutException:
        log_status("Password field found and password entered", False)

    # Find the sign-in button and click it
    try:
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/form/div[4]/button"))
        )
        sign_in_button.click()
        log_status("Sign-in button clicked", True)
    except TimeoutException:
        log_status("Sign-in button clicked", False)

    # Wait for the login process to complete
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("https://app.respond.io/space/240114/dashboard") 
        )
        log_status("Login successful", True)
    except TimeoutException:
        log_status("Login successful", False)

    # Navigate to the settings section
    try:
        settings_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/nav/div/div[1]/a[7]/div[2]/div[1]"))
        )
        settings_icon.click()

        # Wait for the settings page to load
        WebDriverWait(driver, 10).until(
            EC.url_contains("https://app.respond.io/user/user-profile") 
        )
        log_status("Settings section clicked and loaded", True)
    except TimeoutException:
        log_status("Settings section clicked and loaded", False)

    # Navigate to the workspace section
    try:
        workspace_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/main/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div[3]/a[4]/div[1]"))
        )
        workspace_icon.click()

        # Wait for the workspace page to load
        WebDriverWait(driver, 10).until(
            EC.url_contains("https://app.respond.io/organization/238152/spaces") 
        )
        log_status("Workspace section clicked and loaded", True)
    except TimeoutException:
        log_status("Workspace section clicked and loaded", False)

    # Add a new workspace
    try:
        add_workspace = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div[1]/div/div/button"))
        )
        add_workspace.click()
        log_status("Add Workspace button clicked", True)
    except TimeoutException:
        log_status("Add Workspace button clicked", False)

    # Wait for the workspace name input field to be visible
    try:
        workspace_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "field_14"))
        )
        workspace_name_input.send_keys("Hamza Workspace")
        log_status("Workspace name entered", True)
    except TimeoutException:
        log_status("Workspace name entered", False)

    # Wait for the "Next" button to be clickable
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/form/div/div[3]/div/div[2]/div/button[2]"))
        )
        next_button.click()
        log_status("Next button clicked", True)
    except TimeoutException:
        log_status("Next button clicked", False)

    # Wait for the error message to appear and print it
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/section/ol/li/div"))
        )
        print("Error message found: ", error_message.text)
        log_status("Error message found and displayed", True)
    except TimeoutException:
        log_status("Error message found and displayed", False)

finally:
    # Close the browser
    driver.quit()
