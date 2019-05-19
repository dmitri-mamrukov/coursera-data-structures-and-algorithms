from heap import BinHeap, HeapMode

def sort_with_min_bin_heap(data):
    heap = BinHeap(HeapMode.min)
    for datum in data:
        heap.insert(datum)
    for i in range(len(data)):
        data[i] = heap.extract()

def sort_with_max_bin_heap(data):
    heap = BinHeap(HeapMode.max)
    for datum in data:
        heap.insert(datum)
    for i in range(len(data) - 1, -1, -1):
        data[i] = heap.extract()

def partially_sort(data, k):
    """
    Returns the last k elements of a sorted version of the data.
    """
    if k < 0 or k > len(data):
        raise ValueError('The k parameter must be within the data range.')

    heap = BinHeap(HeapMode.max)
    heap.build(data)

    result = []
    for i in range(0, k):
        result.insert(0, heap.extract())

    return result
