def creditCardNumber(cardNumber):

    if cardNumber[0] not in "456":   
        return "Invalid"             
        
    count = cardNumber.count("-")     
    if count > 3:
        return "Invalid"               
        
    if "-" in cardNumber:              
        number = cardNumber.split("-")  # Split the card number into groups of digits, groups are done based on hyphens
        for i in number:
            if len(i) != 4:              # if length of each group is not equal to 4, it returns invalid
                return "Invalid"
        cardNumber = "".join(number)     # join is used  to join the splitted number
        
    if len(cardNumber) != 16:           
        return "Invalid"
        
    if not cardNumber.isdigit():         #It ensures that all the cardnumbers are digits or not
        return "Invalid"

    for i in range(13):
        if cardNumber[i] == cardNumber[i+1] == cardNumber[i+2] == cardNumber[i+3]:
            return "Invalid"       
    
   
    return "Valid"                        # If above all the cases pass, the card number is valid


N = int(input())      
for n in range(N):
   
    cardNumber =input().strip()           # Get each card number, and strip is used to remove leading/trailing spaces
    print(creditCardNumber(cardNumber))