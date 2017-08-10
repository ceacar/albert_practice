#you have input data in the file "stock_input.data"

#read from this file
#calculate how many rows are in this data file
#calculate how many rows each symbol
#calculate average price of each symbol
#calculate total dollars have been trades
#calculate total dollar amount for each symbol
#calcualte each symbol's variance

#needed tip:
#open('file_path','r')
#readline
#rstrip, split 
#for k,v in the_dict.iteritems()




aaplstock = {'aapl1':[1.01,'100'], 'aapl2':[1.07,'100'], 'aapl3':[1.40,'100'] }
spystock = {'spy1':[0.85,'150'], 'spy2':[0.99,'150'], 'spy3':[0.55,'150']}
msftstock = {'msft1':[2.15,'99'], 'msft2':[2.39,'99'], 'msft3':[3.84,'99']}
print (aaplstock)
print (spystock)
print (msftstock)
print("rows in each symbol")
print(len(aaplstock))
print(len(spystock))
print(len(msftstock))
print("rows in data file")
print(len(aaplstock) + len(spystock) + len(msftstock))
#print(aaplstock['aapl1'][0])
#print(aaplstock['aapl2'][0])
#print(aaplstock['aapl3'][0])
print "average price of aapl", (aaplstock['aapl1'][0] + aaplstock['aapl2'][0] + aaplstock['aapl3'][0]) / 3
print "average price of spy", (spystock['spy1'][0] + spystock['spy2'][0] + spystock['spy3'][0]) / 3
print "average price of msft", (msftstock['msft1'][0] + msftstock['msft2'][0] + msftstock['msft3'][0]) / 3
print "total dollars traded of aapl", (aaplstock['aapl3'][0] - aaplstock['aapl1'][0]) * 100
print "total dollars traded of msft", (msftstock['msft3'][0] - msftstock['msft1'][0]) * 150
print "total dollars traded of spy", (spystock['spy3'][0] - spystock['spy1'][0]) * 99
print "total dollars amount of aapl", (aaplstock['aapl3'][0]) * 100
print "total dollars amount of spy", (spystock['spy3'][0]) * 150
print "total dollars amount of msft", (msftstock['msft3'][0]) * 99
aaplprice = [1.01, 1.07, 1.40]
m = sum(aaplprice) / len(aaplprice)
varResaapl = sum([(xi - m)**2 for xi in aaplprice]) / len(aaplprice)
print "variance of aapl", (varResaapl)
spyprice = [0.85, 0.99, 0.55]
m = sum(spyprice) / len(spyprice)
varResspy = sum([(xi - m)**2 for xi in spyprice]) / len(spyprice)
print "variance of spy", (varResspy)
msftprice = [2.15, 2.39, 3.84]
m = sum(msftprice) / len(msftprice)
varResmsft = sum([(xi - m)**2 for xi in msftprice]) / len(msftprice)
print "variance of msft", (varResmsft)
