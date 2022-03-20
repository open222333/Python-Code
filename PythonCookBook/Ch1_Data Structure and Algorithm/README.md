# 資料結構與演算法

1.1 將一個序列拆分給個別變數
* 問題：
有一個Ｎ個元素的元組(tuple)或序列(sequen),拆分給Ｎ個變數
* 解法：
賦值(assignment operation) 拆分給變數
* 討論：
拆分(unpacking)可用在任何可迭代物件(iterable)：元組 串列 字串 檔案 迭代器(iterators) 產生器(generators)
用了就丟的變數名稱(throwaway variable name)：_，須確保所挑的名稱沒用在其他地方

1.2 拆解一個任意長度的可迭代物件之元素
* 問題：
解開一個可迭代物件(iterable)取出Ｎ個元素，但這個可疊愛物件的長度可能比Ｎ個元素還多，導致「要拆解的值太多(too many values to unpack)」的例外
* 解法：
星號運算式(star expressions)
* 討論：
延伸式的可迭代物件(extended iterable unpacking)動作專門用來拆解任意長度或長度未知的可迭代物件(iterables)

1.3 留下最後Ｎ個項目
* 問題：
在迭代(iteration)或某種處理動作的過程中留下最近項目的少量歷程紀錄(limited history)
* 解法：
collections.deque適合用來製作這種少量的歷程紀錄。
* 討論：
搜尋特定項目(items)時，通常使用yield的產生器函示(generator function)

1.4 找出最大或最小的Ｎ個項目
* 問題：
找出一個群集(collection)中最大或最小的Ｎ個項目做成一個串列(list)
* 解法：
heapq模組 nlargest() nsmallest()
* 討論：
heapq運作方式：先將資料轉為一個串列，項目以堆積(heap)的形式安置的。
若找單一最大最小 使用max() min()
若Ｎ的大小接近該群集 使用sorted(items)[:N] sorted(item)[-N:]

1.5 實作一個優先序佇列
* 問題：
實作一個佇列(queue)，依據給定的優先序(priority)排序項目，每次取出(pop)都回傳最高優先序的項目
* 解法：
用heapq模組實作簡單的優先序佇列
* 討論：
heapq.heappush() 插入項目
heapq.heappop() 回傳那個最小的項目
佇列由(-priority, index, item)這種形式的元組(tuples)，取負的priority使項目從最高優先序排到最低優先序
Item實體(instances)是無法比較。
(priority, item)元組，可比較，若有相同優先序就會無法比較。
(priority, index, item)可以比較且因元組不會有相同的index，不會有無法比較的問題。
若要將此佇列用在執行緒(threads)之間的通訊，得加入適當的鎖定(locking)與訊號(signaling)機制。

1.6 在一個字典中將鍵值映射至多個值
* 問題：
製作一個字典，將各個鍵值(keys)映射到一個以上的值(multidict)
* 解法：
將值使用串列或集合儲存。
串列：保留插入順序
集合：移除重複項目
可使用collections模組中的defaultdict：自動初始化第一個值，可專注在值的新增。會自動建立字典條目(dictionary entries)
若不想要自動建立字典條目，可使用setdefult()
* 討論：
使程式碼更簡潔

1.7 維持字典的秩序
* 問題：
建立一個字典(dictionary)，且在迭代(iterating)或序列化(serializing)時，控制其中項目的次序。
* 解法：
collection模組的OrderedDict:在迭代時完全保留資料插入順序。
若想精準控制JSON編碼中欄位出現的順序，可先建立一個裝有資料的OrderedDict。
* 討論：
OrderedDict在內部維護一個雙向鏈結串列(doubly linked list)，依照插入的次序來安排鍵值的次序。
一個OrderedDict的大小超過一個正常字典的兩倍大，因創建了額外的鏈結串列。

