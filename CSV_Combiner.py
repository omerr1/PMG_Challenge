import sys
import csv
import ntpath

def main():
    combined = []
    first_line = False
    
    #Looping through each file given in the arguments:
    for file in sys.argv[1:-1]:
        my_file = open(file, "r")
        csv_file = csv.reader(my_file, delimiter = ',')
        #For each row in said file we read it. And append it to our list. Skipping the first row.
        for row in csv_file:
            if(first_line):
                first_line = False
                continue
            #Attaching the filename the item is from.
            row.append(ntpath.basename(file).split('.')[0])
            combined.append(row)
        first_line = True

    #Writing to a CSV file.
    outputFile = open(sys.argv[-1], 'w', newline='')
    writer = csv.writer(outputFile)
    writer.writerows(combined)
    outputFile.close()
        

if __name__ == "__main__":
    main()

