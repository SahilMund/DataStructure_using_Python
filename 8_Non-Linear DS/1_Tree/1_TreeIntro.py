
# ! Tree 

'''
 A tree is a nonlinear hierarchical data structure that consists of nodes connected by edges.

Tree is a collection of nodes and edges and the edges gives the relatinoship between nodes.

'''

'''
# ? Why Tree Data Structure?

Other data structures such as arrays, linked list, stack, and queue are linear data structures that store data sequentially.
In order to perform any operation in a linear data structure, the time complexity increases with the increase in the data size.
But, it is not acceptable in today's computational world.
Different tree data structures allow quicker and easier access to the data as it is a non-linear data structure.
'''

#! Terminology :-
'''
#? 1.Node
A node is an entity that contains a key or value and pointers to its child nodes.

        # ? a) leaf nodes or external nodes:-
        The last nodes of each path are called leaf nodes or external nodes that do not contain a link/pointer to child nodes.

        # ? b)internal node or non-leaf nodes:-
        The node having at least a child node is called an internal node.

        # ? c)siblings Nodes:-
        Node that are childrens of same parent node.


        # ? d). Root node:-
        It is the topmost node of a tree.Root node doesn't have parent tree

# ? 2. Edge

It is the link between any two nodes.
(For n number of nodes = n ,then number of edeges = n-1  )

# ?3.  Path 
Sequence of nodes such that two consecutive nodes forms an edge.
A path start from root node and goes upto leaf node.


# ? 4. Height of a Node
The height of a node is the number of edges from the node to the deepest leaf (ie. the longest path from the node to a leaf node).

# ? 5. Depth of a Node
The depth of a node is the number of edges from the root to the node.

# ? 6.Height of a Tree
The height of a Tree is the height of the root node or the depth of the deepest node.

# ? 7.Degree of a Node
The degree of a node is the total number of branches of that node.

# ? 8.Degree of a Tree
The degree of a tree is the maximum degree of the node.

# ? 9.Forest
A collection of disjoint trees is called a forest.
You can create a forest by cutting the root of a tree.


# ? 10. subtree
Any nodes having a children node is considered as subtree and also all the leaf nodes
are considered as subtree. 

'''


#! Types of Tree
'''
1)  Binary Tree
2)  Binary Search Tree
3)  AVL Tree
4)  B-Tree

'''
# ! Tree Applications :-
'''
Binary Search Trees(BSTs) are used to quickly check whether an element is present in a set or not.
Heap is a kind of tree that is used for heap sort.
A modified version of a tree called Tries is used in modern routers to store routing information.
Most popular databases use B-Trees and T-Trees, which are variants of the tree structure we learned above to store their data
Compilers use a syntax tree to validate the syntax of every program you write.

'''