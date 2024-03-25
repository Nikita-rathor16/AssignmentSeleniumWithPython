Using Selenium with Python please complete the following assignments.
--------------------------------------------------------------------------

1. Retrieve all the Users and password related information and store it in Sheet named "User credentials" in a excel file.
User ID, User Name, Password

2. Try login with all the Users provided on the website link https://www.saucedemo.com/v1/ and record any error messages 
displayed for a specific user. write this information to another sheet named "Login" in the same excel file as above 
in the following format.
User ID, Login Message
 
3. Login using the "standard_user" and retrieve all the product related information for every listed product. 
Write this information into a separate sheet named "Product Details" in the same excel file.
Product ID, Product Name, Description, Price

4. Manually create another sheet called "Order Details" in the same excel file and add Orders for 
the "standard_user" and "problem_user". Decide on the Columns on your own and try to represent this data. 
(review before you move to next one)

5. Using the above "Order Details" sheet try the place all the orders on the website one by one. Update a new column in the 
"Order Details" sheet called "Order Status" marking it as "Success/Failure".
Success criteria should be as follows.
1. The correct number of items should be added to the Cart.
2. The total amount at the end should be correct.
3. Success message should be displayed for every order placed.
4. No Items should be left over in the cart.
