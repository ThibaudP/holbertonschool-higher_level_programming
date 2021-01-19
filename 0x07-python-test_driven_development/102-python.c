#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - prints a python string in C
 *
 * @p: PyUnicode Object
 */

void print_python_string(PyObject *p)
{
	fflush(stdout);

	printf("[.] string object info\n");
	if PyUnicode_CheckExact(p)
	{
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %zd\n", PyUnicode_GetLength(p));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}