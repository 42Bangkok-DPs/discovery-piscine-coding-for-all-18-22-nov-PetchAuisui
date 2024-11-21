from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)  # Expected Output: Success

if __name__ == "__main__":
    main()