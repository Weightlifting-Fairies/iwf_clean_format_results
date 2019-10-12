import csv
import os
# Use this module when downloading IWF results via the export button on the bottom of results page
# This could be useful when opening the csv file with Microsft Excel. Use Libre Office to get the formatted file.
# Should've used panda

path = '/home/cjw/Documents/iwf_data_clean/old_bw_2018_csv/'

def read():
    """Reads and cleans up the raw data"""
    directory = os.path.join("", path)
    for root,dirs,files in os.walk(directory):
        l = []
        for file in files:
            #file = path + file
            file = '/home/cjw/Documents/iwf_data_clean/old_bw_2018_csv/' + file

            if file.endswith(".csv"):
                f=open(file, 'r')
                lines = f.readlines()
                for line in lines[1:]:
                    row = line.translate({ord(c): None for c in '"=-'})  # deletes ", =, and -
                    new_row = row.strip().split(';')
                    l.append(new_row)
                
        return l


def output(r):
    """Output the data"""
    outfile = open("cleaned_old_bw_2018.csv", "w")
    header = ['pid', 'gender', 'rank', 'rank_s', 'rank_cj', 'name', 'born', 'nation', 'category', 'bweight',
              'snatch1', 'snatch2', 'snatch3', 'snatch', 'jerk1', 'jerk2', 'jerk3', 'jerk', 'total', 'event', 'date']
    header_str = '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(
        header[0], header[1], header[2], header[3], header[4], header[5], header[6], header[7], header[8], header[9], header[10],
        header[11], header[12], header[13], header[14], header[15], header[16], header[17], header[18], header[19], header[20])
    outfile.write(header_str)
    outfile.write('\n')

    for lifter in r:
        row_string = '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(
            lifter[0], lifter[1], lifter[2], lifter[3], lifter[4], lifter[5], lifter[6], lifter[7], lifter[8], lifter[9], lifter[10],
            lifter[11], lifter[12], lifter[13], lifter[14], lifter[15], lifter[16], lifter[17], lifter[18], lifter[19], lifter[20])
        outfile.write(row_string)
        outfile.write('\n')
    outfile.close()


if __name__ == "__main__":
    results = read()
    print(results)
    output(results)
