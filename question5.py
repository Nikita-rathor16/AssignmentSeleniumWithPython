"""inport time pandas etc"""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
# Load the order details from the Excel sheet
#order_details = pd.read_excel("User credentials.xlsx", sheet_name="Order Details")
EXCEL_FILE = "Order.xlsx"
order_details = pd.read_excel(EXCEL_FILE, sheet_name="Order Details",engine="openpyxl")
# Start the WebDriver session
# Login with standard_user
#order_ss = []
# Iterate over each order in the order details
for index, order in order_details.iterrows():
    user = order["User Type"]
    product_name = order["Product Name"]
    quantity = order["Quantity"]
    expected_price = order["Total Price"]
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()
    username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    username_field.send_keys(user)
    password_field.send_keys("secret_sauce")
    login_button.click()
    # Add the product to the cart
    add_to_cart_button = driver.find_element(By.XPATH, f"//*[text()='{product_name}']/ancestor::div[@class='inventory_item_label']/following-sibling::div[@class='pricebar']/button")
    add_to_cart_button.click()
    time.sleep(1)  # Wait for the cart to update
    cart_item_count = driver.find_element(
            By.XPATH, '//*[@class="fa-layers-counter shopping_cart_badge"]'
        ).text
    if int(cart_item_count)>=1:
        click_cart_item = driver.find_element(By.XPATH, '//*[@class="fa-layers-counter shopping_cart_badge"]')
        click_cart_item.click()
    # Proceed to checkout
        checkout_button = driver.find_element(By.XPATH, '//*[@class="btn_action checkout_button"]')
        checkout_button.click()
    # Fill in the checkout information
        first_name_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        first_name_field.send_keys("Nikita")
        last_name_field.send_keys("Rathor")
        postal_code_field.send_keys("411057")
        continue_button = driver.find_element(By.CLASS_NAME, 'cart_button')
        continue_button.click()
    # Verify the total price
        total_price = driver.find_element(
            By.XPATH, '//*[@class="summary_subtotal_label"]'
        ).text
        price_index = total_price.index('$')
        total = total_price[price_index:]
        print(total_price)
        print("total",total)
        print("Expected Price",expected_price)
        if str(total) != str(expected_price).strip():
            order_details.at[index, "Order Status"] = "Failure"
            print("Failure")
            driver.quit()
            continue
        finish_button = driver.find_element(By.XPATH, '//*[@class="btn_action cart_button"]')
        finish_button.click()
        order_details.at[index, "Order Status"] = "Success"
        driver.quit()
        print("Success")
order_details.to_excel("Order.xlsx",sheet_name="Order Details",index=False,engine="openpyxl")
