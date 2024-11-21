from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1
    board1 = """\
R...
.K..
..P.
....\
"""
    print(checkmate(board1))  # Expected Output: Success

if __name__ == "__main__":
    main()