#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	PyObject *item = NULL;
	long int i;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
