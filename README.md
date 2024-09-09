# Coding Assessment

Problem1 # Ordering The Word

   - The user is Used  to enter the number of strings (n) they wish to input.
   - The user then inputs n strings, one by one.

   - Each string is stripped of leading and trailing spaces, and any spaces within the string are removed using Strip method in python built-in function.
   - The string is converted to lowercase to ensure case insensitivity.
   - A dictionary is used to store the count of each unique string.

   - The script first prints the number of unique strings.
   - Then, it prints the frequency of each unique string, all in one line.


Problem2: Validate The Credit Card Number

   - The user is used to enter the number of credit card numbers (N) they wish to validate.
   - The user then inputs N credit card numbers, one by one.

   The script validates each card number based on the following rules:
   -  The card number must start with a 4 or 5 or 6.
   - The card number can contain hyphens (-), but:
       - There should not be more than 3 hyphens.
       - If hyphens are present, they must separate the card number into groups of 4 digits.
   -  The total length of the card number  must be exactly 16 digits.
   -  The card number must consist only of digits 0-9 after removing any hyphens.
   -  The card number should not have 4 or more consecutive repeated digits.

   - For each card number, the script prints "Valid" if the number passes all the above cases are passed.
   - It prints "Invalid" if any of the above rules are not passed.
