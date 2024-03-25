from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to place an order and update the "Order Status" column
def place_order(order_id, user_type, product_name, quantity, total_price):
    # Start the web browser (make sure you have the appropriate browser driver installed)
    driver = webdriver.Chrome()

    # Open the Swag Labs website
    driver.get("https://www.saucedemo.com/v1/")

    # Log in using the provided username and password
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys(user_type)
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Check if login was successful
    if "inventory" in driver.current_url:
        # Search for the product and navigate to its product page
        search_box = driver.find_element(By.CLASS_NAME, "inventory_search")
        search_box.send_keys(product_name)

        # Add the specified quantity of the product to the cart
        add_to_cart_button = driver.find_element(By.XPATH, "//div[text()='{}']/following-sibling::div/button".format(product_name))
        for _ in range(quantity):
            add_to_cart_button.click()

        # Verify the number of items in the cart
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        cart_items_count = int(cart_badge.text)
        if cart_items_count == quantity:
            # Proceed to the cart page
            cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            cart_icon.click()

            # Verify the total amount in the cart
            cart_total = driver.find_element(By.CLASS_NAME, "summary_total_label").text.strip()
            if cart_total == "Total: {}".format(total_price):
                # Proceed to checkout
                checkout_button = driver.find_element(By.CLASS_NAME, "checkout_button")
                checkout_button.click()

                # Place the order and check for success message
                finish_button = driver.find_element(By.CLASS_NAME, "cart_button")
                finish_button.click()

                success_message = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
                )
                if success_message.text == "THANK YOU FOR YOUR ORDER":
                    # Verify there are no items left in the cart
                    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
                    cart_items_count = int(cart_badge.text)
                    if cart_items_count == 0:
                        # Update the "Order Status" column in the "Order Details" sheet as "Success"
                        update_order_status(order_id, "Success")
                    else:
                        # Update the "Order Status" column in the "Order Details" sheet as "Failure"
                        update_order_status(order_id, "Failure")
                else:
                    # Update the "Order Status" column in the "Order Details" sheet as "Failure"
                    update_order_status(order_id, "Failure")
            else:
                # Update the "Order Status" column in the "Order Details" sheet as "Failure"
                update_order_status(order_id, "Failure")
        else:
            # Update the "Order Status" column in the "Order Details" sheet as "Failure"
            update_order_status(order_id, "Failure")

    # Close the web browser
    driver.quit()

# Function to update the "Order Status" column in the "Order Details" sheet
def update_order_status(order_id, status):
    # Code to update the "Order Status" column in the spreadsheet
    # You can use libraries like openpyxl or pandas to update the spreadsheet

# Main function to process each order
    def process_orders():
    # Read the "Order Details" sheet and iterate over each order
         order_details = [
        {"order_id": 1, "user_type": "standard_user", "product_name": "sauce Labs Backpack", "quantity": 1, "total_price": "$29.99"},
        {"order_id": 2, "user_type": "standard_user", "product_name": "Sauce Labs Bolt T-Shirt", "quantity": 1, "total_price": "$15.99"},
        {"order_id": 3, "user_type": "problem_user", "product_name": "Sauce Labs Bike Light", "quantity": 1, "total_price": "$9.99"}
    ]