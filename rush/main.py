from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1
    board = """\
..
.K\
""" 
    print(checkmate(board))  # Expected Output: Success

if __name__ == "__main__":
    main()