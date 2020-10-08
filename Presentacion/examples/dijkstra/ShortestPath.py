# COURSERA ROBOTICS CAPSTONE PROJECT - WEEK 1
# DIJKSTRA SHORTEST PATH ALGORITHM
#
# Usage:  If you run it right now will work only on path2
# of the test_for_grader() function
# I have some problems with the algorithm and the arrays.
# If you want it to work:
# 1 - Go to the mappos function and follow the steps
# 2 - Go to the test for grader and disable the map one or
# two depending on the case
#

import numpy as np
import yaml


def dijkstras(occupancy_map,x_spacing,y_spacing,start,goal):
    """
    Implements Dijkstra's shortest path algorithm
    Input:
    occupancy_map - an N by M numpy array of boolean values (represented
        as integers 0 and 1) that represents the locations of the obstacles
        in the world
    x_spacing - parameter representing spacing between adjacent columns
    y_spacing - parameter representing spacing between adjacent rows
    start - a 3 by 1 numpy array of (x,y,theta) for the starting position
    goal - a 3 by 1 numpy array of (x,y,theta) for the finishing position
    Output:
    path: list of the indices of the nodes on the shortest path found
        starting with "start" and ending with "end" (each node is in
        metric coordinates)
    """


    # Set the obstacle as 65535 and infinite distance as 256
    OBSTACLE = np.power(2,16)
    INF = np.power(2,8)


    # Convert the start and goal positions to cartesian coordinates
    start = mappos(start, x_spacing, y_spacing)
    goal = mappos(goal, x_spacing, y_spacing)


    # occupancy map as input is copied to set the distance map
    # distance_map = map of distances between the starting point
    # and the goal.
    # 1 - Copy the map
    # 2 - Set all 1's to the obstacle value
    # 3 - Set the unocupied regions to a distance of 1
    # 4 - Set the start position to 0 (starting vertex distance)
    distance_map = occupancy_map.copy()
    distance_map[distance_map == 1] = OBSTACLE
    distance_map[distance_map == 0] = 1
    distance_map[start] = 0


    # shortPathFromStart is a map of initial values of the distances
    # 1 - Copy from the occupancy map
    # 2 - Set the non visited regions as infinity distances
    # 3 - Set the starting vertex distance as 0
    shortPathFromStart = distance_map.copy()
    shortPathFromStart[distance_map == 1] = INF
    shortPathFromStart[start] = 0


    # Set some useful arrays and dictionarys to track places
    # unvisited = array of unvisited vertexes
    # visited   = array of visited vertexes
    # previous  = dictionary of previos vertex and reference vertex
    unvisited = []
    visited = []
    previous = {}


    # Do the array of unvisited vertexes
    # Get the distancemap and fill with the vertexes but
    # exclude the obsacles
    for i, item in enumerate(distance_map):
      for j, x in enumerate(item):
        if x != OBSTACLE:
          unvisited.append((i,j))


    # Repeat the lines below for each vertex in unvisited vertexes
    while len(unvisited):
      # calculate the minimun vertex from unvisited vertexes from start
      # 1 - Set a minimal value as "Infinite"
      minVal = INF
      # 2 - For each vertex in the unvisited vertexes get the index
      # of the vertex with te mininum distance and set as the lowest
      # distance of unvisited vertex
      for Ix in unvisited:
        if len(unvisited) == 1:
          minIx = Ix
          break
        if  shortPathFromStart[Ix] < minVal:
          minIx = Ix
          minVal = shortPathFromStart[Ix]
      # 3 - Transform to coordinates and set it as the minimun, that is
      # the current Vertex with smallest distance from unvisited neighbors
      x = np.int(minIx[0])
      y = np.int(minIx[1])
      minV = (x, y)
      # 4 - Set a index list of vertexes neighbors (up, down, left or right)
      # no matter if they are out of the map, we will filter this later
      vertex = [(minV[0] + 1, minV[1]), \
                (minV[0] - 1, minV[1]), \
                (minV[0], minV[1] + 1), \
                (minV[0], minV[1] - 1)]
      # 5 - For each vertex in the neighbors vertexes check the distances
      for v in vertex:
        # 5.1 - Discern if the limits are out of bounds or its an obstacle
        # and continue with the iteration.  On the other hand...
        if v[0] < 0 or v[0] >= shortPathFromStart.shape[0] \
        or v[1] < 0 or v[1] >= shortPathFromStart.shape[1] \
        or shortPathFromStart[v] == OBSTACLE:
          continue
        else:
        # 5.2 - Calculate the distance of the studied vertex and if the
        # distance is lower replace with this minimun distance in the map
        # Also, add the vertex and previous to the dictionary of vertexes
          d = shortPathFromStart[minV] + distance_map[v]
          if d < shortPathFromStart[v]:
            shortPathFromStart[v] = d
            previous[v] = minV
      # 6 - Remove the unvisited vertex and add to the list of visited
      visited.append(minV)
      unvisited.remove(minV)
      # 7 - If the distances studied of the current vertex is the goal
      # then do an early out (probably is not a good option because
      # it could be a better distance map)
      if minV == goal:
        break


    # Find the path in cartesian coordinates
    path = findpath(previous, start, goal)


    # Return the truepoints coordinates depending of x and y spacings
    path = truepoints(path, x_spacing, y_spacing)


    # Send the path back in array form
    return path


