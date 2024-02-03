
def get_num_seq1(n):

    num = 2 * n + 2
    start = n * 3
    for i in range(0, num):
        print(start, end=" ")
        start += 2
    
    
def draw_grid(n):
    for x in range(0, n+1):
        for y in range(0, n+2):
            pass
            # 绘制橙色方块
    if n % 2 == 0:
        pass
        # 绘制绿色方块
    else:
        pass
        # 绘制蓝色方块
        
def get_num_seq2(n):
    start = 0
    delta = 2
    for i in range(2 * n):
        if i == n:
            start = n
            delta = 1
        print(start, end=" ")
        start += delta
            

if __name__ == "__main__":
    get_num_seq2(6)
