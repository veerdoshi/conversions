import sys
import math
import urllib
import time
import json

class Converter():
	def conversions(self):
		print("This is a unit converter")
class Length_and_Distance(Converter):
	def conversions(self):
		print("What unit do you want to convert?")
		print("Type 1 for inches to centimeters")
		print("Type 2 for feet to meters")
		print("Type 3 for yards to meters")
		print("Type 4 for miles to kilometers")
		print("Type 5 for millimeters to inches")
		print("Type 6 for centimeters to inches")
		print("Type 7 for meters to feet")
		print("Type 8 for meters to yards")
		print("Type 9 for kilometers to miles")	
		userentry = int(sys.stdin.readline())
		print("Enter value")
		value = float(sys.stdin.readline())

		if userentry == 1:
			results = value * 2.5400
			print('Results = %.2f' %results + ' centimeters')
		elif userentry == 2:
			results = value * .3048
			print('Results = %.2f' %results + ' meters')
		elif userentry == 3:
			results = value * .9144
			print('Results = %.2f'  %results + ' meters')
		elif userentry == 4:
			results = value * 1.6093
			print('Results = %.2f'  %results + ' kilometers')
		elif userentry == 5:
			results = value * .0394
			print('Results = %.2f'  %results + ' inches')
		elif userentry == 6:
			results = value * .3937	 
			print('Results = %.2f'  %results + ' inches')
		elif userentry == 7:
			results = value * 3.2808
			print('Results = %.2f'  %results + ' feet')
		elif userentry == 8:
			results = value * 1.0936
			print('Results = %.2f'  %results + ' yards')
		elif userentry == 9:
			results = value * .6214
			print('Results = %.2f'  %results + ' miles')
		else:
			print('Does not exist')


class Time(Converter):
	def time_change(self):
		print("What unit do you want to convert?")
		print("Type 1 for minutes to seconds")
		print("Type 2 for hours to minutes")
		print("Type 3 for hours to seconds")
		print("Type 4 for days to hours")
		print("Type 5 for days to minutes")
		print("Type 6 for days to seconds")
		print("Type 7 for weeks to days")
		print("Type 8 for weeks to hours")
		print("Type 9 for weeks to minutes")
		print("Type 10 for weeks to seconds")
		print("Type 11 for months to weeks")
		print("Type 12 for months to days")
		print("Type 13 for months to hours")
		print("Type 14 for years to months")
		print("Type 15 for years to weeks")
		print("Type 16 for years to days")
		print("Type 17 for leap years to days")
		print("Type 18 for decades to years") 
		print("Type 19 for centuries to years")
		print("Type 20 for millenniums to years")
		userentry_time = int(sys.stdin.readline())
		print("Enter value")
		value_time = float(sys.stdin.readline())

		if userentry_time == 1:
			results_time = value_time * 60
			print('Results = %.2f'  %results_time + ' seconds')
		elif userentry_time == 2:
			results_time = value_time * 60
			print('Results = %.2f'  %results_time + ' minutes')
		elif userentry_time == 3:
			results_time = value_time * 3600
			print('Results = %.2f'  %results_time + ' seconds')
		elif userentry_time == 4:
			results_time = value_time * 24
			print('Results = %.2f'  %results_time + ' hours')
		elif userentry_time == 5:
			results_time = value_time * 1440
			print('Results = %.2f'  %results_time + ' minutes')
		elif userentry_time == 6:
			results_time = value_time * 86400
			print('Results = %.2f'  %results_time + ' seconds')
		elif userentry_time == 7:
			results_time = value_time * 7
			print('Results = %.2f'  %results_time + ' days')
		elif userentry_time == 8:
			results_time = value_time * 168
			print('Results = %.2f'  %results_time + ' hours')
		elif userentry_time == 9:
			results_time = value_time * 10080
			print('Results = %.2f'  %results_time + ' minutes')
		elif userentry_time == 10:
			results_time = value_time * 604800
			print('Results = %.2f'  %results_time + ' seconds')
		elif userentry_time == 11:
			results_time = value_time * 4.34
			print('Results = %.2f'  %results_time + ' weeks')
		elif userentry_time == 12:
			results_time = value_time * 30
			print('Results = %.2f'  %results_time + ' days')
		elif userentry_time == 13: 
			results_time = value_time * 730.48
			print('Results = %.2f'  %results_time + ' hours')
		elif userentry_time == 14:
			results_time = value_time * 12
			print('Results = %.2f'  %results_time + ' months')
		elif userentry_time == 15:
			results_time = value_time * 52
			print('Results = %.2f'  %results_time + ' weeks')
		elif userentry_time == 16:
			results_time = value_time * 365
			print('Results = %.2f'  %results_time + ' days')
		elif userentry_time == 17:
			results_time = value_time * 366
			print('Results = %.2f'  %results_time + ' days')
		elif userentry_time == 18:
			results_time = value_time * 10
			print('Results = %.2f'  %results_time + ' years')
		elif userentry_time == 19:
			results_time = value_time * 100
			print('Results = %.2f'  %results_time + ' years')
		elif userentry_time == 20:
			results_time = value_time * 1000
			print('Results = %.2f'  %results_time + ' years')
		else:
			print("Does not exist")			
		




