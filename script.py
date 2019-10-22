import csv, os, shutil


with open('styles.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[3] == "Topwear":
            # print(row)
            try:
                shutil.move('./images/clothing/' + row[0] + ".jpg", './topwear/' + row[0] + ".jpg")
                line_count += 1
            except OSError as e:
                print(e)