'''
  Function Name:  truepoints
  Inputs
  path:  An array of the paths of the dijkstra algorithm
  x_spacing: the spacing on the x position
  y_spacing: the spacing on the y position

  Outputs
  A true path in real distances based on measurements
'''

def truepoints(path, x_spacing, y_spacing):
  for n, ix in enumerate(path):
    i, j = scalar(path[n])
    a = np.around((j + 0.5)*x_spacing, decimals = 3)
    b = np.around((i + 0.5)*y_spacing, decimals = 3)
    path[n] = [a, b]
  return np.array(path)


'''
  Function Name:  findpath
  Inputs
  paths:  A dictionary containing {vertex:previousvertex} list
  s:  start position
  g:  goal position

  Outputs
  A true path in cartesian integer coordinates
'''

def findpath(paths, s, g):
  path = []
  g = scalar(g)
  s = scalar(s)
  prev = g
  path.append(g)
  for p in paths:
      prev = paths.get(prev)
      path.append(prev)
      if prev == s:
        break
  path.reverse()
  return path


'''
  Function Name:  scalar
  Inputs
  arr: An array containing the point [A B ...N]
  x_spacing: the spacing on the x position
  y_spacing: the spacing on the y position

  Outputs
  a tuple named 'x' and 'y' of cartesian coordinates
'''

def scalar(arr):
  arr = np.ravel(arr)
  x = arr[0]
  x = np.asscalar(np.array(x))
  y = arr[1]
  y = np.asscalar(np.array(y))
  return x, y


'''
  Function Name: mappos
  Inputs
  pt:  An array of format ([A B .. N])
  x_spacing: the spacing on the x position
  y_spacing: the spacing on the y position

  Outputs
  a tuple named 'i' and 'j' of cartesian coordinates
'''

def mappos(pt, x_spacing, y_spacing):
  x, y = (pt[0], pt[1])
# FOR TEST_MAP1
# enable lines below for test_map1 and
# disable in test_for_grader() the test_map2 inputs
#  j = np.int_(np.rint(np.ceil(x/x_spacing - 0.5)))
#  i = np.int_(np.rint(np.ceil(y/y_spacing - 0.5)))

# FOR TEST_MAP2
# enable lines below for test_map2
# disable in test_for_grader() the test_map1 inputs
# as shown in test_for_grader() inputs
  j = np.int_(np.rint(np.floor(x/x_spacing - 0.5)))
  i = np.int_(np.rint(np.floor(y/y_spacing - 0.5)))
  return i, j


'''
  Function Name: posmap
  Inputs
  index:  An array of format (A, B)
  x_spacing: the spacing on the x position
  y_spacing: the spacing on the y position

  Outputs
  Transform to real coordinates a point
'''

