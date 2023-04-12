# 삼성 SW 역량테스트 2022 하반기 오후 2번 문제

# import sys
# input = sys.stdin.readline
# # sys.stdin = open("input.txt", "r")
import io, os, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
ans = __pypy__.builders.StringBuilder()

class NODE:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = NODE()
        self.tail = NODE()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cnt = 0

    def append(self, data):
        self.cnt += 1
        p_node = self.tail.prev
        new_node = NODE(data, p_node, self.tail)
        p_node.next = new_node
        self.tail.prev = new_node
        hash_table[data] = new_node

    def appendleft(self, data):
        self.cnt += 1
        n_node = self.head.next
        new_node = NODE(data, self.head, n_node)
        self.head.next = new_node
        n_node.prev = new_node
        hash_table[data] = new_node
    
    def popleft(self):
        self.cnt -= 1
        del_node = self.head.next
        n_node = del_node.next
        self.head.next = n_node
        n_node.prev = self.head

        del hash_table[del_node.data]
        return del_node.data
       
    def search_mid(self):
        curr = self.head
        for _ in range(self.cnt//2):
            curr = curr.next
        return curr
    

q = int(input().rstrip())
for _ in range(q):
    cmd, *args = map(int, input().rstrip().split())
    if cmd == 100:
        n, m, *p_list = args
        belts, hash_table = [DLL() for _ in range(n+1)], dict()

        for p_num, b_num in enumerate(p_list, start=1):
            belts[b_num].append(p_num)

    elif cmd == 200:
        m_src, m_dst = args
        # exception #
        if belts[m_src].cnt == 0: ans.append(str(belts[m_dst].cnt) + '\n'); continue
        # print(belts[m_dst].cnt)
        # dst prev, next change #
        src_head, src_tail, dst_head = belts[m_src].head.next, belts[m_src].tail.prev, belts[m_dst].head.next
        src_head.prev = belts[m_dst].head
        src_tail.next = dst_head
        belts[m_dst].head.next = src_head
        dst_head.prev = src_tail
        # src prev, next clear #
        belts[m_src].head.next = belts[m_src].tail
        belts[m_src].tail.prev = belts[m_src].head
        # cnt #
        belts[m_dst].cnt += belts[m_src].cnt
        belts[m_src].cnt = 0
        
        ans.append(str(belts[m_dst].cnt) + '\n')
        # print(belts[m_dst].cnt)

    elif cmd == 300:
        m_src, m_dst = args

        # extract top box #
        top_src, top_dst = None, None
        if belts[m_src].cnt > 0: top_src = belts[m_src].popleft()
        if belts[m_dst].cnt > 0: top_dst = belts[m_dst].popleft()
        # append otherwise box #
        if top_src: belts[m_dst].appendleft(top_src)
        if top_dst: belts[m_src].appendleft(top_dst)

        ans.append(str(belts[m_dst].cnt) + '\n')
        # print(belts[m_dst].cnt)

    elif cmd == 400:
        m_src, m_dst = args
        # exception #
        if belts[m_src].cnt <= 1: ans.append(str(belts[m_dst].cnt) + '\n'); continue
        # print(belts[m_dst].cnt)
        src_head, src_tail, dst_head = belts[m_src].head.next, belts[m_src].search_mid(), belts[m_dst].head.next
        new_src = src_tail.next
        # dst prev, next change #
        dst_head.prev = src_tail
        src_tail.next = dst_head
        src_head.prev = belts[m_dst].head
        belts[m_dst].head.next = src_head
        # src prev, next change #
        belts[m_src].head.next = new_src
        new_src.prev = belts[m_src].head
        # cnt #
        divide_len = belts[m_src].cnt // 2
        belts[m_src].cnt -= divide_len
        belts[m_dst].cnt += divide_len
        
        ans.append(str(belts[m_dst].cnt) + '\n')
        # print(belts[m_dst].cnt)

    elif cmd == 500:
        p_num = args[0]
        a, b = hash_table[p_num].prev.data, hash_table[p_num].next.data
        if not a: a = -1
        if not b: b = -1
        
        ans.append(str(a + 2*b) + '\n')
        # print(a + 2*b)

    elif cmd == 600:
        b_num = args[0]
        a, b, c = belts[b_num].head.next.data, belts[b_num].tail.prev.data, belts[b_num].cnt
        if not a: a = -1
        if not b: b = -1
        
        ans.append(str(a + 2*b + 3*c) + '\n')
        # print(a + 2*b + 3*c)

os.write(1, ans.build().encode())