class Weight_and_Mass(Converter):
	def conversions(self):
		print("What unit do you want to convert?")
		print("Type 1 for ounces to grams")
		print("Type 2 for pounds to kilograms")
		print("Type 3 for short tons to metric tons")
		print("Type 4 for kilograms to pounds")
		print("Type 5 for metric tons to short tons")
		userentry_weight = int(sys.stdin.readline())
		print("Enter value")
		value_weight = float(sys.stdin.readline())

		if userentry_weight == 1:
			results_weight = value_weight * 28.3495
			print('Results = %.2f' %value_weight + ' ounces = %.2f' %results_weight + '  grams')
		elif userentry_weight == 2:
			results_weight = value_weight * .4536
			print('Results = %.2f' %value_weight + ' pounds = %.2f' %results_weight + '  kilograms')	
		elif userentry_weight == 3:
			results_weight = value_weight * .9072
			print('Results = %.2f' %value_weight + ' short tons = %.2f' %results_weight + '  metric tons')
		elif userentry_weight == 4:
			results_weight = value_weight * 2.2046
			print('Results = %.2f' %value_weight + ' kilograms = %.2f' %results_weight + '  pounds') 	
		elif userentry_weight == 5:
			results_weight = value_weight * 1.1023
			print('Results = %.2f' %value_weight + ' metric tons = %.2f' %results_weight + 'short tons')
		else:
			print("Does not exist")

class Digital_Storage(Converter):
	def conversions_storage(self):
		print("Enter value")
		print("Type 1 for bit to byte")
		print("Type 2 for bit to kilobit")
		print("Type 3 for bit to kilobyte")
		print("Type 4 for kilobit to kilobyte")
		print("Type 5 for kilobit to megabit")
		print("Type 6 for kilobit to megabyte")
		print("Type 7 for kilobyte to megabit")
		print("Type 8 for kilobyte to megabyte")
		print("Type 9 for megabit to megabyte")
		print("Type 10 for megabit to gigabit")
		print("Type 11 for megabit to gigabyte")
		print("Type 12 for megabyte to gigabit")
		print("Type 13 for megabyte to gigabyte")
		print("Type 14 for gigabit to gigabyte")
		print("Type 15 for gigabit to terabit")
		print("Type 16 for gigabit to terabyte")
		print("Type 17 for gigabyte to terabit")
		print("Type 18 for gigabyte to terabyte")
		print("Type 19 for terabit to terabyte")
		print("Type 20 for terabit to petabit")
		print("Type 21 for terabit to petabyte")
		print("Type 22 for terabyte to petabit")
		print("Type 23 for terabyte to petabyte")
		userentry_storage = int(sys.stdin.readline())
		print("Enter value")
		value_storage = float(sys.stdin.readline())

		if userentry_storage == 1:
			results_storage = value_storage * 0.125
			print('Results = %.2f' %results_storage + ' bytes')
		elif userentry_storage == 2:
			results_storage = value_storage * 0.000976563 
			print('Results = %.2f' %results_storage + ' kilobits')
		elif userentry_storage == 3:
			results_storage = value_storage * 0.00012207 
			print('Results = %.2f' %results_storage + ' kilobytes')
		elif userentry_storage == 4:
			results_storage = value_storage * 0.125  
			print('Results = %.2f' %results_storage + ' kilobytes')
		elif userentry_storage == 5:
			results_storage = value_storage * 0.000976563 
			print('Results = %.2f' %results_storage + ' megabits')
		elif userentry_storage == 6:
			results_storage = value_storage * 0.00012207 
			print('Results = %.2f' %results_storage + ' megabytes')
		elif userentry_storage == 7:
			results_storage = value_storage * 0.0078125 
			print('Results = %.2f' %results_storage + ' megabits')
		elif userentry_storage == 8:
			results_storage = value_storage * 0.000976563 
			print('Results = %.2f' %results_storage + ' megabytes')
		elif userentry_storage == 9:
			results_storage = value_storage * 0.125 
			print('Results = %.2f' %results_storage + ' megabytes')
		elif userentry_storage == 10:
			results_storage = value_storage * 0.000976563  
			print('Results = %.2f' %results_storage + ' gigabits')
		elif userentry_storage == 11:
			results_storage = value_storage * 0.00012207 
			print('Results = %.2f' %results_storage + ' gigabytes')
		elif userentry_storage == 12:
			results_storage = value_storage * 0.0078125 
			print('Results = %.2f' %results_storage + ' gigabits')
		elif userentry_storage == 13:
			results_storage = value_storage * 0.000976563 
			print('Results = %.2f' %results_storage + ' gigabytes')
		elif userentry_storage == 14:
			results_storage = value_storage * 0.125 
			print('Results = %.2f' %results_storage + ' gigabytes')
		elif userentry_storage == 15:
			results_storage = value_storage * 0.000976563 
			print('Results = %.2f' %results_storage + ' terabits')
		elif userentry_storage == 16:
			results_storage = value_storage * 0.00012207 
			print('Results = %.2f' %results_storage + ' terabytes')
		elif userentry_storage == 17:
			results_storage = value_storage * 0.0078125 
			print('Results = %.2f' %results_storage + ' terabits')
		elif userentry_storage == 18:
			results_storage = value_storage * 0.000976563 
			print('Results = %.2f' %results_storage + ' terabytes')
		elif userentry_storage == 19:
			results_storage = value_storage * 0.125 
			print('Results = %.2f' %results_storage + ' terabytes')
		elif userentry_storage == 20:
			results_storage = value_storage * 0.000976563 
			print('Results = %.2f' %results_storage + ' petabits')
		elif userentry_storage == 21:
			results_storage = value_storage * 0.00012207 
			print('Results = %.2f' %results_storage + ' petabytes')
		elif userentry_storage == 22:
			results_storage = value_storage * 0.0078125 
			print('Results = %.2f' %results_storage + ' petabits')
		elif userentry_storage == 23:
			results_storage = value_storage * 0.000976563 
			print('Results = %.2f' %results_storage + ' petabytes')
		else:
			print("Does not exist")


