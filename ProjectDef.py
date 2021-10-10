from tkinter import *
import nmap
import os
import threading
from twilio.rest import Client
from datetime import datetime

IPlist = []


class util(object):
    def get_ip(self):
        ip = os.popen("ipconfig")
        # print(ip)
        for line in ip.readlines():
            if "IPv4 Address" in line:
                start = line.find(":")
                # print("{0}".format(line[start+2:-1]))
                address = "{0}".format(line[start + 2:-1])
                # end = -1
                # output = line[start+2:end]
                IPlist.append(address)

        return IPlist


def Scanner(ip_address, textbox):
    ThreadList = []

    def Pinger():
        Address = formatted_ip + str(ip)
        ping_result = os.popen(f"ping -n 1 {Address}").read()
        if "TTL" in ping_result:
            textbox.insert(END, f"{Address} Alive\n")
            # print(f"{Address} Alive")

    textbox.insert(END, f"Chosen network: {ip_address}\n")

    StartIP = 0
    EndIP = 254

    SplitIP = ip_address.split('.')
    formatted_ip = ".".join(SplitIP[:-1]) + '.'

    t1 = datetime.now()
    textbox.insert(END, "Scanning in Progress... \n")

    for ip in range(StartIP, EndIP):
        PingerThread = threading.Thread(target=Pinger, )
        ThreadList.append(PingerThread)
        PingerThread.start()

    for Thread in ThreadList:
        Thread.join()

    t2 = datetime.now()
    total = t2 - t1
    textbox.insert(END, f"Scanning completed in: {total}\n")


def DeepScanner(ip_address, textbox):
    ThreadList = []

    def Nmaper():
        nm = nmap.PortScanner()
        Address = formatted_ip + str(ip)
        ip_addr = str(Address)
        nm.scan(f"{Address}", '1-1024', '-v -sS')
        if nm[ip_addr].state() == "down":
            textbox.insert(END, f"Ip Address: {Address} Status: Down!\n")
        else:
            textbox.insert(END, f"Ip Address: {Address} Status: up!", nm[ip_addr].state(), "\n")
            Protocol = nm[ip_addr].all_protocols()
            textbox.insert(END, f"Protocol: {Protocol}\n")
            PortList = ""
            for i in nm[Address]['tcp'].keys():
                PortList += str(i)
                PortList += str(",")
            textbox.insert(END, f"Open Ports: {PortList}\n")

    textbox.insert(END, f"Chosen network : {ip_address}\n")

    StartIP = 0
    EndIP = 254

    SplitIP = ip_address.split('.')
    formatted_ip = ".".join(SplitIP[:-1]) + '.'

    t1 = datetime.now()
    textbox.insert(END, "Scanning in Progress...\n")

    for ip in range(StartIP, EndIP):
        Nmaper()

    t2 = datetime.now()
    total = t2 - t1
    textbox.insert(END, f"Scanning completed in: {total}\n")


def SendSMS(SmsBody, SmsTo):
    account_sid = "Enter a Twilio account sid."
    auth_token = "Enter a Twilio auth token."
    client = Client(account_sid, auth_token)

    message = client.messages.create(

        body=SmsBody,
        from_='Enter a Twilio Number',
        to=SmsTo
    )
    # print(message.sid)
