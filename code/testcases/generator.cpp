#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int MINIGRIDSIZE = stoi(argv[1]);
	int SIZE = MINIGRIDSIZE*MINIGRIDSIZE;
	int arr[SIZE][SIZE];

	int n = stoi(argv[2]); //no. of missing entries to create in sudoku file

	string file_name = argv[3]; //file_name to be saved with, passed from iterator file

	for(int i = 1; i < SIZE+1; i++){
		arr[0][i-1] = i;
	}

	unsigned seed = 123;

	shuffle(arr[0], arr[0]+SIZE, default_random_engine(seed));

	for(int i = 1; i < SIZE; i++){
		for(int j = 0; j < SIZE; j++){
			if(i % MINIGRIDSIZE == 0){
				arr[i][j] = arr[i-MINIGRIDSIZE][(j+1)%SIZE];
			}
			else{
				arr[i][j] = arr[(i-1)][(j+MINIGRIDSIZE) % SIZE];
			}
		}
	}

	//this saves solution part of sudoku 
/*	ofstream myfile;  //solved sudoku
	myfile.open ("Original1.txt");

	for(int i = 0; i < SIZE; i++){
		for(int j = 0; j < SIZE; j++){
			myfile << arr[i][j] << "  ";
		}
		myfile << endl;
	}

	myfile.close();*/

	int i, j;

	for(long long int k = 0; k < n; k++){
		i = rand() % SIZE;
		j = rand() % SIZE;
		if(arr[i][j] != 0){
			arr[i][j] = 0;
		}
		else{
			n++;
		}
	}

	ofstream myfile1;  //sudoku to solve
	myfile1.open(file_name);

	for(int i = 0; i < SIZE; i++){
		for(int j = 0; j < SIZE; j++){
			myfile1 << arr[i][j] << "  ";
		}
		myfile1 << endl;
	}

	myfile1.close();


	return 0;
}