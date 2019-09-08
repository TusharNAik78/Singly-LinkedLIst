class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class link_list:
    def __init__(self):
        self.head=node()
    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def lenght(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total

    def display(self):
        a=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            a.append(cur_node.data)
        print(a)

    def get(self,index):
        if index>=self.lenght():
            print("Out of range")
            return None
        cur_indx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_indx==index: return cur_node.data
            cur_indx+=1
    def erase(self,index):
        if index>=self.lenght():
            print("Out of range")
            return None
        cur_indx=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_indx==index:
                last_node.next=cur_node.next
                return
            cur_indx +=1

ll=link_list()
no=int(input("Enter how many data do you want add in ll:- "))
for i in range(0,no):
    n=int(input())
    ll.append(n)
# ll.append(1)
# ll.append(2)
ll.display()
print(ll.lenght())
# inx=int(input("Enter index:- "))
# print(ll.get(inx))
ino=int(input("enter index:- "))
ll.erase(ino)
ll.display()