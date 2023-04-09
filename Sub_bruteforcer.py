import argparse
import requests
import sys


print("Tool is created by : \n \n  ~~SANJAY JANGRA~~ \n \n IntsaGram : cybersecjatin \n\n ")

sub_list = open("/home/kali/Desktop/seclist/Discovery/DNS/subdomains-top1million-5000.txt").read() 
subdoms = sub_list.split('\n')

print("target is : ", sys.argv[1])

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}" 

    try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains)   
