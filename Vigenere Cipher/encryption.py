#take input from user
p = input("Enter Plain Text: ").upper()
k= input ("Enter Key: ").upper()
#checking the length of key, so that key could be repeated if it is shorter
if len (k)< len(p): 
    k = (k * (len(p) // len(k) + 1))[:len(p)]
#initialize cipher text as empty string
    c=""
#loop through each char in p
for i in range(len(p)):
    #convert plaintext to number
    p_val=ord(p[i])-ord('A')
    #convert key to number
    k_val=ord(k[i])-ord('A')
    #perform encryption
    encrypval=(p_val+k_val)%26
    #converting back to character
    encrypted=chr(encrypval + ord('A'))
    #add to cipher text
    c+=encrypted

print("Your Cipher Text: ",c)