class Speed_and_Velocity(Converter):
	def conversions_speed(self):
		print("Enter value")
		print("Type 1 for miles per hour to kilometers per hour")
		print("Type 2 for kilometers per hour to miles per hour")
		print("Type 3 for feet per second to centimeters per second")
		print("Type 4 for inches per second to centimeters per second")
		print("Type 5 for kilometers per second to knots")
		print("Type 6 for kilometers per second to machs")
		print("Type 7 for meters per second to miles per hour")
		print("Type 8 for miles per hour to knots")
		print("Type 9 for miles per hour to meters per second")
		print("Type 10 for machs to meters per second")
		print("Type 11 for benz to centimeters per hour")
		print("Type 12 for benz to dekameters per hour")
		print("Type 13 for knots to miles per hour")
		userentry_speed = int(sys.stdin.readline())
		print("Enter value")
		value_speed = float(sys.stdin.readline())

		if userentry_speed == 1:
			results_speed = value_speed * 1.609
			print('Results = %.2f' %results_speed + ' kilometers per hour')
		elif userentry_speed == 2:
			results_speed = value_speed * 0.621
			print('Results = %.2f' %results_speed + ' miles per hour')	
		elif userentry_speed == 3:
			results_speed = value_speed * 30.48
			print('Results = %.2f' %results_speed + ' centimeters per second')
		elif userentry_speed == 4:
			results_speed = value_speed * 2.54
			print('Results = %.2f' %results_speed + ' centimeters per second')
		elif userentry_speed == 5:
			results_speed = value_speed * 1943.844
			print('Results = %.2f' %results_speed + ' knots')
		elif userentry_speed == 6:
			results_speed = value_speed * 2.938
			print('Results = %.2f' %results_speed + ' machs')
		elif userentry_speed == 7:
			results_speed = value_speed * 2.236
			print('Results = %.2f' %results_speed + ' miles per hour')	
		elif userentry_speed == 8:
			results_speed = value_speed * 0.868
			print('Results = %.2f' %results_speed + ' knots')	
		elif userentry_speed == 9:
			results_speed = value_speed * 0.447
			print('Results = %.2f' %results_speed + ' meters per second')
		elif userentry_speed == 10:
			results_speed = value_speed * 340.29
			print('Results = %.2f' %results_speed + ' meters per second')
		elif userentry_speed == 11:
			results_speed = value_speed * 360000
			print('Results = %.2f' %results_speed + ' centimeters per hour')
		elif userentry_speed == 12:
			results_speed = value_speed * 360
			print('Results = %.2f' %results_speed + ' dekameters per hour')
		elif userentry_speed == 13:
			results_speed = value_speed * 1.150779448
			print('Results = %.2f' %results_speed + ' miles per hour') 
		else:
			print("Does not exist")						
			
