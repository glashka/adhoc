
# coding: utf-8

# In[1]:

import urllib.request as urllib2

data = urllib2.urlopen('http://spark-public.s3.amazonaws.com/algo1/programming_prob/QuickSort.txt')
data = data.read()

numbers = [int(line.decode()) for line in data.split()]


# In[23]:

TEST_ARRAY = [3, 2, 8, 5, 1, 4, 7, 6]

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return

def set_pivot(a, start, end, pivot):
    if pivot == 'last':
        swap(a, start, end)
    elif pivot == 'median':
        median = a[(start + end) // 2]
        if median > a[start] and median < a[end] or median < a[start] and median > a[end]:
            swap(a, start, (start + end) // 2)
        elif a[end] > a[start] and a[end] < median or a[end] < a[start] and a[end] > median:
            swap(a, start, end)
    return a[start]
    
def split(a, start, end, pivot):
#    print(a[start:end + 1], pivot)
    if end - start <= 1:
        return
    p = set_pivot(a, start, end, pivot)
    i = start + 1
    for j in range(start + 1, end + 1):
        if a[j] < p:
            swap(a, i, j)
            i += 1
    swap(a, start, i - 1)
#    print(a, a[start:end + 1], i)
    split(a, start, i - 2, pivot)
    split(a, i, end, pivot)
    return

print(TEST_ARRAY)
split(TEST_ARRAY, 0, len(TEST_ARRAY) - 1, 'median')
print(TEST_ARRAY)


# In[ ]:




# In[ ]:



