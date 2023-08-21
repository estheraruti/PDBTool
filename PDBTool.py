import pandas as pd

import sys

import math



colspecs = [(0, 6), (6, 11), (12, 16), (16, 17), (17, 20), (21, 22), (22, 26),

            (30, 38), (38, 46), (46, 54), (54, 60), (60, 66), (76, 78)]



names = ['ATOM', 'serial', 'name', 'altloc', 'resname', 'chainid', 'resseq',

         'x', 'y', 'z', 'occupancy', 'tempfactor', 'element']



# pdb = pd.read_fwf(sys.argv[1], names=names, colspecs=colspecs)

pdb = pd.read_fwf('6lu7.pdb', names=names, colspecs=colspecs)

data = pdb.loc[pdb['ATOM'] == 'ATOM']

print(data.head())

print('Welcome to the pdb program.')

print('To begin, try typing \'help\' for the list of valid commands.')

print('%d atoms recorded.',data.shape[0])

inp = ''



def atomfreq():

    df=data.groupby('name')['name'].count()

    print(df)

    return

    

def resfreq():

    df=data.groupby('resname')['resname'].count()

    print(df)

    return



def reslength(inputs):

    # print(inputs)

    df=data.loc[(data['resname'] == inputs[0]) & (data['chainid'] == inputs[1]) & (data['resseq'] == inputs[2])]

    print(df)

    max = 0

    for i in range(0,df.shape[0]-1):

        for j in range(i+1,df.shape[0]):

            len = math.sqrt(pow((float(df.iloc[i,7])-float(df.iloc[j,7])),2) + pow((float(df.iloc[i,8])-float(df.iloc[j,8])),2) + pow((float(df.iloc[i,9])-float(df.iloc[j,9])),2))

            if len > max:

                max = len

            # reslength SER A 1

    print(inputs[0] + ' with sequence number ' + inputs[1] + ' in chain ' + inputs[2] + ' has length ' + str(max) + ' angstroms. ')

    

def tempcheck(tem):

    print(tem)

    data['tempfactor'] =data['tempfactor'].astype(float)

    df1=data.loc[data['tempfactor'] < float(tem)]

    df2=data.loc[data['tempfactor'] == float(tem)]

    df3=data.loc[data['tempfactor'] > float(tem)]

    print('Temperature factor below ' + tem + ': ' + str(df1.shape[0]) + '/' + str(data.shape[0]))

    print('Temperature factor at ' + tem + ': ' + str(df2.shape[0]) + '/' + str(data.shape[0]))

    print('Temperature factor above ' + tem + ': ' + str(df3.shape[0]) + '/' + str(data.shape[0]))

    

def occupancy(tem):

    print(tem)

    data['occupancy'] =data['occupancy'].astype(float)

    df1=data.loc[data['occupancy'] < float(tem)]

    df2=data.loc[data['occupancy'] == float(tem)]

    df3=data.loc[data['occupancy'] > float(tem)]

    print('Temperature factor below ' + tem + ': ' + str(df1.shape[0]) + '/' + str(data.shape[0]))

    print('Temperature factor at ' + tem + ': ' + str(df2.shape[0]) + '/' + str(data.shape[0]))

    print('Temperature factor above ' + tem + ': ' + str(df3.shape[0]) + '/' + str(data.shape[0]))

    

while inp != 'quit':

    inp = input('Enter a command:')

    if inp == 'atomfreq':

        atomfreq()

    if inp == 'resfreq':

        resfreq()

    if 'reslength' in inp:

        text = inp.split()

        print('Usage: reslength <res_name> <chain_id> <seqnum>')

        if len(text) <4:

            print('Incorrect number of arguments to reslength. Please use the \'help\' command to learn more details about using reslength')

        if len(text[1]) != 3 | len(text[2]) !=1 | len(text[3]) !=1:

            print('The arguments are not provided in the correct order. Please use the \'help\' command to learn more details about using reslength')

        if len(text) == 4:

            try:

                val = int(text[3])

                reslength(text[1:4])

            except ValueError:

                print('The arguments are not provided to reslength in the correct format. Please use the \'help\' command to learn more details about using reslength')

    if 'tempcheck' in inp:

        text = inp.split()

        if len(text) > 2:

            print('Incorrect number of arguments to tempcheck')

        if len(text) < 2:

            print('Missing arguments to tempcheck')

        if len(text) == 2:

            try:

                val = float(text[1])

                if val < 0.0 or val > 100.0:

                    print('Usage: tempcheck <decimal> \n For details about the tempcheck command, use the \'help\' command.')

                else:

                    tempcheck(text[1])

            except ValueError:

                print('Usage: tempcheck <decimal> \n For details about the tempcheck command, use the \'help\' command.')

    if 'occupancy' in inp:

        text = inp.split()

        if len(text) > 2:

            print('Incorrect number of arguments to occupancy')

        if len(text) < 2:

            print('Missing arguments to occupancy')

        if len(text) == 2:

            try:

                val = float(text[1])

                if val < 0.0 or val > 1.0:

                    print('Usage: occupancy <decimal> \n For details about the occupancy command, use the \'help\' command.')

                else:

                    occupancy(text[1])

            except ValueError:

                print('Usage: tempcheck <decimal> \n For details about the occupancy command, use the \'help\' command.')