class Fuel(Converter):
	def conversions_fuel(self):
		
		print("Type 1 for MPG[US] to MPG[imp.]")
		print("Type 2 for MPG[US] to Km/liter")
		print("Type 3 for MPG[US] to Liter/100km")
		print("Type 4 for MPG[imp.] to Km/liter")
		print("Type 5 for MPG[imp.] to Liter/100km")
		print("Type 6 for Km/liter to Liter/100km")
		userentry_fuel = int(sys.stdin.readline())
		print("Enter value")
		value_fuel = float(sys.stdin.readline())

		if userentry_fuel == 1:
			results_fuel = value_fuel * 1.20095
			print('Results = %.2f' %results_fuel + ' MPG[imp.]')
		elif userentry_fuel == 2:
			results_fuel = value_fuel * 0.425144
			print('Results = %.2f' %results_fuel + ' Km/liter')
		elif userentry_fuel == 3:
			results_fuel = value_fuel * 235.215
			print('Results = %.2f' %results_fuel + ' Liter/100km')			
		elif userentry_fuel == 4:
			results_fuel = value_fuel * 0.354006
			print('Results = %.2f' %results_fuel + ' Km/liter')
		elif userentry_fuel == 5:
			results_fuel = value_fuel * 282.481
			print('Results = %.2f' %results_fuel + ' Liter/100km')
		elif userentry_fuel == 6:
			results_fuel = value_fuel * 100
			print('Results = %.0f' %results_fuel + ' Liter/100km')
		else:
			print("Does not exist")				

class Temperature(Converter):
	def conversions(self):
		

		error = 1
		while(error):
	 		print("What unit do you want to convert?")
			print("Type 1 for Fahrenheit to Celsius")
			print("Type 2 for Celsius to Fahrenheit")
			print("Type 3 for Fahrenheit to Kelvin")
			print("Type 4 for Celsius to Kelvin")
			print("Type 5 for Kelvin to Fahrenheit")
			print("Type 6 for Kelvin to Celsius")
			userentry_temp = int(sys.stdin.readline())
			if(userentry_temp == 1 or userentry_temp == 2 or userentry_temp == 3 or userentry_temp == 4 or userentry_temp == 5 or userentry_temp == 6):
				error = 0

		error = 1
		while(error):
			print("Enter temp value between -100.0 to 100.00 degrees")
			value_temp = float(sys.stdin.readline())
			if (value_temp >= -100 and value_temp <= 100): 
				error = 0

		if userentry_temp == 1:
			results_temp = ((value_temp - 32) * 5) / 9
			print('Results = %.2f' %results_temp + ' Celsius')
		elif userentry_temp == 2:
			results_temp = ((value_temp * 9) / 5) + 32
			print('Results = %.2f' %results_temp + ' Fahrenheit')
		elif userentry_temp == 3:
			results_temp = ((value_temp - 32) * 5) / 9	+ 273.15
			print('Results = %.2f' %results_temp + ' Kelvin')
		elif userentry_temp == 4:
			results_temp = value_temp + 273.15
			print('Results = %.2f' %results_temp + ' Kelvin')
		elif userentry_temp == 5:
			results_temp = ((value_temp - 273.15) * 9) / 5 + 32
			print('Results = %.2f' %results_temp + ' Fahrenheit')
		else:
			print("Does not exist")

class Surface_and_Area(Converter):
	def conversions(self):
		print("What unit do you want to convert?")
		print("Type 1 for square feet to square meters")
		print("Type 2 for square yards to square meters")
		print("Type 3 for square miles to square kilometers")
		print("Type 4 for square kilometers to square miles")
		print("Type 5 for hectares to acres")
		userentry_SF_A = int(sys.stdin.readline())
		print("Enter value")
		value_SF_A = float(sys.stdin.readline())

		if userentry_SF_A == 1:
			results_SF_A = value_SF_A * .0929
			print('Results = %.2f' %results_SF_A + 'square meters')
		elif userentry_SF_A == 2:
			results_SF_A = value_SF_A * .8361
			print('Results = %.2f' %results_SF_A + 'square meters')
		elif userentry_SF_A == 3:
			results_SF_A = value_SF_A * 2.5900
			print('Results = %.2f' %results_SF_A + 'square kilometers')
		elif userentry_SF_A == 4:
			results_SF_A = value_SF_A * .3861
			print('Results = %.2f' %results_SF_A + 'square miles')
		elif userentry_SF_A == 5:
			results_SF_A = value_SF_A * 2.4711
			print('Results = %.2f' %results_SF_A + 'square acres')
		else:
			print("Does not exist")
