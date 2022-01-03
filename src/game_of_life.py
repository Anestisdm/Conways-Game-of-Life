"""Conway\'s Game of Life."""

def board(n):
    """Constructs the board of the game.

    n -- dimension parameter of the board

    Constructs representation of the game board with n x n cells,
    where no cell is alive

    Return representation of the game board, where it is a dictionary
    with n x n elements.
    Εach cell corresponds to one element with key the tuple (i, j),
    where inumber of row and j number of column where the cell is located.
    The value of the element is True or False depending on whether
    the cell is alive or not


   Examples:

    >>> game = board(3)
    >>> len(game)
    9
    >>> game
    {(0, 0): False, (0, 1): False, (0, 2): False, (1, 0): False, (1, 1): False, (1, 2): False, (2, 0): False, (2, 1): False, (2, 2): False}
    >>> game[2,1]
    False
    """

    i=0
    ls=[]
    while i<=n-1:
        j=0
        while j<=n-1:
            ls.append([(i,j),False])
            j+=1
        i+=1
    return dict(ls)



def is_alive(board, p):
    """Checks whether the cell is alive.

    board -- game board where the cell is located
    p -- the position of the cell.

    The argument p is tuple of the format (i,j).
    Returns True if the cell is alive or False.

    Examples:

    >>> is_alive(board(4), (3,2))
    False
    """

    return board[p]



def set_alive(board, p, alive):
    """Places or removes live from a cell.

    board -- game board where the cell is located
    p -- the position of the cell.
    alive -- boolean value.

    The cell becomes alive if the arg alive is True. If arg alive is False,
    the cell die.

    Examples:

    >>> game = board(4)
    >>> is_alive(game, (3,2))
    False
    >>> set_alive(game, (3,2), True)
    >>> is_alive(game, (3,2))
    True
    >>> set_alive(game, (3,2), False)
    >>> is_alive(game, (3,2))
    False
    """

    if alive==True :
        board[p]=True
    elif alive==False:
        board[p]=False
  

    
def get_size(board):
    """Size of the game board.

    board -- game board.

    Returns n whether the board represents a game board n x n.

    Examples:

    >>> get_size(board(4))
    4
    >>> get_size(board(10))
    10
    """

    from math import sqrt
    return int(sqrt(len(board)))



def copy_board(board):
    """Copy of the game board.

    board -- game board.

    Returns a new game board whic is copy of the game board

    Examples:

    >>> game = board(10)
    >>> set_alive(game, (4,7), True)
    >>> game2 = copy_board(game)
    >>> game2 is game
    False
    >>> is_alive(game2, (4,7))
    True
    """

    return {x:y for x,y in board.items()}



def get_iterator(board):
    """Iterator for parsing elements of the game board.

    board -- game board.

    Returns iterator which gives the board cells starting from the cells
    of the row 0: (0,0), (0,1), (0,2),..., after following the cells of
    the row 1: (1,0), (1,1), (1,2),... etc. until all the cells are finished.
    For every cell,iterator returns the position and the boolean value
    True or False depending on whether is alive or not.

    Examples:

    >>> game = board(3)
    >>> set_alive(game, (2, 1), True)
    >>> for cell in get_iterator(game):
    ...     print(cell)
    ... 
    ((0, 0), False)
    ((0, 1), False)
    ((0, 2), False)
    ((1, 0), False)
    ((1, 1), False)
    ((1, 2), False)
    ((2, 0), False)
    ((2, 1), True)
    ((2, 2), False)
    """

    ls=[]
    for x,y in board.items():
        ls.append((x,y))
    return ls


def print_board(board):
    """Prints the game board.

    board -- game board.

    Prints the board of the game where with black sqaure
    (unicode character 11035) displayed the alive cells, and
    with white (unicode character 11036) the deads.

    Examples:

    >>> game = board(5)
    >>> set_alive(game, (0,0), True)
    >>> set_alive(game, (2,2), True)
    >>> set_alive(game, (4,4), True)
    >>> set_alive(game, (3,4), True)
    >>> set_alive(game, (0,4), True)
    >>> print_board(game)
    ⬛⬜⬜⬜⬛
    ⬜⬜⬜⬜⬜
    ⬜⬜⬛⬜⬜
    ⬜⬜⬜⬜⬛
    ⬜⬜⬜⬜⬛
    """ 

    for x in range(get_size(board)):
        s=''
        for y in range(get_size(board)):
            if board[x,y]==True:
                s+=chr(11035)
            elif board[x,y]==False:
                s+=chr(11036)
        print(s)