1.8 以字典進行運算
* 問題：
在一個資料字典(dictionary)，進行各種運算。
* 解法：
使用zip()反轉(invert)這個鍵值的keys與values。
使用zip()搭配sorted()進行排序。
注意：zip()建立一個只能消耗一次的迭代器(iterator)
* 討論：
若在字典進行常見的資料縮簡(data reductions)，只會處理鍵值(keys)。
zip()反轉成(values,keys)的序列，先比較value，若剛好有一樣的值，會比較鍵值(key)。

1.9 找出兩個字典的共通處
* 問題：
找出兩個字典共通的鍵值(keys)、值(values)
* 解法：
使用keys()或item()做簡單的集合運算(set operations)，這類運算也這類運算也可用來更動或過濾字典的內容。
* 討論：
一個字典就是一個鍵值(key)集合與一個值(value)集合之間的映射(mapping)。
字典的keys()會回傳一個揭露這些鍵值的keys-view物件。這些物件支援集合運算。
字典的items()會回傳一個items-view物件，由(key, value)對組構成。這些物件支援集合運算。
字典的values()不支援集合運算。原因：values-view 值不保證唯一，使得某些集合運算失去功用。

1.10 從一個序列中移除重複的項目並維持原有順序
* 問題：
消除一個序列(sequence)中重複的值(duplicate values)，但保留剩下項目的次序
* 解法：
若序列中的值事可雜湊的(hashable)，可使用一個集合(set)一個產生器(generator)解決。
若序列中的值是不可雜湊(unhashable)例如：dict，使用key引數指定一個能把序列項目轉為hashable型別的函式，使可偵測重複的值。
* 討論：
若只是想消除重複的項目，通常使用set即可解決，但此方式不表保留順序。
此訣竅使用一個產生器函式(generator function)，表示此函式非常通用。
舉例：讀取檔案並消除重複行。

此處key函式模仿類似功能的內建函式：sorted()、min()、max()。相關實例：1.8，1.13

1.11 為一個切片(Slice)命名
* 問題：
若清理程式充斥著寫死(hardcoded)在程式碼中的切片索引(slice indices)
* 解法：
程式碼範例
* 討論：
內建的slice()會建立一個slice物件，可用在任何允許切片(slice)的地方。
假設有個slice實體s，可用s.start、s.stop、s.step取得更多資訊。
可使用indices(size)會回傳(start, stop, step)元組(tuple)。

1.12 找出一個序列中出現最頻繁的項目
* 問題：
有一個由項目所構成的序列，找出出現最頻繁的項目
* 解法：
collections.Counter類別的most_common()方法
* 討論：
Counter物件可接受任何可雜湊(hashable)的項目序列作為輸入。
Counter是一個映射到出現次數的字典。
若要手動增加次數可用加法。也能使用update()方法。
Counter可用各種數學運算。
Counter物件對於任何需要用到表格資料並進行技術的問題是非常實用的工具。

1.13 藉由一個共通的鍵值來排序一個由字典所構成的串列
* 問題：
一個字典串列(a list of dictionaries)，依據一或多個字典的直來排序其中的條目(entries)。
* 解法：
使用operator模組的itemgetter函式，能輕鬆排序這種結構。
* 討論：
operation.itemgetter()函式可接受的引數是可被用來從rows中的記錄擷取出想要的值的查找索引(lookup indices)，可以是字典鍵值名稱、串列元素或可被未入一個物件的__getitem__()方法的任何值。
若給itemgetter()多個索引，所產的的可呼叫物件會回傳一個其中含有所有指定的值的元組，而sorted()會依據這些元組的次序輸出。
itemgetter()的功能可用lambda取代，但itemgetter()會跑得快一點。若有效能考量可使用。

1.14 在不支援原生的比較運算的情形下排序物件
* 問題：
想排序(sort)同一類別(class)的物件，但沒原生支援(natively support)的比較運算可用。
* 解法：
內建的sorted()函式接受一個key引數，可藉此傳入一個可呼叫物件(callable)，這個callable會回傳物件中的某些值，而sorted會用這些值來比較物件。
可使用lambda以及operator.attrgetter()
* 討論：
可使用lambda以及operator.attrgetter()，attrgetter()速度通常較快一點，且多了「允許同時擷取出多個欄位」的功能。類似為字典使用operator.itemgetter()的選擇(訣竅1.13)。
也可套用到min()或max()這樣的函式。

