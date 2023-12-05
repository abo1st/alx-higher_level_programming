#include <Python.h>

/**
 * print_python_list_info - This prints basic info about Python lists.
 * @p:This is a PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int sizez, allocz, iz;
	PyObject *obj;

	sizez = Py_SIZE(p);
	allocz = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sizez);
	printf("[*] Allocated = %d\n", allocz);

	for (iz = 0; iz < sizez; iz++)
	{
		printf("Element %d: ", iz);

		obj = PyList_GetItem(p, iz);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
