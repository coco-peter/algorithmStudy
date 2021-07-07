import sys

input = sys.stdin.readline

N = int(input())

class Node:
    def __init__(self, item, lchild, rchild):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

graph = {}
for _ in range(N):
    root, left, right = map(str,input().split())
    graph[root] = (left,right)
    # graph[root] = Node(item = root, lchild = left, rchild = right)

print(graph)

# class version
# def preOrder(node):
#     print("%s" %node.item, end="")
#     if node.lchild != '.':
#         preOrder(graph[node.lchild])
#     if node.rchild != '.':
#         preOrder(graph[node.rchild])
#
# def inOrder(node):
#     if node.lchild != '.':
#         preOrder(graph[node.lchild])
#     print("%s" % node.item, end="")
#     if node.rchild != '.':
#         preOrder(graph[node.rchild])
#
# def postOrder(node):
#     if node.lchild != '.':
#         preOrder(graph[node.lchild])
#     if node.rchild != '.':
#         preOrder(graph[node.rchild])
#     print("%s" % node.item, end="")
#
# preOrder(graph['A'])
# print("")
# inOrder(graph['A'])
# print("")
# postOrder(graph['A'])



def preOrder(node):
    if node == ".":
        return
    print("%s" %node, end="")
    preOrder(graph[node][0])
    preOrder(graph[node][1])

def inOrder(node):
    if node == ".":
        return
    inOrder(graph[node][0])
    print("%s" %node, end="")
    inOrder(graph[node][1])

def postOrder(node):
    if node == ".":
        return
    postOrder(graph[node][0])
    postOrder(graph[node][1])
    print("%s" %node, end="")

preOrder("A")
print("")
inOrder("A")
print("")
postOrder("A")