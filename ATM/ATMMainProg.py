#ATMMainProg.py---Main Program
from ATMMenu import menu
from ATMExcept import DepositError,WithdrawError,InSuffFundError
from ATMOperations import deposit,withdraw,balenq
while(True):
	try:
		menu()
		ch=int(input("\tEnter Ur Choice:"))
		match(ch):
			case 1:
						try:
							deposit()
						except ValueError:
							print("Don't try to Deposit Alnums,strs and symbols")
						except DepositError:
							print("Don't try to Deposit -Ve and Zero amount")
			case 2:
						try:
							withdraw()
						except ValueError:
							print("Don't try to Withdraw Alnums,strs and symbols")
						except WithdrawError:
							print("Don't try to Withdraw -Ve and Zero amount")
						except InSuffFundError:
							print("Ur Account does not have Suff Funds--Read Python Notes:")
			case 3:
						balenq()
			case 4:
						print("\tThx for using This Program")
						break
			case _:
				print("\tUr Selection of Operation is Wrong!!!--Try Again ")

	except ValueError:
		print("Don't Enter alnums,strs and symbols for Choice-Try gain")