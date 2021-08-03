#! /usr/bin/python
import sys
import os.path
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import RPi.GPIO as GPIO
import json
from datetime import datetime
import time
import threading
from temp import *
from threading import Thread
from time import sleep
#Initialize Raspberry PI GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.output(17, True)
GPIO.output(27, True)
GPIO.output(22, True)
GPIO.output(5, True)
GPIO.output(6, True)
GPIO.output(13, True)
GPIO.output(19, True)
GPIO.output(26, True)
#Tornado Folder Paths
settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static")
	)

#Tonado server port
PORT = 80
pathroot='/home/pi/Server'
backupName="sample.json" 
backup_path = os.path.join(pathroot,backupName)
thread = 0
temptask = 0
run = True
openloop = True
closeloop = True


switch_state = {
"switch_1_open" : "unchecked",
"switch_1_mid" : "checked",
"switch_1_close" : "unchecked",
"switch_2_open" : "unchecked",
"switch_2_mid" : "checked",
"switch_2_close" : "unchecked",
"switch_2" : "unchecked",
"switch_3" : "unchecked",
"switch_4" : "unchecked",
"switch_5" : "unchecked",
"switch_6" : "unchecked",
"switch_1_start_temp": "00.0",
"switch_1_end_temp": "00.0",
"switch_2_start_temp": "00.0",
"switch_2_end_temp": "00.0",
"switch_3_time": "00:00",
"switch_3_duration": "00:00",
"switch_4_time": "00:00",
"switch_4_duration": "00:00",
"switch_5_time": "00:00",
"switch_5_duration": "00:00",
"switch_6_time": "00:00",
"switch_6_duration": "00:00",
"time":"00:00",
"temp":"00.0",
"door1":"closed",
"door2":"closed"
}


class MainHandler(tornado.web.RequestHandler):
  def get(self):
     print ("[HTTP](MainHandler) Uzytkownik Polaczony.")
     #self.render("index.html")
     #self.write(json.loads(switch_state))
     self.render("index.html", data=switch_state)
    

	
