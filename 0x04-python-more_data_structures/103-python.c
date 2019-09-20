#include <Python.h>
#include <stdio.h>
/**
 * print_python_bytes - prints some basic info about Python bytes type
 * @p: bytes object
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int i, limit;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", Py_SIZE(p));
	printf("  trying string: %s\n", str);

	if (Py_SIZE(p) >= 10)
		limit = 10;
	else
		limit = Py_SIZE(p) + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	}

	printf("\n");
}

/**
 * print_python_list - prints some basic info about Python lists
 * @p: list
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	PyObject *obj;
	long int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		obj = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPEN(obj)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}