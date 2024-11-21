from checkmate import checkmate
def main():
    # กำหนดกระดานหมากรุก (board) โดยตรง
    board = """\
R...
.K..
..P.
...."""
    
    # เรียกใช้ฟังก์ชัน checkmate เพื่อตรวจสอบกระดาน
    checkmate(board)

if __name__ == "__main__":
    main()
