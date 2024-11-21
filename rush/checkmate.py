def checkmate(board):
    # แปลง string ของกระดานเป็น list ของ string (แต่ละ row)
    board = board.strip().split('\n')
    n = len(board)

    # หาตำแหน่งของ King ('K')
    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return

    x, y = king_pos

    # ระบุการเคลื่อนไหวของแต่ละหมาก
    directions = {
        'P': [(1, -1), (1, 1)],  # Pawn
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # Bishop
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],  # Rook
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],  # Queen
    }

    for piece, moves in directions.items():
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == piece:
                    print("Success")
                    return
                if board[nx][ny] != '.':  # เจอหมากอื่น
                    break
                if piece == 'P':  # Pawn เดินได้แค่ช่องแรก
                    break
                nx += dx
                ny += dy

    print("Fail")