1.15 基於一個欄位來為記錄分組
* 問題：
一個由字典(dictionaries)或實體(instances)所構成的序列，基於一個特定欄位(例如日期)的值來分組迭代(iterate over)資料。
* 解法：
itertools.groupby()函式適用。
* 討論：
groupby()函式的運作方式是掃瞄一個序列，尋找連續出現的相同值(或由給定的key函式索回傳得值)加以歸組。
每次迭代中，會回傳那個值以及一個迭代器(iterator)。
第一部需依據要分組的欄位進行排序，因groupby()只檢視連續的項目。
若目標是將資料依照日期歸組，成為一個可隨機存取的大型資料結構。
使用defaultdict()建置一個multidict(訣竅1.6)

1.16 過濾序列的元素
* 問題：
一個有資料的序列(sequence)，使用某些條件擷取出值，或縮減(reduce)該佇列。
* 解法：
串列概括式：過濾(filter)序列資料最容易的方式通常是使用一個串列概括式(list comprehension)。
產生器運算式：也可用產生器運算式(genrtator expressions)透過迭代動作逐次產生過濾後的值。
filter()函式：若過濾的程序涉及例外處理或其他繁複的細節，可使用內建的filter()函式。
* 討論：
串列概括式和產生器運算式通常過濾簡單資料最簡單也最直接的方式。有過濾同時轉換資料的額外功能。
以新的值取代不符合條件的值：將過濾條件一到一個條件運算式(conditional expression)。
itertools.compress()：接受一個可迭代物件(iterable)以及一個搭配的Boolean選擇器序列(selector sequence)作為輸入。
filter()和compress()都回傳一個迭代器(iterator)

1.17 擷取出一個字典的子集合
* 問題：
製作一個字典，為另個字典的子集(subset)
* 解法：
使用字典概括式(dictionary comprehension)能夠輕易達成目標。
* 討論：
建立一個元組序列(a sequen of tuples)並傳給dict函式。也可達成字典概括能做到的大部分事情。

1.18 將名稱映射至序列元素
* 問題：
有段程式碼會依據位置存取串列(list)或元組(tuple)的元素，想用名稱存取元素，使結構少依賴位置。
* 解法：
collection.namedtuple()。
* 討論：
nametuple：可以用來取代字典，因字典所需儲存空間較大。然而不同於字典的是，nametuple的內容不可變(immutable)。
若需要變更屬性，可通過nametuple實體的_replace()方法，會建立一個全新的nametuple。
_replace()巧妙的用途：填充(populate)，具有選擇性欄位或缺少欄位的具名元組。先製作一個有預設值的原型元組，然後用_replace()建立一個植被取代的新實體。
若是定義一種有效率的資料結構，可以考慮使用__slots__定義一個類別。(訣竅 8.4)

1.19 同時轉換並縮減資料
* 問題：需要執行一個縮減函式(reduction function，例如：sum(),min(),max())，但得先轉換或過濾資料。
* 解法：
結合資料縮減動作和轉換動作的方式是使用產生器運算式引數(generator-expression argument)。
* 討論：

'''
1.20 將多個映射結合為單一映射
* 問題：
有多個字典(dictionaries)或映射(mappings)，要合理的方式將他們結合，已進行某種動作，例如：值得查找或檢查鍵值是否存在。
* 解法：
collrctions模組的ChainMap類別。
* 討論：
ChainMap 若有變動都會變動第一個映射的值。
ChainMap特別適合用於具有範疇的值(scoped values，如全域值、區域值等)
作為ChainMap的替代方案，可以考慮使用update()方法將字典合併合併再一起。
'''
