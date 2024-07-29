#ATMOperations.py<---File Name and Module Name
from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500.00 # Here bal is called Global variable
def  deposit():
	damt=float(input("\tEnter Ur Deposit Amount:")) # chance of getting ValueError
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("\tUR Account xxxxxxxx123 Credited with INR:{}".format(damt))
		print("\tBal in UR  Account xxxxxxxx123 after Deposit INR:{}".format(bal))

def  withdraw():
	global bal
	wamt=float(input("\tEnter Ur Withdraw Amount:")) # chance of getting ValueError
	if(wamt<=0):
		raise WithdrawError
	elif((wamt+500)>bal):
		raise InSuffFundError
	else:
		bal=bal-wamt
		print("\tUR Account xxxxxxxx123 Debitted with INR:{}".format(wamt))
		print("\tBal in UR  Account xxxxxxxx123 after Withdraw INR:{}".format(bal))

def  balenq():
	print("\tUr Bal in UR  Account xxxxxxxx123  INR:{}".format(bal))
