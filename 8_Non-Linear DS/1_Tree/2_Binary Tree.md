
# Binary Tree

* A binary tree is a tree data structure in which each parent node can have at most two children.
* Every child nodes is labelled as left child or right child 
* Left Child precedes right child in order of Nodes.
* Any tree with degree 2 is a binary tree.
* Here Each node can have 0 or 1 or 2 children.
* maximum number of nodes present in a binary tree of height h =  2<sup>h+1</sup>-1



## Binary Tree Representation :-
> A node of a binary tree is represented by a structure containing a data part and two pointers to other structures of the same type.

<img src="https://cdn.programiz.com/sites/tutorial2program/files/binary-tree-representation_0.png" alt="">

## Types of Binary Tree :-

1. Full Binary Tree or 2-tree :-

A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.

Binary tree of height h is called a full binary tree if  it has 2 <sup>h+1</sup>-1 nodes.

<img src="https://cdn.programiz.com/sites/tutorial2program/files/full-binary-tree_0.png" alt="" />

2. Perfect Binary Tree
A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

<img src="https://cdn.programiz.com/sites/tutorial2program/files/perfect-binary-tree_0.png" alt="" >


3. Complete Binary Tree
A complete binary tree is just like a full binary tree, but with two major differences

* Every level must be completely filled
* All the leaf elements must lean towards the left.
* The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.


<img src="https://cdn.programiz.com/sites/tutorial2program/files/complete-binary-tree_0.png" alt="" >


4. Degenerate or Pathological Tree
A degenerate or pathological tree is the tree having a single child either left or right.
<img src="https://cdn.programiz.com/sites/tutorial2program/files/degenerate-binary-tree_0.png" alt="" >

5. Skewed Binary Tree
A skewed binary tree is a pathological/degenerate tree in which the tree is either dominated by the left nodes or the right nodes. Thus, there are two types of skewed binary tree: left-skewed binary tree and right-skewed binary tree.
<img src="https://cdn.programiz.com/sites/tutorial2program/files/skewed-binary-tree_0.png" alt="" >

6. Balanced Binary Tree
It is a type of binary tree in which the difference between the left and the right subtree for each node is either 0 or 1.
<img src="https://cdn.programiz.com/sites/tutorial2program/files/height-balanced_0.png" alt="" >


## Binary Tree Applications

* For easy and quick access to data
* In router algorithms
* To implement heap data structure
* Syntax tree