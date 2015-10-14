def main():
	print "If you haven't already entered it, the verification code is 241."
	print "1. Wires"
	print "2. The Button"
	print "3. Keypads"
	print "4. Simon Says"
	print "5. Who's on First"
	print "6. Memory"
	print "7. Morse Code"
	print "8. Complicated Wires"
	print "9. Wire Sequences"
	print "10. Mazes"
	print "11. Passwords"
	print "12. Venting Gas"
	print "13. Capacitator Discharge"
	print "14. Knobs"

	answer = raw_input("Enter the number of the module that you are currently working on.")

	program(answer)

def program(number):
	if number == 1:
		wires()
	elif number == 2:
		theButton()
	elif number = 3:
		keypads()
	elif number == 4:
		simonSays()
	elif number == 5:
		whosOnFirst()
	elif number == 6:
		memory()
	elif number == 7:
		morseCode()
	elif number == 8:
		complicatedWires()
	elif number == 9:
		wireSequences()
	elif number == 10:
		mazes()
	elif number == 11:
		passwords()
	elif number == 12:
		ventingGas()
	elif number == 13:
		capacitatorDischarge()
	elif number == 14:
		knobs()

def complicatedWires():
	red = raw_input("Is the wire red? Enter Y/N.")
	blue = raw_input("Is the wire blue? Enter Y/N.")
	star = raw_input("Is there a star symbol? Enter Y/N.")
	LED = raw_input("Is the LED on? Enter Y/N.")

	if red == 

if __name__ == '__main__':
	main()