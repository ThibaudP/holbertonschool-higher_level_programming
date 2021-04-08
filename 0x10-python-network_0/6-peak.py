#/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak number of the list"""
    listint = list_of_integers
    size = len(listint)

    if listint == []:
        return None
    if size == 1:
        return listint[0]
    
    for i in range (1, size - 1):
        if listint[i] > listint[i + 1]:
            return listint[i]
    return listint[i + 1]
    