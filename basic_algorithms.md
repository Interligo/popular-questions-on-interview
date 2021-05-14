### Базовые алгоритмы

***

### Сортировка:

* Пузырьковая сортировка - выполняет итерации по списку, сравнивая элементы попарно и меняя их местами. Самый медленный из всех алгоритмов. 

Временная сложность — O(n²), из-за которого алгоритм подходит только для небольшого объёма данных.

```python
def bubble_sort(nums):
    swapped = True
    
    while swapped:
        swapped = False        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
```

* Сортировка выборкой - сегментирует список на две части: отсортированную и неотсортированную. Наименьший элемент удаляется из второго списка и добавляется в первый.

```python
def selection_sort(nums):    
    for i in range(len(nums)):        
        lowest_value_index = i        
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j        
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
```


* Сортировка вставками - сегментирует список на две части: отсортированную и неотсортированную. 
Алгоритм перебирает второй сегмент и вставляет текущий элемент в правильную позицию первого сегмента. 
Выполняет меньше сравнений, чем сортировка выборкой и в реальности производительнее.

```python
def insertion_sort(nums):  
    for i in range(1, len(nums)):
        item_to_insert = nums[i]        
        j = i - 1    
        
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1       
            
        nums[j + 1] = item_to_insert
```

* Пирамидальная сортировка (куча) - сегментирует список на две части: отсортированную и неотсортированную. 
Алгоритм преобразует второй сегмент списка в структуру данных «куча» (heap), чтобы можно было эффективно определить самый большой элемент.

```python
def heapify(nums, heap_size, root_index):  
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]        
        heapify(nums, heap_size, largest)

def heap_sort(nums):  
    n = len(nums)
    
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
```

* Сортировка слиянием - разбивает список на две части, каждую из них он разбивает ещё на две и т. д. 
Список разбивается пополам, пока не останутся единичные элементы. Массив из одного элемента считается упорядоченным. 
Соседние элементы сравниваются и соединяются вместе. Это происходит до тех пор, пока не получится полный отсортированный список.

```python
def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:            
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1            
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):      
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)
```

* Быстрая сортировка - Массив разделяется на две части по разные стороны от опорного элемента. 
В процессе сортировки элементы меньше опорного помещаются перед ним, а равные или большие — позади. 
Почти в два раза быстрее, чем сортировка слиянием, и не требуется дополнительное место для результирующего массива.

```python
def partition(nums, low, high):      
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):      
    def _quick_sort(items, low, high):
        if low < high:            
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
```

***

### Поиск:

* Линейный поиск - перебрает массив и возвращает индекс первого вхождения элемента, когда он найден.

```python
def linear_search(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1
```

* Бинарный поиск - быстрее, чем линейный поиск, но требует, чтобы массив был отсортирован перед выполнением алгоритма.

```python
def binary_search_iterative(list, item):    
    low = 0
    high = len(list) - 1

    while low <= high:      
      mid = (low + high) // 2
      guess = list[mid]
      
      if guess == item:
        return mid
      
      if guess > item:
        high = mid - 1      
      else:
        low = mid + 1
    
    return None
```

* Работа с деревьями (обход в ширину и глубину).

Деревья — это разновидность графа, их обход, иначе называемый поиск по дереву, является видом обхода графа.

```python
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : [],
  'D' : [],
  'E' : []
}
```

**BFS (поиск в ширину, "слепой" поиск)** - поиск по всем узлам дерева, создавая широкую сеть. 
Это означает, что сначала мы обходим один уровень потомков и лишь затем переходим к последующему уровню уже их потомков.
BFS требует больше памяти. 

```python
visited = []  
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
        
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
```

**DFS (поиск в глубину)** - посещаем самый углублённый узел, затем идём назад и следуем другим путём, достигая другого конечного узла. 
Этот поиск легко реализовать через рекурсию, но он не всегда находит ближайший путь к исткомому узлу.

```python
visited = set() 

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
```

***

* О-большое при оценке сложности алгоритмов.

Нотация О большое является одним из самых фундаментальных инструментов анализа сложности алгоритма и описывает верхнюю границу сложности.

Сложность:

1. **O(1)** - линейная сложность (постоянная по времени);

2. **O(log(n))** - логарифмическая сложность;

3. **O(n⁵)** - квадратичная сложность. Сложность многочленов увеличивается с ростом степени.

***
