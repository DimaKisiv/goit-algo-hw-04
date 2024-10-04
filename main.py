
import timeit
from algorithms import algorithms
from arrays import arrays


def main():
    for array_name, array in arrays.items():
        print(f"\n{array_name}:")
        for alg_name, func in algorithms.items():    
            try:
                result = timeit.timeit(lambda: func(array.copy()), number=10) 
                print(f"\t {alg_name} -> {result:.7f}")
            except Exception as err:
                print(f"\t {alg_name} -> {err}")
        time_sort = timeit.timeit(lambda: array.copy().sort(), number=10)
        print(f"\t Вбудованою функцією sort -> {time_sort:.7f}")
        

if __name__ == "__main__":
    main()