class Money(Converter):
	def conversions_Money(self):	
		class USA(Money):
			def cash(self):
				print("What unit would you like to convert?")
				print("Type 1 for pennies to cents")
				print("Type 2 for nickels to cents")
				print("Type 3 for dimes to cents")
				print("Type 4 for quarters to cents")
				print("Type 5 for half-dollars to cents")
				print("Type 6 for dollars to cents")
				userentry_money = int(sys.stdin.readline())
				print("Enter value")
				value_money = float(sys.stdin.readline())

				if userentry_money == 1:
					results_money = value_money * 1
					print('Results = %.0f' %results_money + ' cents')
				elif userentry_money == 2:
					results_money = value_money * 5 
					print('Results = %.0f' %results_money + ' cents')
				elif userentry_money == 3:
					results_money = value_money * 10
					print('Results = %.0f' %results_money + ' cents')
				elif userentry_money == 4:
					results_money = value_money * 25 
					print('Results = %.0f' %results_money + ' cents')
				elif userentry_money == 5:
					results_money = value_money * 50
					print('Results = %.0f' %results_money + ' cents')
				elif userentry_money == 6:
					results_money = value_money * 100 
					print('Results = %.0f' %results_money + ' cents')
					
				else:
					print("Does not exist")
		class INT(Money):
			def world(self):
				print("In what currency do you want your result")
				print("to be in?")
				print("")
				print("Type 1 for USD(United States Dollar)")
				print("Type 2 for EUR(Euro)")
				print("Type 3 for GBP(British Pound)")
				print("Type 4 for INR(Indian Rupee)")
				print("Type 5 for AUD(Australian Dollar)")
				print("Type 6 for CAD(Canadian Dollar)")
				print("Type 7 for SGD(Singapore Dollar)")
				print("Type 8 for JPY(Japanese Yen)") 
				money_topic = int(sys.stdin.readline())

				if money_topic == 1:
					class USD_M(INT):
						def america(self):
							print("Type 1 for EUR to USD")
							print("Type 2 for GBP to USD")
							print("Type 3 for INR to USD")
							print("Type 4 for AUD to USD")
							print("Type 5 for CAD to USD")
							print("Type 6 for SGD to USD")
							print("Type 7 for JPY to USD")
							usd_choice = int(sys.stdin.readline())
							print("Enter value")
							value_money = float(sys.stdin.readline())

							if usd_choice == 1:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=EUR&to=USD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif usd_choice == 2:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=GBP&to=USD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif usd_choice == 3:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=INR&to=USD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.3f' %results_money)
							elif usd_choice == 4:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=AUD&to=USD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])										
								print('Results = %.2f' %results_money)
							elif usd_choice == 5:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=CAD&to=USD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif usd_choice == 6:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=EUR&to=USD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif usd_choice == 7:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=JPY&to=USD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							else:
								print("")
					
					usb = USD_M()
					usb.america()				

				elif money_topic == 2:
					class EUR_M(INT):
						def belgium(self):
							print("Type 1 for USD to EUR")
							print("Type 2 for GBP to EUR")
							print("Type 3 for INR to EUR")
							print("Type 4 for AUD to EUR")
							print("Type 5 for CAD to EUR")
							print("Type 6 for SGD to EUR")
							print("Type 7 for JPY to EUR")
							eur_choice = int(sys.stdin.readline())
							print("Enter value")
							value_money = float(sys.stdin.readline())

							if eur_choice == 1:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=USD&to=EUR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif eur_choice == 2:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=GBP&to=EUR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif eur_choice == 3:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=INR&to=EUR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif eur_choice == 4:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=AUD&to=EUR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif eur_choice == 5:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=CAD&to=EUR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %2f' %results_money)			
							elif eur_choice == 6:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=SGD&to=EUR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif eur_choice == 7:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=JPY&to=EUR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							else:
								print("")
				
					europe = EUR_M()	
					europe.belgium()			

				elif money_topic == 3:
					class GBP_M(INT):
						def UK(self):
							print("Type 1 for USD to GBP")
							print("Type 2 for EUR to GBP")
							print("Type 3 for INR to GBP")
							print("Type 4 for AUD to GBP")
							print("Type 5 for CAD to GBP")
							print("Type 6 for SGD to GBP")
							print("Type 7 for JPY to GBP")
							GBP_choice = int(sys.stdin.readline())
							print("Enter value")
							value_money = float(sys.stdin.readline())

							if GBP_choice == 1:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=USD&to=GBP")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif GBP_choice == 2:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=EUR&to=GBP")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif GBP_choice == 3:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=INR&to=GBP")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif GBP_choice == 4:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=AUD&to=GBP")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif GBP_choice == 5:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=CAD&to=GBP")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif GBP_choice == 6:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=SGD&to=GBP")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif GBP_choice == 7:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=JPY&to=GBP")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							else:
								print("")

					wales = GBP_M()
					wales.UK()


				elif money_topic == 4:
					class INR_M(INT):
						def rajkot(self):
							print("Type 1 for USD to INR")
							print("Type 2 for EUR to INR")
							print("Type 3 for GBP to INR")
							print("Type 4 for AUD to INR")
							print("Type 5 for CAD to INR")
							print("Type 6 for SGD to INR")
							print("Type 7 for JPY to INR")
							INR_choice = int(sys.stdin.readline())
							print("Enter value")
							value_money = float(sys.stdin.readline())

							if INR_choice == 1:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=USD&to=INR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif INR_choice == 2:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=EUR&to=INR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif INR_choice == 3:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=GBP&to=INR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif INR_choice == 4:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=AUD&to=INR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif INR_choice == 5:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=CAD&to=INR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif INR_choice == 6:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=SGD&to=INR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif INR_choice == 7:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=JPY&to=INR")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)			
							else:
								print("")

					bombay = INR_M()			
					bombay.rajkot()

				
				elif money_topic == 5:
					class AUR_MN(INT):
						def nz(self):
							print("Type 1 for USD to AUD")
							print("Type 2 for EUR to AUD")
							print("Type 3 for GBP to AUD") 
							print("Type 4 for INR to AUD")
							print("Type 5 for CAD to AUD")
							print("Type 6 for SGD to AUD")
							print("Type 7 for JPY to AUD")
							AUR_choice = int(sys.stdin.readline())
							print("Enter value")
							value_money = float(sys.stdin.readline())

							if AUR_choice == 1:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=USD&to=AUD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif AUR_choice == 2:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=EUR&to=AUD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif AUR_choice == 3:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=GBP&to=AUD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif AUR_choice == 4:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=INR&to=AUD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif AUR_choice == 5:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=CAD&to=AUD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif AUR_choice == 6:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=SGD&to=AUD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif AUR_choice == 7:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=JPY&to=AUD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							else:
								print("")

					koala = AUR_MN()
					koala.nz()					
				
				elif money_topic == 6:
					class CAD_MN(INT):
						def piastre(self):
							print("Type 1 for USD to CAD")
							print("Type 2 for EUR to CAD")
							print("Type 3 for GBP to CAD")
							print("Type 4 for INR to CAD")
							print("Type 5 for AUD to CAD")
							print("Type 6 for SGD to CAD")
							print("Type 7 for JPY to CAD")
							CAD_choice = int(sys.stdin.readline())
							print("Enter value")
							value_money = float(sys.stdin.readline())

							if CAD_choice == 1:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=USD&to=CAD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif CAD_choice == 2:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=EUR&to=CAD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif CAD_choice == 3:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=GBP&to=CAD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif CAD_choice == 4:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=INR&to=CAD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif CAD_choice == 5:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=AUD&to=CAD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif CAD_choice == 6:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=SGD&to=CAD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif CAD_choice == 7:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=JPY&to=CAD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							else:
								print("")
					canada = CAD_MN()
					canada.piastre()			
				
				elif money_topic == 7:
					class SGD_MN(INT):
						def sing(self):
							print("Type 1 for USD to SGD")
							print("Type 2 for EUR to SGD")
							print("Type 3 for GBP to SGD")
							print("Type 4 for INR to SGD")
							print("Type 5 for AUD to SGD")
							print("Type 6 for CAD to SGD")
							print("Type 7 for JPY to SGD")
							SGD_choice = int(sys.stdin.readline())
							print("Enter value")
							value_money = float(sys.stdin.readline())

							if SGD_choice == 1:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=USD&to=SGD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif SGD_choice == 2:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=EUR&to=SGD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif SGD_choice == 3:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=GBP&to=SGD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif SGD_choice == 4:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=INR&to=SGD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif SGD_choice == 5:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=AUD&to=SGD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif SGD_choice == 6:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=CAD&to=SGD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif SGD_choice == 7:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=JPY&to=SGD")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							else:
								print("")
					singapore = SGD_MN()
					singapore.sing()


				elif money_topic == 8:
					class JPY(INT):
						def tokyo(self):
							print("Type 1 for USD to JPY")
							print("Type 2 for EUR to JPY")
							print("Type 3 for GBP to JPY")
							print("Type 4 for INR to JPY")
							print("Type 5 for AUD to JPY")
							print("Type 6 for CAD to JPY")
							print("Type 7 for SGD to JPY")
							JPY_choice = int(sys.stdin.readline())
							print("Enter value")
							value_money = float(sys.stdin.readline())

							if JPY_choice == 1:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=USD&to=JPY")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif JPY_choice == 2:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=EUR&to=JPY")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif JPY_choice == 3:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=GBP&to=JPY")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif JPY_choice == 4:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=INR&to=JPY")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif JPY_choice == 5:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=AUD&to=JPY")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif JPY_choice == 6:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=CAD&to=JPY")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							elif JPY_choice == 7:
								url = urllib.urlopen("http://rate-exchange.herokuapp.com/fetchRate?from=SGD&to=JPY")
								response = url.read()
								data = json.loads(response)
								results_money = value_money * float(data['Rate'])
								print('Results = %.2f' %results_money)
							else:
								print("")
					japan = JPY()
					japan.tokyo()
				else:
					print("")	


		print("What would you like to convert?")
		print("Type 1 for US Currency") 

		print("Type 2 for International Currency")
		money_way = int(sys.stdin.readline())

		if money_way == 1:
			us = USA() 
			us.cash()
		elif money_way == 2:
			wide = INT()	
			wide.world()
		else:
			print("hi")	

