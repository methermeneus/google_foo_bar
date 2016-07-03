#ifndef ANSWER_H
#define ANSWER_H

#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#define PRECISION 5

typedef class Array {
	/* This sort of thing is easier with some functions built-in, so..
	 * .yeah. Anyway, I wanted to have something like Python's
	 * __str__(self), but that turned out to be too much of a hassle with
	 * C strings. Might have worked with C++ <string>s, but I wanted to
	 * keep things simple. */
	private:
		int length;
		double* array;
	public:
		Array (double*, int);
		int len (void);
		void sort (void);
		void swap (int, int);
		void str (void);
		void reverse (void);
		// Get Array[i]
		double operator [] (int i) const {
			return array[i];
		}
		// Set Array[i]
		double & operator[] (int i) {
			return array[i];
		}
} Array;

int answer (Array x, Array y) {
	x.sort();
	y.sort();
	double profile = (y[0] - x[0]) / y[0];
	int result = (int) 100 * profile;
	return result;
}

Array::Array (double* _array, int _length) {
	//double array[_length];
	array = (double*) malloc (_length * sizeof (double));
	for (int i (0); i < _length; ++i) {
		array[i] = _array[i];
	}
	length = _length;
}
int Array::len (void) {
	return length;
}

void Array::sort (void) {
	for (int i = 0; i < length; ++i) {
		for (int j = i + 1; j < length; ++j) {
			if (array[i] > array[j]) {
				swap (i, j);
			}
		}
	}
}

void Array::reverse (void) {
	int i (0), j (length - 1);
	while (i < j) {
		swap (i, j);
	}
}

void Array::swap (int x, int y) {
	// Would have liked to swap in place, but xor won't work with floats.
	float tmp = array[x];
	array[x] = array[y];
	array[y] = tmp;
}

void Array::str (void) {
	printf ("[");
	for (int i = 0; i < length; ++i) {
		printf ("%lf", array[i]);
		printf ("%s", (i == length - 1)?"]":", ");
	}
}

#endif
