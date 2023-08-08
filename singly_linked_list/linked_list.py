'''
This class implements a singly linked list. 
'''
from node import node

# Class
class singly_linked_list():
    def __init__(self):
        self.length_of_list = 0

    def add_node(self, value):
        if self.length_of_list == 0:
            self.head = node(value)
            self.length_of_list += 1
        else:
            start = self.head
            while start.next != None:
                start = start.next
            new_node = node(value)
            start.next = new_node
            self.length_of_list += 1

    def print_list(self):
        start = self.head
        while start != None:
            print(start.value)
            start = start.next

    def insert_at_beginning(self, value):
        new_head = node(value)
        new_head.next = self.head
        self.head = new_head
        self.length_of_list += 1

    def delete_head(self):
        head = self.head
        self.head = self.head.next
        head = None
        self.length_of_list-=1

    def insert_between_nodes_index(self, index, value):
        if index > self.length_of_list:
            print('list isn\'t long enough to index at this position.')
        elif index < 0:
            print('Index can\'t be a negative number')
        else:
            if index == 0:
                self.insert_at_beginning(value)
            else:
                start = self.head
                for i in range(index-1):
                    start = start.next
                new_node = node(value)
                new_node.next = start.next
                start.next = new_node
                self.length_of_list+=1
                

