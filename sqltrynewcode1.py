import sqlite3	
import time
from threading import Timer
import itertools
import serial
import re
ser=serial.Serial("COM7",9600)
f=open("sqltest.txt","w")
stringval=''
class sql:
	def __init__(self):
		self.conn=sqlite3.connect('Drive.db')
		self.ctrl=self.conn.cursor()
	def createtb(self):
		self.UpdatableStringval=""
		self.table="Driver"
		self.day="day"
		self.accelator="accelerator"
		self.brake="break"
		self.clutch="cluch"
		self.gear="gear"
		self.handbrake="handbrake"
		self.leftind="leftind"
		self.rightind="rightind"
		self.rpm="rpm"
		self.speed="speed"
                self.turn="turn"
		#self.ctrl.execute("drop table if exists Driver ")
		self.ctrl.execute("create table if not exists {tn}({d} datetime not null,{sensorval1} INT not null,{sensorval2} INT not null ,{sensorval3} INT not null,{sensorval4} INT not null,{sensorval5} INT not null,{sensorval6} INT not null,{sensorval7} INT not null,{sensorval8} INT not null,{sensorval9} INT not null ,{sensorval10} INT not null )"\
		.format(tn=self.table,d=self.day,sensorval1=self.accelator,sensorval2=self.brake,sensorval3=self.clutch,sensorval4=self.gear,sensorval5=self.handbrake,sensorval6=self.leftind,sensorval7=self.rightind,sensorval8=self.rpm,sensorval9=self.speed,sensorval10=self.turn))
	def insert_tb(self,sense1,sense2,sense3,sense4,sense5,sense6,sense7,sense8,sense9,sense10):
		self.table="Driver"
		self.accelator=sense1
		self.brake=sense2
		self.clutch=sense3
		self.gear=sense4
		self.handbrake=sense5
		self.leftind=sense6
		self.rightind=sense7
		self.rpm=sense8
		self.speed=sense9
		self.turn=sense10
		self.ctrl.execute("insert into {tn} values(datetime('now'),{s1},{s2},{s3},{s4},{s5},{s6},{s7},{s8},{s9},{s10})"\
		.format(tn=self.table,s1=self.accelator,s2=self.brake,s3=self.clutch,s4=self.gear,s5=self.handbrake,s6=self.leftind,s7=self.rightind,s8=self.rpm,s9=self.speed,s10=self.turn))
		self.conn.commit()
	'''def select_tb(self):
		rows=self.ctrl.execute("select * from Driver")
		print "helooooo"
		for row in rows:
			print row
		self.conn.commit()
	'''
	def __del__(self):
		self.conn.close()
if __name__=="__main__":
	s=sql()
	s.createtb()
	def do():
		var=ser.readline()
		print var
		string=var
		values=re.split(',',var)
		print values
		#var1=int(values[0])
		#var2=int(values[1])
		s.insert_tb(int(values[0]),int(values[1]),int(values[2]),int(values[3]),int(values[4]),int(values[5]),int(values[6]),int(values[7]),int(values[8]))
		f.write(string)
		s.select_tb
		#print val 
	#for i in itertools.count():
	for i in range(1,10):
		time.sleep(0.5)
		print "loop"
		Timer(1,do()).start
		time.sleep(1)
	print stringval