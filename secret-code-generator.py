while True:
    print("======Secret code generator====== ") #create the Menu bar for the code Generator
    print("1.Encode Message")
    print("2.Decode Message")
    print("3.Exit")
    choice = input("Enter your choice between (1-3): ")#take input for the operation


    if choice == '1':   #check for the encoding of message
        print("Encoding is selected")
        message=input('enter the message: ')
        shift=int(input('enter the shift value: '))
        def Encoding(message,shift):
            encoded_msg=''
            for char in message: #traversing throught the message
                if char.isalpha():
                    if char.isupper():
                        position = ord(char) - ord('A')
                        new_position = (position +shift)%26
                        new_char = chr(new_position + ord('A'))
                        encoded_msg+=new_char
                    else:
                        position = ord(char)-ord('a')
                        new_position=(position+shift)%26
                        new_char =  chr(new_position+ord('a'))
                        
                        encoded_msg+=new_char
                else:
                    encoded_msg+=char
            return encoded_msg
        Encoding_result=Encoding(message,shift)
        print(Encoding_result)
            
    elif choice == '2':  #check for the decoding  message
        print("Decoding is selected")
        Decoded_msg=''
        encoded_msg=input('Enter the Encoded msg to decode: ')
        decode_shift=int(input('enter shift value to decode the msg: '))
        def Decoding(encoded_msg,decode_shift):
            decoded_msg=''
            for i in encoded_msg:
                if i.isalpha():
                    if i.isupper():
                        position=ord(i)-ord('A')
                        new_position= (position- decode_shift)%26
                        new_char = chr(new_position + ord('A'))
                        decoded_msg+=new_char
                    else:
                        position = ord(i)-ord('a')
                        new_position=(position-decode_shift)%26
                        new_char =  chr(new_position+ord('a'))
                        decoded_msg+=new_char
                else:
                    decoded_msg+=i
            return decoded_msg
        Decoding_result=Decoding(encoded_msg,decode_shift)
        print(Decoding_result)
                        
        
    elif choice == '3':   #check for the exit choice
        print("program closed")
        
    else: #check whether user entered input is invalid input
        print("invalid choice")

