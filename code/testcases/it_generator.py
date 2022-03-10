import subprocess
import os

cmd = 'g++ -o m.exe generator.cpp' 
p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE).stdout

size = [3,4,5]; #mini-grid size
# size = [4]

missing_entries = 150;

for i in range(len(size)):
	sudoku_size = size[i]*size[i]
	file_name = '{}x{}_{}.txt'.format(sudoku_size, sudoku_size, missing_entries)
	cmd = './m.exe {} {} {}'.format(size[i], missing_entries, file_name)
	p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE).stdout

print("All test_cases generated!!")