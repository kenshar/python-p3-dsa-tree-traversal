class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    if not self.root:
      return None

    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      nodes_to_visit = nodes_to_visit + node['children']

    return None


def breadth_first_traversal(node):
  result = []
  nodes_to_visit = [node]

  while len(nodes_to_visit) > 0:
    node = nodes_to_visit.pop(0)
    result.append(node['value'])
    nodes_to_visit = nodes_to_visit + node['children']

  return result


def depth_first_traversal(node):
  result = []
  nodes_to_visit = [node]

  while len(nodes_to_visit) > 0:
    node = nodes_to_visit.pop(0)
    result.append(node['value'])
    nodes_to_visit = node['children'] + nodes_to_visit

  return result
