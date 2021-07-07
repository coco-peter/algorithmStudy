import sys

input = sys.stdin.readline

word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def preOrder(node):
    print(word[node])
    preOrder(graph[node])



# def midOrder():
#
#
# def postOrder():



graph = []

for _ in range(int(input())):
    graph.append(list(map(str, input().split()))[1:])

#
preOrder(0)
# midOrder("A")
# postOrder("A")
#