class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    print ('Server: Polaczenie zostalo nawiazane.')
    
  def on_message(self, message):
    
    print ('Server: Przychodzace zadanie:'), message
    
    if message == "switch_1_open":
        switch_state.update({'switch_1_mid':'unchecked'})
        switch_state.update({'switch_1_open': 'checked'})
        print(switch_state['door1'])
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch_1_open - checked")
        
    if message == "switch_1_close":
        switch_state.update({'switch_1_mid':'unchecked'})
        switch_state.update({'switch_1_close': 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch_1_close - checked")
    
    if message == "switch_2_open":
        switch_state.update({'switch_2_mid':'unchecked'})
        switch_state.update({'switch_2_open': 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch_2_open - checked")
        
    if message == "switch_2_close":
        switch_state.update({'switch_2_mid':'unchecked'})
        switch_state.update({'switch_2_close': 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch_2_close - checked")

    if message == 'switch_3_on':
      GPIO.output(13, False)
      switch_state.update({'switch_3': 'checked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 3 on")

    if message == 'switch_3_off':
      GPIO.output(13, True)
      switch_state.update({'switch_3': 'unchecked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 3 off")
      
    if message == 'switch_4_on':
      GPIO.output(26, False)
      switch_state.update({'switch_4': 'checked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 4 on")
    
    if message == 'switch_4_off':
      GPIO.output(26, True)
      switch_state.update({'switch_4': 'unchecked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 4 off")

    if message == 'switch_5_on':
      GPIO.output(19, False)
      switch_state.update({'switch_5': 'checked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 5 on")

    if message == 'switch_5_off':
      GPIO.output(19, True)
      switch_state.update({'switch_5': 'unchecked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 5 off")

    if message == 'switch_6_on':
      GPIO.output(6, False)
      switch_state.update({'switch_6': 'checked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 6 on")

    if message == 'switch_6_off':
      GPIO.output(6, True)
      switch_state.update({'switch_6': 'unchecked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 6 off")
    
    if message == 'switch_7_on':
      GPIO.output(19, False)
      switch_state.update({'switch_7': 'checked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 7 on")

    if message == 'switch_7_off':
      GPIO.output(19, True)
      switch_state.update({'switch_7': 'unchecked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 7 off")

    if message == 'switch_8_on':
      GPIO.output(26, False)
      switch_state.update({'switch_8': 'checked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 8 on")

    if message == 'switch_8_off':
      GPIO.output(26, True)
      switch_state.update({'switch_8': 'unchecked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 8 off")

    if "switch_1_start_temp" in message:
      tempstart = message[20:24]
      switch_state.update({'switch_1_start_temp': tempstart})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 1 start tem")
      print(tempstart)
      
    if "switch_1_end_temp" in message:
      tempend = message[18:22]
      switch_state.update({'switch_1_end_temp': tempend})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 1 endtemp")
      print(tempend)
    
    if "switch_2_start_temp" in message:
      tempstart = message[20:24]
      switch_state.update({'switch_2_start_temp': tempstart})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 2 start temp")
      print(tempstart)
    
    if "switch_2_end_temp" in message:
      tempend = message[18:22]
      switch_state.update({'switch_2_end_temp': tempend})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 2 endtemp")
      print(tempend)
    
    if "switch_3_time" in message:
      time = message[14:20]
      switch_state.update({'switch_3_time': time})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 3 time")
      print(time)
    
    if "switch_3_duration" in message:
      duration = message[18:23]
      switch_state.update({'switch_3_duration': duration})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 3 duration")
      print(duration)

    if "switch_4_time" in message:
      time = message[14:20]
      switch_state.update({'switch_4_time': time})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 4 time")
      print(time)
    
    if "switch_4_duration" in message:
      duration = message[18:23]
      switch_state.update({'switch_4_duration': duration})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 4 duration")
      print(duration)
    
    if "switch_5_time" in message:
      time = message[14:20]
      switch_state.update({'switch_5_time': time})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 5 time")
      print(time)
    
    if "switch_5_duration" in message:
      duration = message[18:23]
      switch_state.update({'switch_5_duration': duration})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 5 duration")
      print(duration)

    if "switch_6_time" in message:
      time = message[14:20]
      switch_state.update({'switch_6_time': time})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 6 time")
      print(time)
    
    if "switch_6_duration" in message:
      duration = message[18:23]
      switch_state.update({'switch_6_duration': duration})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano switch 6 duration")
      print(duration)

    if "STOP" in message:
      switch_state.update({'switch_1_mid' : 'checked'})
      switch_state.update({'switch_1_close' : 'unchecked'})
      switch_state.update({'switch_1_open' : 'unchecked'})
      switch_state.update({'door1' : 'mid'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano stop")

    if "abort" in message:
      switch_state.update({'switch_2_mid' : 'checked'})
      switch_state.update({'switch_2_close' : 'unchecked'})
      switch_state.update({'switch_2_open' : 'unchecked'})
      switch_state.update({'door2' : 'mid'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano abort")


  def on_close(self):
    print ('Server: Polaczenie zostalo zakonczone.')


application = tornado.web.Application([
  (r'/', MainHandler),
  (r'/ws', WSHandler),
  ], **settings)

def exit_handler():
  print 'My application is ending!'
  run=False
  print("Thread Krawol!!")
  thread.join()

def timer_task():
  while run:
    now = datetime.now()
    curr_time = now.strftime("%H:%M")
    switch_state.update({'time':curr_time})
    if(curr_time == switch_state["switch_3_time"] and curr_time != "00:00"):
      GPIO.output(13, False)
      if(switch_state["switch_3"] == "unchecked"):
        switch_state.update({'switch_3': 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("zapisano switch_3 checked")
    if(curr_time == switch_state["switch_3_duration"] and curr_time != "00:00"):
      GPIO.output(13, True)
      if(switch_state["switch_3"] == "checked"):
        switch_state.update({'switch_3': 'unchecked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("zapisano switch_3 unchecked")
    if(curr_time == switch_state["switch_4_time"] and curr_time != "00:00"):
      GPIO.output(26, False)
      if(switch_state["switch_4"] == "unchecked"):
        switch_state.update({'switch_4': 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("zapisano switch_3 checked")
    if(curr_time == switch_state["switch_4_duration"] and curr_time != "00:00"):
      GPIO.output(26, True)
      if(switch_state["switch_4"] == "checked"):
        switch_state.update({'switch_4': 'unchecked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("zapisano switch_4 unchecked")
    if(curr_time == switch_state["switch_5_time"] and curr_time != "00:00"):
      GPIO.output(19, False)
      if(switch_state["switch_5"] == "unchecked"):
        switch_state.update({'switch_5': 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("zapisano switch_5 checked")
    if(curr_time == switch_state["switch_5_duration"] and curr_time != "00:00"):
      GPIO.output(19, True)
      if(switch_state["switch_5"] == "checked"):
        switch_state.update({'switch_5': 'unchecked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("zapisano switch_5 unchecked")
    if(curr_time == switch_state["switch_6_time"] and curr_time != "00:00"):
      GPIO.output(6, False)
      if(switch_state["switch_6"] == "unchecked"):
        switch_state.update({'switch_6': 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("zapisano switch_6 checked")
    if(curr_time == switch_state["switch_6_duration"] and curr_time != "00:00"):
      GPIO.output(6, True)
      if(switch_state["switch_6"] == "checked"):
        switch_state.update({'switch_6': 'unchecked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("zapisano switch_6 checked")

def get_temp():
    currtemp = switch_state["temp"]
    currtemp = read_temp()
    print("[" + switch_state["time"] + "]" + "Obecna temperatura: " + str(currtemp))
    sleep(60)
    return currtemp 

def temp_task():
  while run:
    curr_temp = get_temp() 
    switch_state.update({'temp':curr_temp})
    if(float(switch_state["switch_1_start_temp"]) != 00.0):
      if(curr_temp >= float(switch_state["switch_1_start_temp"])):
        print("przeszlo")
        if(switch_state['door1'] == 'closed'):
          timer_start = 0
          timer_duration = 0
          if(timer_start == 0):
            switch_state.update({'switch_1_mid' : 'unchecked'})
            switch_state.update({'switch_1_open' : 'checked'})
            json_object= json.dumps(switch_state)
            with open(backup_path, "w") as outfile:
              outfile.write(json_object)
              outfile.close() 
            print("Otwieranie drzwi [Przod]")
            timer_start = time.time()
            timer_duration = 80
            GPIO.output(17, False)
            if(time.time() >= timer_start + timer_duration):
              print("doneotwieranie")
              GPIO.output(17, True)
              timer_start = 0
              timer_duration = 0
              switch_state.update({'door1' : 'opened'})
              switch_state.update({'switch_1_open' : 'unchecked'})
              switch_state.update({'switch_1_mid' : 'checked'})
              json_object= json.dumps(switch_state)
              with open(backup_path, "w") as outfile:
                outfile.write(json_object)
                outfile.close() 
                print("Otwarto drzwi [Przod]")
    if(float(switch_state["switch_2_start_temp"]) != 00.0):
      if(curr_temp >= float(switch_state["switch_2_start_temp"])):
        print("przeszlov2")
        if(switch_state['door2'] == 'closed'):
          timer2_start = 0
          timer2_duration = 0
          if(timer2_start == 0):
            switch_state.update({'switch_2_mid' : 'unchecked'})
            switch_state.update({'switch_2_open' : 'checked'})
            json_object= json.dumps(switch_state)
            with open(backup_path, "w") as outfile:
              outfile.write(json_object)
              outfile.close() 
            print("Otwieranie drzwi  [Tyl]")
            timer2_start = time.time()
            timer2_duration = 80
            GPIO.output(22, False)
            if(time.time() >= timer2_start+timer2_duration):
              GPIO.output(22, True)
              timer2_start = 0
              timer2_duration = 0
              switch_state.update({'door2' : 'opened'})
              switch_state.update({'switch_2_open' : 'unchecked'})
              switch_state.update({'switch_2_mid' : 'checked'})
              json_object= json.dumps(switch_state)
              with open(backup_path, "w") as outfile:
                outfile.write(json_object)
                outfile.close() 
                print("Otwarto drzwi [Tyl]")

    if(float(switch_state["switch_1_end_temp"]) != 00.0):
      if(curr_temp <= float(switch_state["switch_1_end_temp"]) ):
        if(switch_state['door1'] == 'opened'):
          timer3_start = 0
          timer3_duration = 0
          if(timer3_start == 0):
            switch_state.update({'switch_1_mid' : 'unchecked'})
            switch_state.update({'switch_1_close' : 'checked'})
            json_object= json.dumps(switch_state)
            with open(backup_path, "w") as outfile:
              outfile.write(json_object)
              outfile.close() 
            print("Zamykanie drzwi [Przod]")
            timer3_start = time.time()
            timer3_duration = 80
            GPIO.output(27, False)
            if(time.time() >= timer3_start+timer3_duration):
              GPIO.output(27, True)
              timer3_start = 0
              timer3_duration = 0
              switch_state.update({'door1' : 'closed'})
              switch_state.update({'switch_1_close' : 'unchecked'})
              switch_state.update({'switch_1_mid' : 'checked'})
              json_object= json.dumps(switch_state)
              with open(backup_path, "w") as outfile:
                outfile.write(json_object)
                outfile.close() 
                print("Zamknieto drzwi [Przod]")  

    if(float(switch_state["switch_2_end_temp"]) != 00.0):
      if(curr_temp <= float(switch_state["switch_2_end_temp"]) ):
        if(switch_state['door2'] == 'opened'):
          timer4_start = 0
          timer4_duration = 0
          if(timer4_start == 0):
            switch_state.update({'switch_2_mid' : 'unchecked'})
            switch_state.update({'switch_2_close' : 'checked'})
            json_object= json.dumps(switch_state)
            with open(backup_path, "w") as outfile:
              outfile.write(json_object)
              outfile.close() 
            print("Zamykanie drzwi [Tyl]")
            timer4_start = time.time()
            timer4_duration = 80
            GPIO.output(5, False)
            if(time.time() >= timer4_start + timer4_duration ):
              GPIO.output(5, True)
              timer4_start  = 0
              timer4_duration  = 0
              switch_state.update({'door2' : 'closed'})
              switch_state.update({'switch_2_close' : 'unchecked'})
              switch_state.update({'switch_2_mid' : 'checked'})
              json_object= json.dumps(switch_state)
              with open(backup_path, "w") as outfile:
                outfile.write(json_object)
                outfile.close() 
                print("Zamknieto drzwi [Tyl]")

def engine_Task():
  while run:
    if(switch_state['switch_1_open'] == 'checked'):

      if(switch_state['door1'] == 'opened'):
        time_start = 0
        time_duration = 0
        switch_state.update({'switch_1_open' : 'unchecked'})
        switch_state.update({'switch_1_mid' : 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("Drzwi [Przod] sa juz otwarte!")

      if(switch_state['door1'] == 'closed'):
        if(time_start == 0):
          print("Otwieranie drzwi [Przod]")
          time_start = time.time()
          time_duration = 80
          GPIO.output(17, False)
        if(time.time() >= time_start + time_duration):
          print("doneotwieranie")
          GPIO.output(17, True)
          time_start = 0
          time_duration = 0
          switch_state.update({'door1' : 'opened'})
          switch_state.update({'switch_1_open' : 'unchecked'})
          switch_state.update({'switch_1_mid' : 'checked'})
          json_object= json.dumps(switch_state)
          with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Otwarto drzwi [Przod]")

      if(switch_state['door1'] == 'mid'):
        if(time_start == 0):
          print("Otwieranie drzwi po przerwaniu [Przod]")
          time_start = time.time()
          time_duration = 80
          GPIO.output(17, False)
        if(time.time() >= time_start+time_duration):
          GPIO.output(17, True)
          time_start = 0
          time_duration = 0
          switch_state.update({'door1' : 'opened'})
          switch_state.update({'switch_1_open' : 'unchecked'})
          switch_state.update({'switch_1_mid' : 'checked'})
          json_object= json.dumps(switch_state)
          with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Otwarto drzwi [Przod]")

    if(switch_state['switch_1_close'] == 'checked'):

      if(switch_state['door1'] == 'closed'):
        time_start = 0
        time_duration = 0
        switch_state.update({'switch_1_close' : 'unchecked'})
        switch_state.update({'switch_1_mid' : 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Drzwi [Przod] sa juz zamkniete!")

      if(switch_state['door1'] == 'opened'):
        if(time_start == 0):
          print("Zamykanie drzwi [Przod]")
          time_start = time.time()
          time_duration = 80
          GPIO.output(27, False)
        if(time.time() >= time_start+time_duration):
          GPIO.output(27, True)
          time_start = 0
          time_duration = 0
          switch_state.update({'door1' : 'closed'})
          switch_state.update({'switch_1_close' : 'unchecked'})
          switch_state.update({'switch_1_mid' : 'checked'})
          json_object= json.dumps(switch_state)
          with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Zamknieto drzwi [Przod]")

      if(switch_state['door1'] == 'mid'):
        if(time_start == 0):
          print("Zamykanie drzwi po przerwaniu [Przod]")
          time_start = time.time()
          time_duration = 80
          time_check = time_start + time_duration
          GPIO.output(27, False)
        if(time.time() >= time_start+time_duration):
          GPIO.output(27, True)
          time_start = 0
          time_duration = 0
          switch_state.update({'door1' : 'closed'})
          switch_state.update({'switch_1_close' : 'unchecked'})
          switch_state.update({'switch_1_mid' : 'checked'})
          json_object= json.dumps(switch_state)
          with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Zamknieto drzwi [Przod]")

    if(switch_state['switch_1_mid'] == 'checked'):
      GPIO.output(27, True)
      GPIO.output(17, True)
      time_start = 0
      time_duration = 0
      switch_state.update({'switch_1_close' : 'unchecked'})
      switch_state.update({'switch_1_open' : 'unchecked'})
      switch_state.update({'switch_1_mid' : 'checked'})
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
    
    if(switch_state['switch_2_open'] == 'checked'):

      if(switch_state['door2'] == 'opened'):
        time_start2 = 0
        time_duration2 = 0
        switch_state.update({'switch_2_open' : 'unchecked'})
        switch_state.update({'switch_2_mid' : 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("Drzwi [Tyl] sa juz otwarte!")

      if(switch_state['door2'] == 'closed'):
        if(time_start2 == 0):
          print("Otwieranie drzwi  [Tyl]")
          time_start2 = time.time()
          time_duration2 = 80
          GPIO.output(22, False)
        if(time.time() >= time_start2+time_duration2):
          GPIO.output(22, True)
          time_start2 = 0
          time_duration2 = 0
          switch_state.update({'door2' : 'opened'})
          switch_state.update({'switch_2_open' : 'unchecked'})
          switch_state.update({'switch_2_mid' : 'checked'})
          json_object= json.dumps(switch_state)
          with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Otwarto drzwi [Tyl]")

      if(switch_state['door2'] == 'mid'):
        if(time_start2 == 0):
          print("Otwieranie drzwi po przerwaniu [Tyl]")
          time_start2 = time.time()
          time_duration2 = 80
          GPIO.output(22, False)
        if(time.time() >= time_start2+time_duration2):
          GPIO.output(22, True)
          time_start2 = 0
          time_duration2 = 0
          switch_state.update({'door2' : 'opened'})
          switch_state.update({'switch_2_open' : 'unchecked'})
          switch_state.update({'switch_2_mid' : 'checked'})
          json_object= json.dumps(switch_state)
          with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Otwarto drzwi [Tyl]")
    
    if(switch_state['switch_2_close'] == 'checked'):

      if(switch_state['door2'] == 'closed'):
        time_start2 = 0
        time_duration2 = 0
        switch_state.update({'switch_2_close' : 'unchecked'})
        switch_state.update({'switch_2_mid' : 'checked'})
        json_object= json.dumps(switch_state)
        with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Drzwi [Tyl] sa juz zamkniete!")

      if(switch_state['door2'] == 'opened'):
        if(time_start2 == 0):
          print("Zamykanie drzwi [Tyl]")
          time_start2 = time.time()
          time_duration2 = 80
          GPIO.output(5, False)
        if(time.time() >= time_start2+time_duration2):
          GPIO.output(5, True)
          time_start2 = 0
          time_duration2 = 0
          switch_state.update({'door2' : 'closed'})
          switch_state.update({'switch_2_close' : 'unchecked'})
          switch_state.update({'switch_2_mid' : 'checked'})
          json_object= json.dumps(switch_state)
          with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Zamknieto drzwi [Tyl]")

      if(switch_state['door2'] == 'mid'):
        if(time_start2 == 0):
          print("Zamykanie drzwi po przerwaniu [Tyl]")
          time_start2 = time.time()
          time_duration2 = 80
          GPIO.output(5, False)
        if(time.time() >= time_start2+time_duration2):
          GPIO.output(5, True)
          time_start2 = 0
          time_duration2 = 0
          switch_state.update({'door2' : 'closed'})
          switch_state.update({'switch_2_close' : 'unchecked'})
          switch_state.update({'switch_2_mid' : 'checked'})
          json_object= json.dumps(switch_state)
          with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
            print("Zamknieto drzwi [Tyl]")

    if(switch_state['switch_2_mid'] == 'checked'):
      GPIO.output(5, True)
      GPIO.output(22, True)
      time_start2 = 0
      time_duration2 = 0
      switch_state.update({'switch_2_mid' : 'checked'})
      switch_state.update({'switch_2_close' : 'unchecked'})
      switch_state.update({'switch_2_open' : 'unchecked'})
      
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
            outfile.write(json_object)
            outfile.close() 
    
timertask = Thread(target = timer_task)
temptask = Thread(target = temp_task)
enginetask = Thread(target = engine_Task)

if __name__ == "__main__":
    try:
      with open(backup_path) as json_file:
       switch_state = json.load(json_file)
      http_server = tornado.httpserver.HTTPServer(application)
      http_server.listen(PORT)
      main_loop = tornado.ioloop.IOLoop.instance()
      timertask.setDaemon(True)
      temptask.setDaemon(True)
      enginetask.setDaemon(True)
      timertask.start()
      temptask.start()  
      enginetask.start() 
      print ("Usluga serwera uruchomiona.")
      main_loop.start()
      timertask.join()
      temptask.join()
      enginetask.join()
     
     
        
    except Exception as e:
      #print ("Obsluzono wyjatek - Usluga serwera wylaczona.")
      print(e)
      print("!problem")
      GPIO.cleanup()
    except KeyboardInterrupt:
      print("Wyjatek Ctrl+C")
      json_object= json.dumps(switch_state)
      with open(backup_path, "w") as outfile:
          outfile.write(json_object)
          outfile.close() 
          print("zapisano po keyboardinterrupt")
      run = False
      timertask.join()
      print ( "e spisz?")
      temptask.join()
      enginetask.join()
      GPIO.cleanup()
      sys.exit(1)
#End of Program
