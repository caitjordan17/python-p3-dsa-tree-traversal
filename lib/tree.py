class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while nodes_to_visit:
      current = nodes_to_visit.pop()
      if current['id'] == id:
        return current
      
      nodes_to_visit = nodes_to_visit + current['children']
    return None


# def depth_first_traversal(node):
#   result = []
#   nodes_to_visit = [node]

#   while len(nodes_to_visit) > 0:
#     # 1. Remove the first node from the `nodes_to_visit` list
#     node = nodes_to_visit.pop(0)
#     # 2. Add its value to the result list
#     result.append(node['value'])
#     # 3. Add its children (if any) to the BEGINNING of the `nodes_to_visit` list
#     nodes_to_visit = node['children'] + nodes_to_visit

#   return result

# def breadth_first_traversal(node):
#   result = []
#   nodes_to_visit = [node]
#   print("0:", nodes_to_visit)

#   while len(nodes_to_visit) > 0:
#     # 1. Remove the first node from the `nodes_to_visit` list
    
#     node = nodes_to_visit.pop(0)
    
#     print("1:", nodes_to_visit)
#     # 2. Add its value to the result list
    
#     result.append(node['value'])
    
#     print("2:", nodes_to_visit)
#     print("result:", result)
#     # 3. Add its children (if any) to the END of the `nodes_to_visit` list
    
#     nodes_to_visit = nodes_to_visit + node['children']

#   return result

# child_1 = {
#   'value': 2,
#   'children': []
# }

# child_2 = {
#   'value': 3,
#   'children': []
# }

# child_3 = {
#   'value': 4,
#   'children': []
# }

# root = {
#   'value': 1,
#   'children': [child_1, child_2, child_3]
# }
# print(breadth_first_traversal(root))