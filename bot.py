#!/usr/bin/env python3
import time
import os 
import email


def main():
    os.chdir('/home/kirby/Maildir/new/')
    for filename in os.listdir(os.getcwd()):
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            msgStr = ""
            for line in f:
                message = f.readlines()
                msgStr+=str(message)

            #mail = email.message_from_string(msgStr)
            #print(mail['from'])
            #print(mail.keys())
if __name__ == '__main__':
    main()

'''
i = 1
while(True):
    print(i)
    i=i+1
    time.sleep(5)
'''

