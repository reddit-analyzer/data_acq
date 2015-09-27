import os
import glob

#puts all csvs together, threads to one csv, comments to one csv
def csvGlue(dir_csv_files):
    try:
        path = os.chdir(dir_csv_files)
    except:
        return "No such directory"

    #test if all files are csv in that directory
    csv_files = [file for file in glob.glob('*csv')]
    all_files = [file for file in glob.glob('*')]
    if len(csv_files) < len(all_files):
        return "Not all files are csv, please remove them."

    #separate into thread csvs and comments csvs
    thread_csv_list = []
    comments_csv_list = []
    for item in csv_files:
        if 'thread' in item:
            thread_csv_list.append(item)
        else:
            comments_csv_list.append(item)

    csv_writer(thread_csv_list, 'all_thread.csv')
    csv_writer(comments_csv_list, 'all_comments.csv')
    return "All CSV files glued and written"

def csv_writer(csv_list, outfile_name):
    with open(outfile_name, 'a') as finalFile:
        for file in csv_list:
            f = open(file)
            for line in f:
                finalFile.write(line)
    return "CSV file written"