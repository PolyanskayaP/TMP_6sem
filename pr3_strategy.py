
class SortingStrategy:
    def sort(self, data):
        pass

class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        return sorted(data)

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class MergeSortStrategy(SortingStrategy):
    def sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.sort(left_half)
            self.sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1

        return data

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorter = Sorter(QuickSortStrategy())
sorted_data = sorter.sort(data)
print(sorted_data)

sorter.set_strategy(BubbleSortStrategy())
sorted_data = sorter.sort(data)
print(sorted_data)

sorter.set_strategy(MergeSortStrategy())
sorted_data = sorter.sort(data)
print(sorted_data)


# В этом примере класс `SortingStrategy` является абстрактным классом стратегии, 
# а его подклассы `QuickSortStrategy`, `BubbleSortStrategy` и `MergeSortStrategy` 
# представляют конкретные стратегии сортировки. Класс `Sorter` является контекстом, 
# который использует стратегию для сортировки данных. В методе `set_strategy` можно 
# изменить текущую стратегию сортировки.