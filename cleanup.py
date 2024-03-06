import csv
with open('data/daily_sales_data_2.csv', newline='') as readfile:
    with open('data/daily_sales_data_2_clean.csv','w', newline='') as writefile:
        csvreader = csv.reader(readfile, delimiter=',')
        csvwriter = csv.writer(writefile, delimiter=',')
        for row in csvreader:
            if(row[0] == "pink morsel"):
                csvwriter.writerow(row)   
