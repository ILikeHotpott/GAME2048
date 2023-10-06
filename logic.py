import random
import constants as c

def new_game(n):
    matrix = []
    for i in range(n):
        matrix.append([0]*n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix

def add_two(mat):
    a = random.randint(0,len(mat)-1)
    b = random.randint(0,len(mat)-1)
    while mat[a][b] != 0:
        a = random.randint(0,len(mat)-1)
        b = random.randint(0,len(mat)-1)
    mat[a][b] = 2
    return mat

def game_state(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 2048:
                return 'win'
            
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                return 'not over'
            
    for i in range(n-1):
        for j in range(n-1):
            if mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i+1][j]:
                return 'not over'
            
    for k in range(n-1):
        if mat[n-1][k] == mat[n-1][k+1]:
            return 'not over'
        
    for j in range(n-1):
        if mat[j][n-1] == mat[j+1][n-1]:
            return 'not over'
        
    return 'lose'

def reverse(mat):
    n = len(mat)
    new = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n-1, -1, -1):
            new[i].append(mat[i][j])

    return new
    
def transpose(mat):
    n = len(mat)
    new = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[i].append(mat[j][i])

    return new

def cover_up(mat):
    new = [[0]*c.GRID_LEN for _ in range(c.GRID_LEN)]
    done = False
    
    for i in range(c.GRID_LEN):
        count = 0
        for j in range(c.GRID_LEN):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done

def merge(mat, done):
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN-1):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return mat, done

def up(game):
    print("up")
    game = transpose(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(game)
    return game, done

def down(game):
    print("down")
    game = reverse(transpose(game))
    game = reverse(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return game, done

def left(game):
    print("left")
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    return game, done

def right(game):
    print(right)
    game = reverse(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game  = cover_up(game)[0]
    game = reverse(game)
    return game, done
