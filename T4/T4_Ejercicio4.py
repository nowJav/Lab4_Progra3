# Definición: Nodo de árbol binario.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def delete_Node(root, key):
 # si la raíz no existe, simplemente devuélvela
	if not root: 
		return root
	# Encuentra el nodo en el subárbol izquierdo si el valor clave es menor que el valor raíz
	if root.val > key: 
		root.left = delete_Node(root.left, key)
	# Encuentra el nodo en el subárbol derecho si el valor clave es mayor que el valor raíz, 
	elif root.val < key: 
		root.right= delete_Node(root.right, key)
	# Eliminar el nodo si root.value == clave
	else: 
	# Si no hay hijos correctos, elimine el nodo y la nueva raíz sería root.left
		if not root.right:
			return root.left
	# Si no quedan hijos, elimine el nodo y la nueva raíz sería root.right	
		if not root.left:
			return root.right
# Si los hijos izquierdo y derecho existen en el nodo, reemplace su valor con
  # el valor mínimo en el subárbol derecho. Ahora elimina ese nodo mínimo
  # en el subárbol derecho
		temp_val = root.right
		mini_val = temp_val.val
		while temp_val.left:
			temp_val = temp_val.left
			mini_val = temp_val.val
# Eliminar el nodo mínimo en el subárbol derecho
		root.right = delete_Node(root.right,root.val)
	return root

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   
    
root = TreeNode(5)  
root.left = TreeNode(3)  
root.right = TreeNode(6) 
root.left.left = TreeNode(2)  
root.left.right = TreeNode(4) 
root.left.right.left = TreeNode(7)  
print("Original node:")
print(preOrder(root))
result = delete_Node(root, 4)
print("After deleting specified node:")
print(preOrder(result))