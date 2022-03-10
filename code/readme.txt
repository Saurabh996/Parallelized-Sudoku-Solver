["code" folder]
####################

Syntax for running code.cpp
	>>  g++ -fopenmp -o m.exe code.cpp
	>> ./m.exe (No_of_threads) (sudoku_file)
	>> for eg: ./m.exe 8 testcases/25x25_hard.txt

For timing study:
	python script named it_plot.py has been written, which updates macro(#define MINIGRIDSIZE 5) for every iteration, compiles it and then run code.cpp file for different combinations
	>> to run the same: python3 it_plot.py
	

["code>>testcases" folder]
###############################

For generating sudoku sample, file named generator.cpp has been written, which takes 3 arguments: 1) MINIGRIDSIZE 2) n(no. of missing entries) 3) file name(to be saved with). These arguments are passed from iterator file(it_generator.py)
	>> syntax: g++ -o m.exe generator.cpp
	>> ./m.exe {} {} {}'.format(size[i], missing_entries, file_name)

For generating bunch of difft. testcases, it_generator.py has been written which takes no.of missing entries(for instance "missing_entries = 60") to be created in sudoku file, and creates sudoku puzzle with asked entries for three difft. sudoku sizes: 9x9, 16*16, 25*25 in .txt format
	To run the script: python3 it_generator.py