class Formulas(Converter):
	def strategies(self):
		print("Type 1 for force")
		print("Type 2 for acceleration")
		print("Type 3 for density")
		print("Type 4 for mass")
		print("Type 5 for circumference")
		print("Type 6 for distance")
		print("Type 7 for area of a circle")
		print("Type 8 for area of a parallelegram")
		print("Type 9 for area of a triangle")
		print("Type 10 for area of a trapezoid")
		print("Type 11 for volume of a cylinder")
		print("Type 12 for surface area of a cylinder")
		print("Type 13 for volume of a sphere")
		print("Type 14 for surface of a sphere")
		print("Type 15 volume of a cone")
		print("Type 16 for surface area of a cone")
		print("Type 17 for volume of a square pyramid")
		print("Type 18 for surface area of a square pyramid")
		print("Type 19 for free fall")
		print("")
		print("For all the questions you'll be asked,")
		print("do NOT label.")
		userentry_formulas = int(sys.stdin.readline())

		if userentry_formulas == 1:
		  	print("There are two ways to get force")
			print("Type 1 for Way 1")
			print("Type 2 for Way 2")
			way = int(sys.stdin.readline())
			if way == 1:
				print("What is your mass?")
				mass_force = float(sys.stdin.readline())
				print("What is your acceleration?")
				acceleration_force = float(sys.stdin.readline())
				results_formulas = mass_force * acceleration_force
				print('Results = %.2f' %results_formulas)
			elif way == 2:
				print("What is your mass?")
				mass_force_two = float(sys.stdin.readline())
				print("What is your velocity?")
				velocity_force = float(sys.stdin.readline())
				print("What is your time?")
				time_force = float(sys.stdin.readline())
				results_formulas = mass_force_two * velocity_force / time_force
				print('Results = %.2f' %results_formulas)
			else:
				print("Wrong number typed")	
		elif userentry_formulas == 2:
			print("What is your velocity?")
			velocity_acceleration = float(sys.stdin.readline())
			print("What is your time?")	
			time_acceleration = float(sys.stdin.readline())
			results_formulas = velocity_acceleration / time_acceleration
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 3:
			print("What is your mass?")
			mass_density = float(sys.stdin.readline())		
			print("What is your volume?")
			volume_density = float(sys.stdin.readline())
			results_formulas = mass_density / volume_density
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 4:
			print("What is your density?")
			density_mass = float(sys.stdin.readline())
			print("What is your volume?")
			volume_mass = float(sys.stdin.readline())
			results_formulas = density_mass * volume_mass
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 5:
			print("What is your radius?")
			radius_circumference = float(sys.stdin.readline())
			results_formulas = 2 * radius_circumference * math.pi	
			print('Results = %.14f' %results_formulas)
		elif userentry_formulas == 6:
			print("What is your speed?")
			s_d = float(sys.stdin.readline())
			print("What is your time?")
			t_d = float(sys.stdin.readline())
			results_formulas = s_d * t_d
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 7:
			print("What is your radius?")
			r_d = float(sys.stdin.readline())
			results_formulas = r_d * r_d * math.pi
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 8:
			print("What is the length of your base?")
			b_p = float(sys.stdin.readline())
			print("What is the length of your height?")
			h_p = float(sys.stdin.readline())
			results_formulas = b_p * h_p
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 9:
			print("What is the length of your base?")
			b_t = float(sys.stdin.readline())
			print("What is the length of your height?")
			h_t = float(sys.stdin.readline())
			results_formulas = b_t * h_t / 2
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 10:
			print("What is the length of your height?")
			h_t_z = float(sys.stdin.readline())
			print("What is the length of your Base 1?")
			b_o_t = float(sys.stdin.readline())
			print("What is the length of your Base 2?")
			b_t_t = float(sys.stdin.readline())
			results_formulas = h_t_z * (b_o_t + b_t_t) / 2
			print('Results = %.2f' %results_formulas) 
		elif userentry_formulas == 11:
			print("What is the length of your radius?")
			r_c = float(sys.stdin.readline())
			print("What is the length of your height?")
			h_c = float(sys.stdin.readline())
			results_formulas = r_c * r_c * h_c * math.pi
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 12:
			print("What is your radius?")
			r_s_c = float(sys.stdin.readline())
			print("What is your height?")
			h_s_c = float(sys.stdin.readline())
			results_formulas = r_s_c * h_s_c * math.pi * 2 + r_s_c * r_s_c * math.pi * 2
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 13:
			print("What is your radius?")
			r_s = float(sys.stdin.readline())
			results_formulas = r_s * r_s * r_s * math.pi * 4 / 3		
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 14:
			print("What is your radius?")
			r_s_s = float(sys.stdin.readline())
			results_formulas = r_s_s * r_s_s * 4 * math.pi
			print('Results = %.2f' %results_formulas)

		elif userentry_formulas == 15:
			print("What is your radius?")
			r_v_c = float(sys.stdin.readline())
			print("What is your height?")
			h_v_c = float(sys.stdin.readline())
			results_formulas = r_v_c * r_v_c * math.pi * h_v_c / 3
			print('Results = %.2f' %results_formulas) 
		elif userentry_formulas == 16:
			print("What is your height?")
			h_s_a_c = float(sys.stdin.readline())
			print("What is your radius?")
			r_s_a_c = float(sys.stdin.readline())
			results_formulas = math.pi * r_s_a_c * (r_s_a_c + (math.sqrt (math.pow(h_s_a_c, 2) + math.pow(r_s_a_c, 2)) ))
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 17:
			print("What is your base edge?")
			b_p = float(sys.stdin.readline())
			print("What is your height?")
			h_p = float(sys.stdin.readline())
			results_formulas = b_p * b_p * (h_p / 3)
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 18:
			print("What is your base edge?")
			b_e_p = float(sys.stdin.readline())
			print("What is your height?")
			h_s_p = float(sys.stdin.readline())
			results_formulas = (b_e_p * b_e_p) + 2 * b_e_p * math.sqrt((b_e_p * b_e_p) / 4 + (h_s_p * h_s_p))
			print('Results = %.2f' %results_formulas)
		elif userentry_formulas == 19:
			print("There are two ways to find free fall")
			print("Type 1 if you want to use Way 1")
			print("Type 2 if you want to use Way 2")
			free_way = int(sys.stdin.readline())

			if free_way == 1:
				print("What is your mass?")
				m_f = float(sys.stdin.readline())
				print("What is your volume?")
				v_f = float(sys.stdin.readline())
				print("What is your time?")
				t_f = float(sys.stdin.readline())
				results_formulas = m_f * v_f / t_f
				print('Results = %.2f' %results_formulas)
			elif free_way == 2:
				print("What is your mass?")	
				m_f_f = float(sys.stdin.readline())
				print("What is your gravity?")
				g_f = float(sys.stdin.readline())
				results_formulas = m_f_f * g_f
				print('Results = %.2f' %results_formulas)
		else:
			print("")				
