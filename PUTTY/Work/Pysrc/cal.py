while True:
	a=int(input("정수입력: "))
	b=int(input("정수입력: "))
	op=input("연산입력: ")

	def cal(choice,a,b):
		if choice=="+":
			return a+b
		elif choice =="-":
			return a-b
		elif choice =="*":
			return a*b
		else:
			return a/b
	result = cal(op,a,b)
	print(result)