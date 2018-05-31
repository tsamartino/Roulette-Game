# DOES NOT HANDLE 00 BETS

import random
import matplotlib.pyplot as plt
import pandas as pd

# Initial variables
spins = 1000

# Use an int to bet on individual numbers ("00" is -1)
# Use a str to bet on colors (i.e. "red", "black", or "green")

# bet = raw_input('Bet on a number (i.e. 7, 11, 33) or a color (i.e. "red", "black", or "green"): ')
# bankroll_start = raw_input('How much cash do you want to bring to the casino? $')

# Sets the bet - currently set to bet on black
bet = "black"
# Sets the starting bankroll
bankroll_start = 500
# Initializes running bankroll
bankroll = bankroll_start
# Initializes the max amount the bankroll reaches throughout the simulation - for reporting at end
bankroll_max = bankroll

# bet_amount_start = raw_input('What do you want the minimum bet to be set to? $')
# Specifies initial bet amount
bet_amount_start = 25
bet_amount = bet_amount_start
# Specifies the max bet allowed
bet_amount_max = 1000

# Initialize counters
counter = 0
wins = 0
losses = 0

# Empty dictionary to hold count of how many times an individual number was landed on
result = {}
history = {}

# Sets up roulette board and result dictionary to summarize number of times individual number hit
# "-1" is "00"
board = {}
for i in range(-1,37):
	if i == -1:
		board["00"] = "green"
		result["00"] = counter
	elif i == 0:
		board["0"] = "green"
		result["0"] = counter
	elif i % 2 == 0:
		board[str(i)] = "red"
		result[str(i)] = counter
	else:
		board[str(i)] = "black"
		result[str(i)] = counter

# Empty list to hold data to be displayed in DataTable
data = []

def spin():
	global counter
	global result
	global wins
	global losses
	global bankroll
	global bankroll_max
	global bet_amount
	global bet_amount_max
	# Empty string to hold win/lose status
	status = ""
	for spin in range(spins):
		# Empty list to hold data for each individual spin
		spin_data = []
		spin_data.append("$%s"%'{:,}'.format(bet_amount))
		counter += 1
		history[counter] = bet_amount
		num = random.randint(-1, 36)

		if num == -1:
			num = "00"
		# Increases the summary count for each individual number
		result[str(num)] += 1
		if bankroll == 0:
			# print
			# print("Game over :( at spin %s" % spin)
			# print
			break
		#Checks if there is enough cash to bet
		if bet_amount > bankroll:
			#Does the most we can bet
			bet_amount = bankroll
			# print("   -- Can't bet that much, new bet set to $%s - All of your bankroll!" % '{:,}'.format(bet_amount))
			# wait = raw_input("   -- Press $ to cash out or enter to continue. ")
			# if wait == "$":
			# 	print
			# 	print("Congrats. You won $%s!" % '{:,}'.format(bankroll))
			# 	print
			# 	break
			# print

		# print("Spin %s: %s - Bet: $%s on %s from a bankroll of $%s" % (counter, num, '{:,}'.format(bet_amount), bet, '{:,}'.format(bankroll),))

		if isinstance(bet, str):
			# Red/black bets
			if board[str(num)] == bet:
				wins += 1
				bankroll += (bet_amount * 2)
				bet_amount = bet_amount_start
				status = "**WON!!**"
			else:
				losses += 1
				bankroll += -bet_amount
				bet_amount = bet_amount * 2
				status = " -Lost-  "
		elif isinstance(bet, int):
			# Number bets
			# Checks for win or lose
			if num == bet:
				wins += 1
				bankroll += bet_amount * 35
				bet_amount = bet_amount_start
				status = "**WON**"
			else:
				losses += 1
				bankroll += -bet_amount
				bet_amount = bet_amount * 2
				status = "Lost."

		# print("   %s Bankroll now at $%s (Next bet: $%s)" % (status, '{:,}'.format(bankroll), '{:,}'.format(bet_amount)))
		# print("%s SPIN %s Bankroll: $%s Bet: $%s on %s - landed on %s" % (status, counter, '{:,}'.format(bankroll), '{:,}'.format(bet_amount), bet, num))
		if bet_amount > bet_amount_max:
			bet_amount = bet_amount_max
		if bankroll > bankroll_max:
			bankroll_max = bankroll

		# if status == "**WON!!**":
		# 	wait = input("Press enter to continue.")

		# Appends data points for each individual spin
		spin_data.append(bet)
		spin_data.append(num)
		spin_data.append(board[str(num)])
		spin_data.append(status)
		spin_data.append("$%s"%'{:,}'.format(bankroll))
		spin_data.append("$%s"%'{:,}'.format(bet_amount))
		# Adds individual data to master list
		data.append(spin_data)

def summary():
	# Summary
	print
	print("Bet was for $%s on %s" % (str(bet_amount_start), str(bet)))
	print("# of spins: %s" % str(counter))
	print("# of wins: %i" % wins)
	print("# of losses: %i" % losses)
	print("Starting cash: $%s" % str('{:,}'.format(bankroll_start)))
	print("$ left: $%s" % str('{:,}'.format(bankroll)))
	print
	print("Biggest bet: $%s" % '{:,}'.format(bet_amount_max))
	print("Highest bankroll: $%s" % '{:,}'.format(bankroll_max))
spin()
df = pd.DataFrame(data,columns=['Bet Amount','Bet', 'Landed On', 'Color', 'Status', 'Bankroll', 'Next Bet'])
print df
summary()
# for key in results:
# 	print("%s: %s" % (key, str(results[key])))




magnitude = 10 ** (len(str(counter)) - 2)
D = {}
for key in history:
	if key % magnitude == 0:
		D[key] = history[key]
	else:
		continue
# plt.bar(range(len(D)), list(D.values()), align='center')
# plt.xticks(range(len(D)), list(D.keys()))
# plt.show()
