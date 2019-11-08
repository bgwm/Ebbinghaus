import datetime

'For Programming Code Review'
'''print(filter(lambda y:
	y>0, 
	map(lambda x:
		(datetime.date.today() - datetime.date(2019,10,10)).days - x, 
		[0,1,3,7,14,29,59,119.239])
     )
)
'''
out = list(map(lambda x:(datetime.date.today() - datetime.date(2019,10,10)).days - x, [0,1,3,7,14,29,59,119.239]))

print(out)


	
