# -*- coding: utf-8 -*-
"""수행시간비교.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ztifefe9ZPIck4O9kEbtjsrfOvbSYCq-
"""

import time, random
n = int(input())

def compute_e_ver1(n):
	sum1 = 0
	fac = 1
	for i in range(1, n+1):
		sum1 += 1/fac
		for j in range(1, i):
			fac *= j
	return sum1
	# code for O(n^2)-time version
def compute_e_ver2(n):
	sum2 = 0
	fac = 1
	for i in range(1, n+1):
		fac *= i
		sum2 += 1/fac
	return sum2
	# code for O(n)-time version
s = time.process_time()
compute_e_ver1(n)
e = time.process_time()
print("O(n^2)의 수행시간 = ",e-s)

s = time.process_time()
compute_e_ver2(n)
e = time.process_time()
print("O(n)의 수행시간 = ",e-s)