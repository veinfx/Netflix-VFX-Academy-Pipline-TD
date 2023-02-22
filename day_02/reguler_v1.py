import re
memo = """asjeiflsiejfasddlkfjwifjaskdjfklwe
jfklasdfsaldkfjweifjlsdkjfklwefa
sdflkje010-235-1123dkjwfeiasdfwejflij010-12
3-4567aslkghjweoljldsajflk"""

aa = re.search('010\-\d{3,4}\-\d{4}', memo)
print(aa)