class Main():
	def awesomeness(self): 
		print("")
		print("For all answers there will only be two decimals.")
		print("")
		print("What would you like to convert?")
		print("")
		print("Type 1 for Length and Distance")
		print("Type 2 for Surface and Area")
		print("Type 3 for Money")
		print("Type 4 for Weight and Mass")
		print("Type 5 for Temperature")
		print("Type 6 for Time")
		print("Type 7 for Speed and Velocity")
		print("Type 8 for Digital Storage")
		print("Type 9 for Fuel Consumption")
		print("Type 10 for Formulas")
		main_conversion = int(sys.stdin.readline())	

		if main_conversion == 1:
			length = Length_and_Distance()
			length.conversions()
		elif main_conversion == 2:
			area = Surface_and_Area()
			area.conversions()
		elif main_conversion == 3:
			cents = Money()
			cents.conversions_Money()
		elif main_conversion == 4:
			mass = Weight_and_Mass()
			mass.conversions()
		elif main_conversion == 5:
			temp = Temperature()
			temp.conversions()
		elif main_conversion == 6:
			clock = Time()
			clock.time_change()
		elif main_conversion == 7:
			fast = Speed_and_Velocity()	
			fast.conversions_speed()
		elif main_conversion == 8:
			storage = Digital_Storage()
			storage.conversions_storage()
		elif main_conversion == 9:
			gas = Fuel()
			gas.conversions_fuel()
		elif main_conversion == 10:
			form = Formulas()		
			form.strategies()
		else:
			print("Invalid entry.")


		print("Do you want to run again?")
		print("Type 1 for yes or 2 for no")
		answer = int(sys.stdin.readline())

		if answer == 1:
			restart = Main()
			restart.awesomeness()
		elif answer == 2:
			print("Bye")
		else:
			print("Bye")

main = Main()
main.awesomeness()
