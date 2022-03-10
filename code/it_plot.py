import subprocess
import os
import time

size = [3, 4, 4, 4, 5, 5, 5, 5, 5]; #mini-grid size
#size = [5]; #mini-grid size

# size = [2**i for i in range(1,5)]; #mini-grid size
# size = [i for i in range(4,9)]

threads = [i for i in range(1,17)]

etime = [[] for i in range(len(size))]
speedup = [[] for i in range(len(size))]

rep = 5 #take average of these repetitions

sudoku_file = ["9x9_60.txt", "16x16_120.txt", "16x16_150.txt","16x16_200.txt", "25*25_250.txt", "25*25_300.txt", "25*25_350.txt", "25*25_400.txt", "25*25_hard.txt"]
# sudoku_file = ["25*25_hard.txt"]


for i in range(len(size)):
	sudoku_size = size[i]*size[i]
	# file_name = '{}x{}_{}_generated.txt'.format(sudoku_size, sudoku_size, missing_entries)
	print("running for sudoku size: {}x{}".format(sudoku_size, sudoku_size))
	for j in range(len(threads)):
		###update sudoku_size.h###
		f = open("minigrid.h", "w") #overwrite
		f.write("#define MINIGRIDSIZE {}\n".format(size[i]))
		f.close()

		#compile
		cmd = 'g++ -fopenmp -o m.exe code.cpp' 
		p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE).stdout
		time.sleep(3)

		arr = []
		for k in range(rep):
			#run
			cmd = './m.exe {} testcases/{}'.format(threads[j], sudoku_file[i])
			# cmd = './m.exe {} testcases/{}'.format(threads[j], file_name)
			p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE).stdout

			#output 
			output = str(p.read())
			#print(output[2:-3])
			print(output[2:-3])
			arr.append(float(output[2:-3]))
			time.sleep(1)

		val = round((sum(arr)/len(arr)), 6) 
		etime[i].append(val)
		print(cmd)
		print('avg_time: {}'.format(val))



import matplotlib.pyplot as plt 

#Execution time graph
plt.figure()
for i in range(len(size)):
	sudoku_size = size[i]*size[i]
	# file_name = '{}x{}_{}'.format(sudoku_size, sudoku_size, missing_entries)
	plt.plot(threads, etime[i], label = sudoku_file[i], marker = "o")
plt.legend()
plt.title("Time versus number of threads for different sudoku size")
plt.xlabel("Number of threads")
plt.ylabel("Execution Time(second)")
plt.savefig("Time_plot_updated.png")


#SpeedUp graph
for i in range(len(size)):
	for j in range(len(threads)):
		val = round(etime[i][0]/etime[i][j], 6)
		speedup[i].append(val)


plt.figure()
for i in range(len(size)):
	sudoku_size = size[i]*size[i]
	# file_name = '{}x{}_{}'.format(sudoku_size, sudoku_size, missing_entries)
	# plt.plot(threads, speedup[i], label = file_name, marker = "o")
	plt.plot(threads, speedup[i], label = sudoku_file[i], marker = "o")

plt.legend()
plt.title("SpeedUp versus number of threads for different sudoku size")
plt.xlabel("Number of threads")
plt.ylabel("SppedUp")
plt.savefig("SpeedUp_graph_{}.png".format("Final"))

print("All test_cases run successfully!!")