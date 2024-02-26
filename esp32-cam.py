import machine
import camera
import esp
import network
import usocket as socket
import time

station = network.WLAN(network.STA_IF)

def connect(id, password, retry):
    ssid = id
    password = password
    
    if station.isconnected() == True:   
        print("Already connected", station.ifconfig())
        return True

    station.active(True) 
    station.connect(ssid, password)
    time.sleep(1)
    while retry !=0 and not station.isconnected():
        time.sleep(1)
        retry -= 1
    return station.isconnected()

led = machine.Pin(4, machine.Pin.OUT)
try:
    camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
    #camera.framesize(camera.FRAME_96X96)
    camera.quality(40)
except:
    pass


    
result = connect("WIFINAME", "WIFIPASSWORD", 15)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('', 80))
    s.listen(5)
except Exception as e:
    print("Failed to bind the port, likely it's already binded.")

while True:
    conn, addr = s.accept()
    print("wating")
    request = None
    try:
        conn.settimeout(2)
        request = conn.recv(1024)
    except Exception as e:
        print(request)
        time.sleep(1)
        conn.close()
        continue
    print("done wating")
    print(request)
    
    pic = camera.capture()
    
    if not pic:
        print("Failed to take the picture.")
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: image/jpeg\n')
        conn.send('Access-Control-Allow-Origin: *\n')
        conn.send('Connection: close\n\n')
        conn.close()
        continue
    
    try:
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: image/jpeg\n')
        conn.send('Access-Control-Allow-Origin: *\n')
        conn.send('Connection: close\n\n')
        conn.sendall(bytes(pic))
        conn.close()
        print("response sent")
    except Exception as e:
        print("Failed sending data")


