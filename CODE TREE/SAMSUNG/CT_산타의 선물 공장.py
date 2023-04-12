# 삼성 SW 역량테스트 2022 하반기 오전 2번 문제

# import sys
# input = sys.stdin.readline
# # sys.stdin = open("input.txt", "r")
import io, os, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
ans = __pypy__.builders.StringBuilder()

class NODE():
    def __init__(self, boxid=None, weight = None, belt_pos = None, prev=None, next=None):
        self.boxid = boxid
        self.weight = weight
        self.belt_pos = belt_pos
        self.prev = prev
        self.next = next

class DLL():
    def __init__(self):
        self.head = NODE()
        self.tail = NODE()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.repair = True
        self.cnt = 0

    def append(self, boxid, weight, belt_pos):
        self.cnt += 1
        p_node = self.tail.prev
        new_node = NODE(boxid, weight, belt_pos, p_node, self.tail)
        p_node.next = new_node
        self.tail.prev = new_node
        hash_table[boxid] = new_node

    def appendleft(self, boxid, weight, belt_pos):
        self.cnt += 1
        n_node = self.head.next
        new_node = NODE(boxid, weight, belt_pos, self.head, n_node)
        self.head.next = new_node
        n_node.prev = new_node
        hash_table[boxid] = new_node

    def pop(self):
        self.cnt -= 1
        del_node = self.tail.prev
        p_node = del_node.prev
        p_node.next = self.tail
        self.tail.prev = p_node
        del hash_table[del_node.boxid]
        return del_node.boxid, del_node.weight
    
    def popleft(self):
        self.cnt -= 1
        del_node = self.head.next
        n_node = del_node.next
        n_node.prev = self.head
        self.head.next = n_node
        del hash_table[del_node.boxid]
        return del_node.boxid, del_node.weight

q = int(input().rstrip())
for _ in range(q):
    cmd, *args = map(int, input().rstrip().split())
    if cmd == 100: 
        n, m, *infos = args
        p_id, p_weight, size = infos[:n], infos[n:], n//m
        belts, hash_table = [DLL() for _ in range(m+1)], dict()
        for belt_num in range(m):
            for idx in range(belt_num*size, (belt_num+1)*size):
                belts[belt_num+1].append(p_id[idx], p_weight[idx], belt_num+1)
        belts[0].repair = False

    elif cmd == 200: 
        w_max = args[0]
        result = 0
        for belt_num in range(1, m+1):
            if belts[belt_num].cnt > 0 and belts[belt_num].repair:
                head_id, head_weight = belts[belt_num].popleft()
                if head_weight <= w_max: result += head_weight
                else: belts[belt_num].append(head_id, head_weight, belt_num)
        ans.append(str(result) + '\n')
        # print(result)

    elif cmd == 300: 
        r_id = args[0]
        if r_id in hash_table:
            belt_num = hash_table[r_id].belt_pos
            p_node, n_node = hash_table[r_id].prev, hash_table[r_id].next
            p_node.next = n_node
            n_node.prev = p_node
            belts[belt_num].cnt -= 1
            del hash_table[r_id]

        else: r_id = -1
        ans.append(str(r_id) + '\n')
        # print(r_id)

    elif cmd == 400:
        f_id = args[0]
        if f_id in hash_table:
            curr_beltnum = hash_table[f_id].belt_pos
            if hash_table[f_id].prev != belts[curr_beltnum].head:
                new_head, new_tail = hash_table[f_id], hash_table[f_id].prev
                prev_head, prev_tail = belts[curr_beltnum].head.next, belts[curr_beltnum].tail.prev
                
                belts[curr_beltnum].head.next = new_head
                new_head.prev = belts[curr_beltnum].head
                
                belts[curr_beltnum].tail.prev = new_tail
                new_tail.next = belts[curr_beltnum].tail

                prev_head.prev = prev_tail
                prev_tail.next = prev_head
            
        else: curr_beltnum = -1
        ans.append(str(curr_beltnum) + '\n')
        # print(curr_beltnum)

    elif cmd == 500:
        b_num = args[0]
        if not belts[b_num].repair: ans.append(str(-1) + '\n'); continue
            # print(-1); continue
        else:
            belt_index = (b_num + 1) % (m+1)
            while True:
                if belts[belt_index].repair:
                    while belts[b_num].cnt > 0:
                        head_id, head_weight = belts[b_num].popleft()
                        belts[belt_index].append(head_id, head_weight, belt_index)
                    belts[b_num].repair = False
                    break
                belt_index = (belt_index + 1) % (m+1)
            ans.append(str(b_num) + '\n')
            # print(b_num)

os.write(1, ans.build().encode())