class LinkedList:
  def __init__(self):
    self.start_node = None

  def traverse(self):
    pass

  def add_node(self, new_node):
      if self.start_node == None:
        self.start_node = new_node
      else:
        previous = None
        node = self.start_node
        while node:
          print(node.data)
          if ord(node.data) > ord(new_node.data):
            new_node.next_node = node
            if previous == None:
              self.start_node = new_node
              return 
            else:
              previous.next_node = new_node.next_node
              return
          previous = node
          node = node.next_node
        previous.next_node = new_node
              
      # add to the beggining
      # add to the middle
      # add to the end




        
  def remove_node(self, node_to_remove):
        # Remove from beginning
        # Remove from middle
        # Remove from end
        pass



class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

a = LinkedList()
a1 = Node("D")
a3 = Node("W")
a4 = Node("F")
a.start_node = a1
a1.next_node = a4
a4.next_node = a3

# a.add_node(Node('E'))
a.traverse()

while True:
    opt = input('''
1. Add an item
2. Remove an item
3. Traverse
''')
    if opt == '1':
        item = input('Enter item: ')
        a.add_node(Node(item))
        a.traverse()
    elif opt == '2':
        item = input('Enter item: ')
        a.remove_node(item)
        a.traverse()
    else:
        a.traverse()
