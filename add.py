import csv
with open('data/d.csv', newline='') as readfile:
    with open('data/d1.csv','w', newline='') as writefile:
        csvreader = csv.reader(readfile, delimiter=',')
        csvwriter = csv.writer(writefile, delimiter=',')
        for row in csvreader:
            if(row[0] == "pink morsel"):
                row.append( str(float(row[1][1:]) * float(row[2])) )
                csvwriter.writerow(row)   
