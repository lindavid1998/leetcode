'''
There is a collection of photos to place into an empty photo album, one at a time by order of importance. 
Each time a photo is inserted, all subsequent photos are shifted toward the right by one position. 
Given the id’s of the photos and the positions where each should be placed, 
find out the sequence of the photos in the album after all photos have been inserted.

Example

n = 5
index = [0, 1, 2, 1, 2]
identity = [0, 1, 2, 3, 4]

The sequence of the photos is as follows:
    The photos 0, 1 and 2 keep the same indexes 0, 1 and 2 respectively.
    The photo 3 is inserted in index 1 and the subsequent photos 1 and 2 are shifted right by one position.
    The photo 4 is inserted in position 2 and again the photos 1 and 2 are shifted right by one position.

This problem is most similar to:
https://leetcode.com/problems/create-target-array-in-the-given-order/submissions/1494506918/
'''

def solution(index, identity):
  res = []
  n = len(index)
  for i in range(n):
    idx = index[i]
    value = identity[i]
    res.insert(idx, value)
  return res

assert solution([0, 1, 2, 1, 2], [0, 1, 2, 3, 4]) == [0, 3, 4, 1, 2]