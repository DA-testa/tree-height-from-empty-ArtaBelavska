# # python3
import sys
import threading
#import numpy


def compute_height(n, parents):
    # izveido sarakstu lai saglabatu mezlu skaitu
    heights = [0] * n
    # Atrast saknes skaitu
    root = parents.index(-1)
    # aprekinat katra mezgla augstumu
    def dfs(skaits):
        # atgriezt mezgla uagstumu ja tas ir aprekinats
        if heights[skaits] != 0:
            return heights[skaits]
        if skaits == root:  # ja ir sakne tad garums ir 1
            heights[skaits] = 1
        else: # aprekina vecaka garumu un pieliek 1
            heights[skaits] = dfs(parents[skaits]) + 1
        return heights[skaits]
    #aprekina katra mezgla augstumu
    for i in range(n):
        dfs(i)
    # atgriez maksimalo garumu
    return max(heights)


def main():
    text=input("Enter I or F: ")
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
    elif "F" in text:
        filename=input()
        if "a" not in filename:
            try:
                with open ("/test/16", mode="r") as fails:
                    text=fails.read()
                    parents=list(map(int, fails.readline().split()))
            except Exception as j:
                print("Error:", str(j))
                return
        else:
            print("Error: invalid filename")
            return
    max_height = compute_height(n, parents)
    print(max_height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()