import os, time
import keyboard
from gen import print_maze

maze = [[]]
visited = [[]]
end = (0,0)
start = (0,0)
watch = False

# find the coordinates for the start and end
def get_start_end():
    global maze, end, start
    found_start = False
    found_end = False
    i=0
    for row in maze:
        if 's' in row[0]:
            found_start = True
            start = (i,0)
        if 'e' in row[len(row)-1]:
            found_end = True
            end = (i,len(row)-1)
        if found_start and found_end:
            return
        i=i+1

def can_go_up(y,x):
    # check space above for wall
    if('_' in maze[y-1][x]):
        return False
    return True

def can_go_down(y,x):
    # check current space for wall
    if('_' in maze[y][x] or 'o\u0332' in maze[y][x]):
        return False
    return True

def can_go_left(y,x):
    # check left space for wall or start (dont want to leave maze)
    if('|' in maze[y][x-1] or 's' in maze[y][x-1]):
        return False
    return True

def can_go_right(y,x):
    # check current space for wall
    if('|' in maze[y][x]):
        return False
    return True

def getkey():
    key = None
    while key is None:
        event = keyboard.read_event()
        if event.event_type == 'down':
            key = event.name
    return key

def move_marker(curr,prev):
    #move marker and underline if bottom wall
    space=maze[curr[0]][curr[1]]
    if not can_go_down(curr[0], curr[1]):
        maze[curr[0]][curr[1]] = space.replace("_","o\u0332")
    else:
        maze[curr[0]][curr[1]] = space.replace(" ","o", 1)
    #clear prev space
    maze[prev[0]][prev[1]] = maze[prev[0]][prev[1]].replace("o\u0332","_").replace("o"," ")
    
def play():
    global maze, start, end
    #initialize position to right of start
    curr = (start[0], start[1]+1)
    move_marker(curr, start)
    print_maze(maze)
    print("Use WASD or Arrow Keys to move")
    while not curr == end:
        prev = curr
        dir = getkey()
        
        if dir=='w' or dir=="up":
            if not can_go_up(curr[0],curr[1]): continue
            dir = 'up'
            curr = (curr[0]-1, curr[1])
        
        elif dir=='a' or dir=="left":
            if not can_go_left(curr[0],curr[1]): continue
            dir = 'left'
            curr = (curr[0], curr[1]-1)
        
        elif dir=='s' or dir=="down":
            if not can_go_down(curr[0],curr[1]): continue
            dir = 'down'
            curr = (curr[0]+1, curr[1])
        
        elif dir=='d' or dir=="right":
            if not can_go_right(curr[0],curr[1]): continue
            dir = 'right'
            curr = (curr[0], curr[1]+1)
            
        else:
            dir = 'invalid'
            continue
        
        move_marker(curr,prev)
        print_maze(maze)
        print("Use WASD or Arrow Keys to move")
        
    print("You Win!")

def main():
    os.system('cls')
    global maze, watch
    file_list = []

    print("List of mazes:")
    for file in os.listdir('./mazes'):
        if file.endswith('.txt'):
            file_list.append(file)
            print("\t"+str(len(file_list))+":", file)

    maze_num = 0
    while(maze_num > len(file_list) or maze_num < 1):
        maze_num = int(input("Enter number of the maze you want to play: "))
    
    maze = []

    with open('./mazes/'+file_list[maze_num-1], "r") as f:
        for line in f.readlines():
            maze.append([line[i:i+2] for i in range(0, len(line)-1, 2)])
    
    print_maze(maze)
    get_start_end()
    play()

if __name__ == "__main__":
    main()