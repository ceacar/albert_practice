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
stock_data = open('./stock_input.data','r')
#readline
first_line = stock_data.readline();
stock_dict = {}
for line in stock_data:
    lines = line.rstrip().split(" ")
    symbol = lines[0]
    price = lines [1]
    size = lines[2]
    if symbol in stock_dict:
        stock_dict[symbol].append((price,size))
    else:
        stock_dict[symbol] = [(price,size)]

print (stock_dict)
#rstrip, split 
#for k,v in stock_dict.iteritems():
    #print k
    #print v
    #for temp in v:
        #temp = (price, size)
        #print price
        #print size
avgstock = {}
def average(avgfun):
    #print "in average" + str(price)
    total = 0.0
    for temp in avgfun:
        # temp = (1.01,100)
        (price, size) = temp
        #price =1.01
        total = total + float(price) * float(size)
        #print price
    #print total
    return total / len(avgfun) / float(size)

tolstock = {}
def totalstock(tolst):
    total = 0.0
    for temp in tolst:
        (price, size) = temp
        total = total + (float(price) * float(size))
    #print total
    return total

#m = (totalaplprice) / len(aaplprice)
#varResaapl = sum([(xi - m)**2 for xi in aaplprice]) / len(aaplprice)
#mean
#sum((num1-mean)^2) / (n-1)
#print "variance of aapl", (varResaapl)

variancenum = {}

def variance(varfun):
    varamount = 0.0
    for temp in varfun:
        (price, size) = temp
        varamount = varamount = ((float(price) - float(avg)) ** 2)
    return varamount / (len(varfun) - 1)

#def cal_variance():

for k,v in stock_dict.iteritems():
    #import pdb
    #pdb.set_trace()
    avg = average(v)
    avgstock['v'] = avg
    print avg
    tol = totalstock(v)
    tolstock['v'] = tol
    print tol
    var = variance(v)
    variancenum['v'] = var
    print var


#function of calculating average
#write a for loop to calculate the average using below hint
#for k,v in the_dict.iteritems()
#aaplstock = {'aapl1':[1.01,'100'], 'aapl2':[1.07,'100'], 'aapl3':[1.40,'100'] }
#spystock = {'spy1':[0.85,'150'], 'spy2':[0.99,'150'], 'spy3':[0.55,'150']}
#msftstock = {'msft1':[2.15,'99'], 'msft2':[2.39,'99'], 'msft3':[3.84,'99']}
#print (aaplstock)
#print (spystock)
#print (msftstock)
#print("rows in each symbol")
#print(len(aaplstock))
#print(len(spystock))
#print(len(msftstock))
#print("rows in data file")
#print(len(aaplstock) + len(spystock) + len(msftstock))
#print(aaplstock['aapl1'][0])
#print(aaplstock['aapl2'][0])
#print(aaplstock['aapl3'][0])
#print "average price of aapl", (aaplstock['aapl1'][0] + aaplstock['aapl2'][0] + aaplstock['aapl3'][0]) / 3
#print "average price of spy", (spystock['spy1'][0] + spystock['spy2'][0] + spystock['spy3'][0]) / 3
#print "average price of msft", (msftstock['msft1'][0] + msftstock['msft2'][0] + msftstock['msft3'][0]) / 3
#print "total dollars traded of aapl", (aaplstock['aapl3'][0] - aaplstock['aapl1'][0]) * 100
#print "total dollars traded of msft", (msftstock['msft3'][0] - msftstock['msft1'][0]) * 150
#print "total dollars traded of spy", (spystock['spy3'][0] - spystock['spy1'][0]) * 99
#print "total dollars amount of aapl", (aaplstock['aapl3'][0]) * 100
#print "total dollars amount of spy", (spystock['spy3'][0]) * 150
#print "total dollars amount of msft", (msftstock['msft3'][0]) * 99
#aaplprice = [1.01, 1.07, 1.40]
#m = sum(aaplprice) / len(aaplprice)
#varResaapl = sum([(xi - m)**2 for xi in aaplprice]) / len(aaplprice)
#print "variance of aapl", (varResaapl)
#spyprice = [0.85, 0.99, 0.55]
#m = sum(spyprice) / len(spyprice)
#varResspy = sum([(xi - m)**2 for xi in spyprice]) / len(spyprice)
#print "variance of spy", (varResspy)
#msftprice = [2.15, 2.39, 3.84]
#m = sum(msftprice) / len(msftprice)
#varResmsft = sum([(xi - m)**2 for xi in msftprice]) / len(msftprice)
#print "variance of msft", (varResmsft)

