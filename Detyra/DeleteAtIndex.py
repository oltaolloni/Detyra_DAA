# Përshkruaj zgjidhjen se si mund të implementohet, ashtu që secili nga operacionet ne vijim,
# në vargun e dhënë, koha e ekzekutimit nuk varet në madhësinë e vargut - n.
#
# i) Fshirja e elementit të i-të në një varg
# ii) Fshirja e elementit të i-të në një varg të sortuar
#     (vargu i mbetur duhet të jetë poashtu i sortuar)


# i) Swap dhe Pop në një array (O(1)), funksionon vetem me varg te pasortuar
def delete_at_index(arr, i):
    if i < 0 or i >= len(arr):
        return arr  # Kontroll për indeksin jashtë kufijve

    arr[i], arr[-1] = arr[-1], arr[i]  # Ndërrimi i elementit i-të me të fundit
    arr.pop()  # Fshirja e fundit (O(1))

    return arr

# Testim
nums = [10, 20, 30, 40, 50]
print(delete_at_index(nums, 2))  # [10, 20, 50, 40]

# ii)  Përdorimi i një Linked List për fshirje (O(1))
# Në një array të zakonshëm të sortuar, fshirja e një elementi shkakton
# zhvendosje të elementeve të mbetura për të mbajtur rendin, qw kerkon O(n) kohe
# Linked list numdeson ndryshimin e lidhjeve mes nyjeve pa nevojen e zhvendosjes
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head or self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        while curr.next and curr.next.value < value:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def delete_at_index(self, i):
        if i == 0 and self.head:
            self.head = self.head.next
            return
        prev, curr = None, self.head
        for _ in range(i):
            if not curr:
                return  # Indeksi jashtë kufijve
            prev, curr = curr, curr.next
        if prev and curr:
            prev.next = curr.next  # Lidh nyjen para me atë pas

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

# Testim
sll = SortedLinkedList()
for num in [1, 2, 3, 5, 12]:  # Lista e renditur
    sll.insert(num)

sll.print_list()  # 1 -> 2 -> 3 -> 5 -> 12 -> None

sll.delete_at_index(2)  # Fshijmë elementin në indeksin 2
sll.print_list()  # 1 -> 2 -> 5 -> 12 -> None