import random

#Q5
def encryption_func(msg):
    """A function that does encryption by randomly generating an interval (between 2 and 20), space the message out accordingly, and filling the gaps with random letters"""
    interval = random.randint(2,20)
    msg_lst = [i for i in msg if i.isalpha()]
    encrypt_lst = []
    
    for x in msg_lst:
        encrypt_lst.append(x)
        
        for i in range(interval):
            encrypt_lst.append(chr(random.randint(ord("a"),ord("z")))) 
        
    return "".join(encrypt_lst[:-interval]),interval



message = "TEST"
print(encryption_func(message))



#Q6
    
def deCyph(encpt_msg,interval):
    
    """A program that decrypts messages encoded as above."""
    return encpt_msg[::interval+1]


print(deCyph(*encryption_func(message)))
