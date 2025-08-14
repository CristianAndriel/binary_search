from typing import List

def binary_search(sorted_list: List[int], target: int) -> int:
    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        mid = (start + end) // 2
        guess = sorted_list[mid]

        if guess == target:
            return mid
        elif guess < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1  # Fica fora do while

if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]
    target_number = 9

    result = binary_search(numbers, target_number)

    if result != -1:
        print(f"Elemento {target_number} encontrado no índice {result}.")
    else:
        print(f"Elemento {target_number} não encontrado.")
