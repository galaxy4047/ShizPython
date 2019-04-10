import obd,time
from threading import Timer
import itertools
import serial
import re
import MySQLdb

# OBD setup
obd.logger.setLevel(obd.logging.DEBUG)
ser=serial.Serial("/dev/ttyACM0",9600)
ports = obd.scan_serial()
print "Ports: " 
print ports
connection = obd.OBD("/dev/ttyUSB0",baudrate=38400,fast=False)
print "Connection status: " 
print connection.status()

class sql:
	def __init__(self):
# Open database connection
		self.conn = MySQLdb.connect("localhost","rasp","raspberry","data" )
		self.ctrl=self.conn.cursor()
	def createtb(self):
		self.table="value"
		self.day="timestamp"
		self.accelator="accelerator"
		self.brake="break"
		self.clutch="cluch"
		self.gear="gear"
		self.handbrake="handbrake"
		self.indicator="indicator"
		self.rpm="rpm"
		self.speed="speed"
		self.turn="turn"
		self.ctrl.execute("drop table if exists Driver ")
		self.ctrl.execute("create table if not exists {tn}({d} timestamp not null,{sensorval1} INT not null,{sensorval2} INT not null ,{sensorval3} INT not null,{sensorval4} INT not null,{sensorval5} INT not null,{sensorval6} INT not null,{sensorval7} INT not null,{sensorval8} INT not null ,{sensorval9} INT not null )"\
		.format(tn=self.table,d=self.day,sensorval1=self.accelator,sensorval2=self.brake,sensorval3=self.clutch,sensorval4=self.gear,sensorval5=self.handbrake,sensorval6=self.indicator,sensorval7=self.rpm,sensorval8=self.speed,sensorval9=self.turn))
	def insert_tb(self,sense1,sense2,sense3,sense4,sense5,sense6,sense7,sense8,sense9):
		self.table="Driver"
		self.accelator=sense1
		self.brake=sense2
		self.clutch=sense3
		self.gear=sense4
		self.handbrake=sense5
		self.indicator=sense6
		self.rpm=sense7
		self.speed=sense8
		self.turn=sense9
		try:
			self.ctrl.execute("insert into {tn} values(CURRENT_TIMESTAMP(),{s1},{s2},{s3},{s4},{s5},{s6},{s7},{s8},{s9})"\
			.format(tn=self.table,s1=self.accelator,s2=self.brake,s3=self.clutch,s4=self.gear,s5=self.handbrake,s6=self.indicator,s7=self.rpm,s8=self.speed,s9=self.turn))
			self.conn.commit()
		except:
			self.conn.rollback()
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
		rpm_val=0
		speed_val=0
		try:
	        res1 = connection.query(obd.commands.RPM,force=True)
	        #print(res.value)
	        res2 = connection.query(obd.commands.SPEED,force=True)
	        rpm_str=str(res1.value)
	        rpm_list=rpm_str.split(' ')
	        rpm_float=rpm_list[0].split('.')
	        print "Integer RPM = "
	        print rpm_float[0]
	        rpm_val=int(rpm_float[0])
	        #print int(rpm_float[0],10)
	        
	        speed_str=str(res2.value)
	        speed_list=speed_str.split(' ')
	        speed_float=speed_list[0].split('.')
	        print "Integer SPEED = "
	        print speed_float[0]
	        speed_val=int(speed_float[0])
	        #print(speed_float[0],10)        
	        #print(res.unit)
    	except Exception as ex:
        	print "Error: " + str(ex)
    		#time.sleep(0.5)
	#	var="10,20,30,40,50,60,70,80,90,100";
		var=ser.readline()
		print var
		string=var
		values=re.split(',',var)
		print values
		#var1=int(values[0])
		#var2=int(values[1])
		s.insert_tb(int(values[0]),int(values[1]),int(values[2]),int(values[3]),int(values[4]),int(values[5]),int(values[6]),rpm_val,speed_val,int(values[9]))
		#f.write(string)
#		s.select_tb
		#print val 
	for i in itertools.count():
	#for i in range(10):
		#time.sleep(0.5)
		print "loop "
		Timer(0.1,do()).start
		#time.sleep(1)
	print stringval
