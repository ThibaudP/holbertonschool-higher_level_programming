#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about a python list
 *
 * @p: pointer to a PyObject
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len = 0;
	int i = 0, size = 0;
	PyObject *obj;

	if (PyList_Check(p))
	{
		len = PyList_Size(p);
		size = ((PyListObject *)p)->allocated;

		printf("[*] Size of the Python List = %d\n", (int)len);
		printf("[*] Allocated = %d\n", size);

		for (i = 0; i < len; i++)
		{
			obj = PyList_GetItem(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
		}
	}
}
