import os
path = '/home/cjw/Documents/iwf_data_clean/old_bw_2018_csv/'


directory = os.path.join("",path)
for root,dirs,files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            file = '/home/cjw/Documents/iwf_data_clean/old_bw_2018_csv/' + file
            print(file)
            f=open(file, 'r')
            print(f)
            #f=open(file, 'r')
            #print(f)
            #  perform calculation
            #f.close()