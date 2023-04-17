import random
import time, os, sys

maze = [[]]
visited = [[]]
end = (0,0)
start = (0,0)
watch = False

# generates square maze with start and end using DFS

def generate_maze(n):
    n = n+1 #need extra space for outer walls
    global maze, start, end, visited
    # initialize maze
    maze = [['_|' for j in range(n)] for i in range(n)]
    for i in range(0,n):
        maze[i][0]=' |'
        maze[0][i]='_ '
    maze[0][0] = '  '
    
    visited = [[False for j in range(n)] for i in range(n)]
    start = (random.randint(1, n-1), 1)
    end = (random.randint(1, n-1), n-1)
    maze[start[0]][start[1]-1]= ' s'
    dfs(start)
    ex=maze[end[0]][end[1]]
    maze[end[0]][end[1]] = ex.replace("|","e")
    if watch: print_maze(maze)

def dfs(curr):
    global maze, visited, watch
    n = len(maze)
    visited[curr[0]][curr[1]] = True
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    random.shuffle(directions) # randomize L
    for d in directions: # try every direction
        # get neighbor
        neighbor = (curr[0]+d[0], curr[1]+d[1])
        # check neighbor in mze and not visited
        if 1 <= neighbor[0] < n and 1 <= neighbor[1] < n and not visited[neighbor[0]][neighbor[1]]:
            if watch:
                print_maze(maze)
                time.sleep(0.1)
            connectCells(curr, neighbor, d)
            dfs(neighbor)
    return

def connectCells(curr, next, d):
    global maze, end

    if(d==(1,0)): #D
        if(maze[curr[0]][curr[1]] == '_ '):
            maze[curr[0]][curr[1]] = '  '
        else: maze[curr[0]][curr[1]] = ' |'
        
    if(d==(-1,0)): #U
        maze[next[0]][next[1]] = ' |'
        
    if(d==(0,1)): #R
        if(maze[curr[0]][curr[1]] == ' |'):
            maze[curr[0]][curr[1]] = '  '
        else: maze[curr[0]][curr[1]] = '_ '
        
    if(d==(0,-1)): #L
        maze[next[0]][next[1]] = '_ '

def print_maze(maze):
    m = maze_to_str(maze)
    os.system('cls')
    print(m)

def maze_to_str(maze):
    m = ''
    for row in maze:
        for col in row:
            m += col
        m += '\n'
    return m

def save_maze(f,maze):
    if not os.path.exists("./mazes"):
        os.makedirs("./mazes")
    f = open('./mazes/'+f+'.txt', "w")
    f.write(maze_to_str(maze))
    f.close()
    

def main():
    global maze, watch
    os.system('cls')
    size=0
    while(size > 100 or size < 5):
        size = int(input('Size (from 5 to 50): '))

    yn = input('Watch? (Y/N):  ')
    if(yn=='y' or yn=='Y'):
        watch=True

    lim = sys.getrecursionlimit()
    sys.setrecursionlimit(1000000)
    generate_maze(size)
    sys.setrecursionlimit(lim)

    if not watch:
        yn = input('Print? (Y/N):  ')
        if(yn=='y' or yn=='Y'):
            print_maze(maze)
        
    yn = input('Save? (Y/N):  ')
    if(yn=='y' or yn=='Y'):
        f = input('save-file name: ')
        save_maze(f,maze)

if __name__ == "__main__":
    main()