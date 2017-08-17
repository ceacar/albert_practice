#dataset is named 2014-15_Graduation_Outcomes_-_Ethnicity.csv
#need results as follows:
    #graduation student total
    #graduation student every race percentage
    #total graduation student by school
    #total graduation student by race
    #graduation student by school percentage
    #graduation student by school by race percentage
    #overall average year it took for a student to graduate
    #average year it took to graduate by race
    #average year it took to graduate by school
    #graduation school by school by race by year percentage(want to see the shift of race percentage over the years)
import pprint
student_data = open('./2014-15_Graduation_Outcomes_-_Ethnicity.csv','r')
#student_data = open('./temp.csv','r')
first_line = student_data.readline();
# use for loop to get a dict
student_dict = {}
race_dict = {}
counter = 0
for line in student_data:
    lines = line.rstrip().split(",")
    counter = counter + 1
    code = lines [0]
    school = lines [1]
    years = lines [2]
    category = lines [3]
    ethnicity = lines [4]
    #if ethnicity not in ethnicity_set:
    #    print lines
    #    print ethnicity
    #    ethnicity_set.append(ethnicity)

    if  code in student_dict:
        student_dict[code].append((school,years,category,ethnicity))
    else:
        student_dict[code] = [(school,years,category,ethnicity)]
    if ethnicity in race_dict:
        race_dict[ethnicity].append((code,school,years,category))
    else:
        race_dict[ethnicity] = [(code,school,years,category)]

#pprint.pprint (student_dict)

#print sum(1 for _ in student_data)
print counter
        #(code,school,years,category) = temp

#race_dict: {'black':[()
#print len(race_dict[ethnicity])
percentagetemp = {}
#def percentage(percent):
    #'''{
    #    'black':[(),(),()] ,
    #    'white':[(),(),()] ,
    #}'''
    #num = 0
    #num = len(race_dict[ethnicity])
        #print num

res = {}
for k,v in race_dict.iteritems():
    #import pdb
    #pdb.set_trace()
    res[k] = len(v)
    print res[k]
