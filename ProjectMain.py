from ProjectDef import *
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.title("SysIT Network Scan")
window.geometry("400x500")
window.resizable(False, False)
backgroundWorker = []


def ScannerButtonClick():
    ip_address = variable.get()
    t = threading.Thread(target=Scanner, args=(ip_address, ResultTextBox))
    backgroundWorker.append(t)
    t.start()


def DeepScannerButtonClick():
    ip_address = variable.get()
    t = threading.Thread(target=DeepScanner, args=(ip_address, ResultTextBox))
    backgroundWorker.append(t)
    t.start()


def CreateSmsWindow():
    SmsWindow = Toplevel(window)
    SmsWindow.title("Send Sms!")
    SmsWindow.geometry("220x95")

    def SendSmsClick():
        Name = SmsSenderEntry.get()
        ip_address = variable.get()
        To = SmsToEntry.get()
        Body = f"{Name} Scan his net Subnet:{ip_address}"
        SendSMS(Body, To)

    def SmsExit():
        SmsWindow.destroy()

    SmsSenderLabel = Label(SmsWindow, text="Sender name: ")
    SmsSenderEntry = Entry(SmsWindow, width=20)
    SmsToLabel = Label(SmsWindow, text="To: ")
    SmsToEntry = Entry(SmsWindow, width=30)
    SmsSendButton = Button(SmsWindow, text="Send", command=SendSmsClick)
    SmsExitButton = Button(SmsWindow, text="Exit", command=SmsExit)

    SmsSenderLabel.place(x=5, y=5)
    SmsSenderEntry.place(x=82, y=5)
    SmsToLabel.place(x=5, y=35)
    SmsToEntry.place(x=25, y=35)
    SmsSendButton.place(x=139, y=60)
    SmsExitButton.place(x=179, y=60)


def Exit():
    window.destroy()


u = util()
u.get_ip()
variable = StringVar(window)
variable.set(IPlist[0])

SubnetLabel = Label(window, text="Subnet: ")
SubnetEntry = OptionMenu(window, variable, *IPlist)
ScanButton = Button(window, text="Scan", command=ScannerButtonClick)
DeepScanButton = Button(window, text="Deep Scan", command=DeepScannerButtonClick)
ResultTextBox = ScrolledText(window, width=47, height=26)
ExitBottun = Button(window, text="Exit", command=Exit)
SmsButton = Button(window, text="SMS", command=CreateSmsWindow)

SubnetLabel.place(x=5, y=7)
SubnetEntry.place(x=60, y=8)
ScanButton.place(x=290, y=5)
DeepScanButton.place(x=327, y=5)
ResultTextBox.place(x=5, y=40)
ExitBottun.place(x=360, y=467)
SmsButton.place(x=320, y=467)

window.mainloop()