def neighbors(p):
    """Neighbor cells.

    p -- position of the cell (tuple of the format (i,j)).

    Returns a set, containing the locations of neigbor cells
     of p. The returning set does not contain cell p.

    Examples:

    >>> neighbors((3,2))
    {(3, 3), (3, 1), (2, 1), (2, 3), (4, 3), (2, 2), (4, 2), (4, 1)}
    >>> neighbors((0,0))
    {(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1)}
    >>> neighbors((0,10))
    {(-1, 9), (1, 10), (-1, 11), (0, 11), (-1, 10), (1, 9), (0, 9), (1, 11)}
    """

    set_neighbors=set()
    i=p[0]-1
    while i<=p[0]+1:
        j=p[1]-1
        while j<=p[1]+1:
            set_neighbors.add((i,j))
            j+=1
        i+=1
    set_neighbors.remove(p)
    return set_neighbors


def place_blinker(board, p = (0,0)):
    """Blinker placement.

    board -- game board.
    p -- placement cell (tuple (i,j) with default value (0,0))

    Place 3 alive bodies to board
    In neighbor cells of the same column, starting from position p and
    proceeding to the bottom lines.

    Examples:
    
    >>> game = board(5)
    >>> place_blinker(game)
    >>> print_board(game)
    ⬛⬜⬜⬜⬜
    ⬛⬜⬜⬜⬜
    ⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜
    >>> place_blinker(game, (1,2))
    >>> print_board(game)
    ⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜
    ⬛⬜⬛⬜⬜
    ⬜⬜⬛⬜⬜
    ⬜⬜⬜⬜⬜
    >>> place_blinker(game, (4,4))
    >>> print_board(game)
    ⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜
    ⬛⬜⬛⬜⬜
    ⬜⬜⬛⬜⬜
    ⬜⬜⬜⬜⬛
    """

    for i in range(p[0],p[0]+3):
        set_alive(board,(i,p[1]),True)



def place_glider(board, p = (0,0)):
    """Glider placement.

    board -- game board.
    p -- placement cell (tuple (i,j) with default value (0,0))

    Places 5 alive bodies to board in shapes of glider
    starting from th elocation p, as shown in the example below.
    Note that the same cell p is not alive.
    
    Examples:

    >>> game = board(7)
    >>> place_glider(game)
    >>> print_board(game)
    ⬜⬜⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜⬜⬜
    ⬜⬛⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    >>> place_glider(game, (3,3))
    >>> print_board(game)
    ⬜⬜⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜⬜⬜
    ⬜⬛⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬛⬜⬛⬜
    ⬜⬜⬜⬜⬛⬛⬜
    ⬜⬜⬜⬜⬜⬜⬜
    """

    set_alive(board,(p[0],p[1]+2),True)
    set_alive(board,(p[0]+1,p[1]),True)
    set_alive(board,(p[0]+1,p[1]+2),True)
    set_alive(board,(p[0]+2,p[1]+1),True)
    set_alive(board,(p[0]+2,p[1]+2),True)



def tick(board):
    """The game goes one step further to the next generation.

    board -- game board.

    Changes the board by passing a generation
    ccording to the rules of Game of Life.

    Examples:

    >>> game = board(6)
    >>> place_glider(game)
    >>> place_blinker(game, (3,4))
    >>> print_board(game)
    ⬜⬜⬛⬜⬜⬜
    ⬛⬜⬛⬜⬜⬜
    ⬜⬛⬛⬜⬜⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬛⬜
    >>> tick(game)
    >>> print_board(game)
    ⬜⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬛⬛⬛⬜⬜
    ⬜⬜⬜⬛⬜⬜
    ⬜⬜⬜⬛⬛⬛
    ⬜⬜⬜⬜⬜⬜
    """

    n=get_size(board)
    board2=copy_board(board)
    for k,v in board2.items():
        a=0
        for y in neighbors(k):
            if y[0]>=0 and y[1]>=0 and y[0]<n and y[1]<n:
                if board2[y]==True:
                    a+=1
        if board2[k]==True:
            if a<=1:
                board[k]=False
            elif a>=4:
                board[k]=False
        else:
            if a==3:
                board[k]=True



if __name__ == '__main__':
    """Plays the game for a specific initial placement for 100 generations.
     The board of the game displays in every step.
    """

    # Initial board
    game = board(10)
    place_blinker(game, (1,2))
    place_glider(game, (2,4))

    from time import sleep


    for x in range(1,100):
        tick(game)
        print_board(game)
        print('\n')
        sleep(1)
