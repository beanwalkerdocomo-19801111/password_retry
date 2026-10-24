password_1 = 'a123456'
i = 1
while i <= 3:
	customer_answer = input('請輸入密碼: ')
	if customer_answer != password_1:
		print('密碼錯誤, 還有',3-i, '次機會')
		i = i + 1
	else:
		print('登入成功')
		break
	