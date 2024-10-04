from mergesort import merge_sort
from insertionsort import insertion_sort
from timsortrecursive import tim_sort_recursive
from timsortiterative import tim_sort_iterative

algorithms = {
    "Вставками": insertion_sort,
    "Злиттям": merge_sort,
    "Рекурсивний TimSort": tim_sort_recursive,
    "Ітеративний TimSort": tim_sort_iterative,
    "Вбудованою функцією sorted": sorted
}