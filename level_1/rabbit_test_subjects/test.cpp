#include <cstdio>
#include "./solution.cpp"

char* arraystr (Array);

int main (int argc, char** argv) {

	double y1array[] = {1.0};
	double x1array[] = {1.0};
	Array y1 (y1array, 1);
	Array x1 (x1array, 1);
	int ans1 = 0;
	int result1 = answer (y1, x1);
	int test1 = (result1 == ans1);
	
	double y2array[] = {2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002};
	double x2array[] = {23.0, 150.0, 1024.0, 34868.0};

	Array y2 (y2array, 4);
	Array x2 (x2array, 4);
	int ans2 = 90;
	int result2 = answer (y2, x2);
	int test2 = (result2 == ans2);
	
	printf ("Test 1:\nInput ");
	y1.str();
	printf (", ");
	x1.str();
	printf (" expected answer %d.\n", ans1);
	printf ("Result %d\n", result1);
	printf ("Test 1 %s!\n", test1?"passed":"failed");
	
	printf ("\n\n");
	printf ("Test 2:\nInput ");
	y2.str();
	printf (", ");
	x2.str();
	printf (" expected answer %d.\n", ans2);
	printf ("Result %d\n", result2);
	printf ("Test 2 %s!\n", test2?"passed":"failed");
	
	return 0;
}

