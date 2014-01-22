__author__ = 'changyunglin'

import csv, math
from collections import defaultdict
def genChunks(reader, chunksize=1000):
    '''
    Chunk generator. Take a CSV `reader` and yield
    `chunksize` sized slices.
    '''
    chunk = []
    for i, line in enumerate(reader):
        if (i % chunksize == 0 and i > 0):
            yield chunk
            del chunk[:]
        if line[14] == 'NA':
            pass
        else:
            chunk.append(line[14])
    yield chunk

def genFreqTable(chunck):
    '''
    generate freq table
    '''
    d = defaultdict(int)
    for row in chunck:
        d[row] += 1
    return d

def mergeFreqTables(A, B):
    '''
    merge freq table A, B into a new one
    '''
    for key in B.keys():
        if key in A.keys():
            A[key] = A[key] + B[key]
        else:
            A[key] = B[key]
    return A

def getMeanFromFreqTable(d):
    '''
    Input: frequency table - in dictionary structure
    Output: mean
    '''
    return sum(int(k)*v for k, v in d.items()) / float(sum(d.values()))

def getSTDFromFreqTable(d, mean):
    '''
    Input: frequency table - in dictionary structure
    Output: std
    '''
    numerator = sum( ((int(k) - mean ) ** 2) * v  for k, v in d.items())
    denominator = float(sum(d.values()))
    std = math.sqrt(numerator / denominator)
    return std

def getMedianFromFreqTable(d):
    '''
    Input: frequency table - in dictionary structure
    Output: median
    '''
    D = dict((int(k), v) for k, v in d.items())
    ds = sorted(D.items(), key=lambda t: t[0])
    # print("ds: ", ds)
    return getMedian(ds)

def getMedian(mylist):
    '''
    Input: a tuple list
    Putput: key in frequency table
    '''
    accu = 0
    total_element_num = sum(e[1] for e in mylist)
    median_index = total_element_num / float(2)
    if total_element_num % 2 == 1:  # when the number of observation is odd
        for i, v in enumerate(mylist):
            accu += v[1]
            if accu >= median_index:
                return mylist[i][0]
    else:
        for i, v in enumerate(mylist):
            accu += v[1]
            if accu == median_index:
                return (mylist[i][0] + mylist[i+1][0]) / float(2)
            elif accu > median_index:
                return mylist[i][0]

def main():
    fileName = '/Users/changyunglin/Dropbox/STA250/test_1.csv'
    freqTable = {}
    with open(fileName, 'rb') as csvFile:
        dataReader = csv.reader(csvFile, delimiter=',')
        print('Getting CSV...')
        next(dataReader, None)              # skip header
        print('Chunking...')
        for chunk in genChunks(dataReader):
            mergeFreqTables(freqTable, genFreqTable(chunk))
        print("Got freq-table ")

    # calculate mean
    mean = getMeanFromFreqTable(freqTable)
    print('mean: ', mean)
    # calculate std
    std = getSTDFromFreqTable(freqTable, mean)
    print("STD: ", std)
    # calculate median
    median = getMedianFromFreqTable(freqTable)
    print('median:', median)



if __name__ == "__main__":
    main()