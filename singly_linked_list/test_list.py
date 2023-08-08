'''
main function to test singly linked list
'''

# Imports
from linked_list import singly_linked_list

def main():
    SLL = singly_linked_list()
    SLL.add_node('I')
    SLL.add_node('Like')
    SLL.add_node('to')
    SLL.add_node('Eat')
    SLL.insert_at_beginning('1, 2, 3, 4: ')
    SLL.print_list()
    SLL.delete_head()
    SLL.print_list()
    SLL.insert_between_nodes_index(5, 'sit')
    SLL.insert_between_nodes_index(4, 'and')
    SLL.insert_between_nodes_index(0, 'new head')
    SLL.print_list()

if __name__ == '__main__':
    main()