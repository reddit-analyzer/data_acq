import csv

def csvSave(list_of_list, outfile):
    result_csv = open(outfile, "w")
    content = csv.writer(result_csv)#, delimiter = ',', quoting = csv.QUOTE_NONE, quotechar = '', lineterminator='\r\n')
    for item in list_of_list:
        item = [x.encode('utf8') for x in item]
        content.writerow(item)
    result_csv.close()
    return "Saved"