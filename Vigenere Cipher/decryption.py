#take input from user
c = input("Enter Cipher Text: ").upper()
k= input ("Enter Key: ").upper()
#checking the length of key, so that key could be repeated if it is shorter
if len (k)< len(c): 
    k=(k*(len(c)//len(k) + 1))[:len(c)]
#initialize plain text as empty string
    p=""
#loop through each char in cYUETUFTM
for i in range(len(c)):
    #convert ciphertext to number
    c_val=ord(c[i])-ord('A')
    #convert key to number
    k_val=ord(k[i])-ord('A')
    #perform decryption
    decrypval=(c_val-k_val+26)%26
    #converting back to character
    decrypted=chr(decrypval + ord('A'))
    #add to plain text
    p+=decrypted

print("Your PLain Text: ",p)
