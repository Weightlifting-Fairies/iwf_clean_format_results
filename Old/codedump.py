import math

A_2020_M = 0.751945030
b_2020_M = 175.508
A_2020_W = 0.783497476
b_2020_W = 153.655

# Tian Tao
bweight_M = 95.75
total_M = 410

#
bweight_W = 63.4
total_W = 261


def men():
    X = math.log10(bweight_M/b_2020_M)
    A_Xsq = A_2020_M * X**2
    S_coeff = 10**(A_Xsq)
    S_total = total_M * S_coeff
    return S_total


def women():
    X = math.log10(bweight_W/b_2020_W)
    A_Xsq = A_2020_W * X**2
    S_coeff = 10**(A_Xsq)
    S_total = total_W * S_coeff
    return S_total


print(men())
print(women())


df = pd.read_csv('cleaned_results2019.csv', sep='\s*,\s*',
                 delimiter=',', encoding='ascii',
                 names=('pid', 'gender', 'rank', 'rank_s', 'rank_cj', 'name', 'born', 'nation', 'category', 'bweight',
                        'snatch1', 'snatch2', 'snatch3', 'snatch', 'jerk1', 'jerk2', 'jerk3', 'jerk', 'total', 'event', 'date'))


def men_sinclair(bwt, total):
    # Sinclair constants for 2017-2020
    A_2020_M = 0.751945030
    b_2020_M = 175.508

    # Calculation
    X = math.log10(bwt/b_2020_M)
    A_Xsq = A_2020_M * X**2
    S_coeff = 10**(A_Xsq)
    S_total = total * S_coeff
    return S_total


def women_sinclair(bwt, total):
    # Sinclair constants for 2017-2020
    A_2020_W = 0.783497476
    b_2020_W = 153.655

    # Calculation
    X = math.log10(bwt/b_2020_W)
    A_Xsq = A_2020_W * X**2
    S_coeff = 10**(A_Xsq)
    S_total = total * S_coeff
    return S_total


# Sinclair total calculation
if df['gender'] == 'M':
    men_sinclair(df['bweight'], df['total'])


if df['gender'] == 'W':
    women_sinclair(df['bweight'], df['total'])


#df.bweight.astype(float)
#df.total.astype(float)
#print (df['bweight'].astype(float))

#print(df.dtypes)


# if df['gender'] == 'W':
#   women_sinclair(df['bweight'], df['total'])


#lname = []
#fname = []


# for index, row in df.iterrows():
#print(index, row['gender'])

#print(df.loc[df['nation'].str.contains("CHN", case=False)])
#print(df.sort_values(['snatch', 'jerk'], ascending=[0, 0]))


#last = new_row[5].split()[0]
#first = new_row[5].split()[0]
# lname.append(last)
# fname.append(first)
# l.append(new_row)

# print(df.name)

# print(pd.DataFrame(l))
#print(l[0], len(l[0]))



#e = df['event']
#d = df['date'].astype(str)
#lst = [e[1]] + [d[1]]
#d_e = " ".join(lst)
#name_of_output_csv = d_e.replace(' ', '_').replace('.','_')

#Splits name and adds individual last and first name columns
#df[['lname','fname']] = df['name'].loc[df['name'].str.split().str.len() == 2].str.split(expand=True)