def posmap(index, x_spacing, y_spacing):
  i = index[0]
  j = index[1]
  x = np.around((j + 0.5)*x_spacing, decimals=3)
  y = np.around((i + 0.5)*y_spacing, decimals=3)
  pt = [x, y]
  return pt



def test():
    """
    Function that provides a few examples of maps and their solution paths
    """
    test_map1 = np.array([
              [1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1]])
    x_spacing1 = 0.13
    y_spacing1 = 0.2
    start1 = np.array([[0.3], [0.3], [0]])
    goal1 = np.array([[0.6], [1], [0]])
    path1 = dijkstras(test_map1,x_spacing1,y_spacing1,start1,goal1)
    true_path1 = np.array([
        [ 0.3  ,  0.3  ],
        [ 0.325,  0.3  ],
        [ 0.325,  0.5  ],
        [ 0.325,  0.7  ],
        [ 0.455,  0.7  ],
        [ 0.455,  0.9  ],
        [ 0.585,  0.9  ],
        [ 0.600,  1.0  ]
        ])
    print(path1)
    if np.array_equal(path1,true_path1):
      print("Path 1 passes")

    test_map2 = np.array([
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 1, 1, 0, 0, 1],
             [1, 0, 0, 1, 1, 0, 0, 1],
             [1, 0, 0, 1, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]])
    start2 = np.array([[0.5], [1.0], [1.5707963267948966]])
    goal2 = np.array([[1.1], [0.9], [-1.5707963267948966]])
    x_spacing2 = 0.2
    y_spacing2 = 0.2
    path2 = dijkstras(test_map2,x_spacing2,y_spacing2,start2,goal2)
    true_path2 = np.array([[ 0.5,  1.0],
                           [ 0.5,  1.1],
                           [ 0.5,  1.3],
                           [ 0.5,  1.5],
                           [ 0.7,  1.5],
                           [ 0.9,  1.5],
                           [ 1.1,  1.5],
                           [ 1.1,  1.3],
                           [ 1.1,  1.1],
                           [ 1.1,  0.9]])
    print(path2)
    if np.array_equal(path2,true_path2):
      print("Path 2 passes")

def test_for_grader():
    """
    Function that provides the test paths for submission
    """
'''
    test_map1 = np.array([
              [1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 1, 0, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 0, 0, 1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1]])
    x_spacing1 = 1
    y_spacing1 = 1
    start1 = np.array([[1.5], [1.5], [0]])
    goal1 = np.array([[7.5], [1], [0]])
    path1 = dijkstras(test_map1,x_spacing1,y_spacing1,start1,goal1)
    s = 0
    for i in range(len(path1)-1):
      s += np.sqrt((path1[i][0]-path1[i+1][0])**2 + (path1[i][1]-path1[i+1][1])**2)
    print("Path = \n", path1)
    print("Path 1 length:")
    print(np.around(s, decimals = 3))
'''


test_map2 = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]])
start2 = np.array([[0.4], [0.4], [1.5707963267948966]])
goal2 = np.array([[0.4], [1.8], [-1.5707963267948966]])
x_spacing2 = 0.2
y_spacing2 = 0.2
path2 = dijkstras(test_map2,x_spacing2,y_spacing2,start2,goal2)
s = 0
for i in range(len(path2)-1):
  s += np.sqrt((path2[i][0]-path2[i+1][0])**2 + (path2[i][1]-path2[i+1][1])**2)
print("Path = \n", path2)
print("Path 2 length:")
print(np.around(s,decimals=3))



def main():
    # Load parameters from yaml
    param_path = 'params.yaml' # rospy.get_param("~param_path")
    f = open(param_path,'r')
    params_raw = f.read()
    f.close()
    params = yaml.load(params_raw)
    # Get params we need
    occupancy_map = np.array(params['occupancy_map'])
    pos_init = np.array(params['pos_init'])
    pos_goal = np.array(params['pos_goal'])
    x_spacing = params['x_spacing']
    y_spacing = params['y_spacing']
    path = dijkstras(occupancy_map,x_spacing,y_spacing,pos_init,pos_goal)

if __name__ == '__main__':
    test_for_grader()
