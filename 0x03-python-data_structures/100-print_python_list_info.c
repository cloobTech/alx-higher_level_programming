#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: parameter
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
    PyListObject *x;
    int i;

    x = (PyListObject *) p;
    printf("[*] Size of the Python List = %ld\n", x->ob_base.ob_size);
    printf("[*] Allocated = %ld\n", x->allocated);
    for (i = 0; i < x->ob_base.ob_size; i++)
        printf("Element %d: %s", i, x->ob_item[i]->ob_type->tp_name);
}
