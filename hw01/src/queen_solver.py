def solve_n_queens(n: int) -> list[list[str]]:
    """
    求解 N 皇后问题，返回所有合法的棋盘布局
    :param n: 皇后数量（棋盘大小 n×n）
    :return: 所有合法解，每个解是一个字符串列表，代表一行棋盘
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    # 用于快速判断列、主对角线、副对角线是否被占用
    col_used = [False] * n
    diag1_used = [False] * (2 * n - 1)  # 主对角线（行-列）
    diag2_used = [False] * (2 * n - 1)  # 副对角线（行+列）

    def backtrack(row: int):
        if row == n:
            # 找到一个解，将棋盘转换为字符串列表存入结果
            solution = [''.join(row) for row in board]
            result.append(solution)
            return
        
        for col in range(n):
            # 计算当前位置对应的对角线索引
            d1 = row - col + (n - 1)  # 偏移避免负数
            d2 = row + col
            
            # 检查当前位置是否安全
            if not col_used[col] and not diag1_used[d1] and not diag2_used[d2]:
                # 放置皇后
                board[row][col] = 'Q'
                col_used[col] = True
                diag1_used[d1] = True
                diag2_used[d2] = True
                
                # 递归处理下一行
                backtrack(row + 1)
                
                # 回溯：撤销操作
                board[row][col] = '.'
                col_used[col] = False
                diag1_used[d1] = False
                diag2_used[d2] = False

    backtrack(0)
    return result

# 测试函数
if __name__ == "__main__":
    # 测试 4 皇后
    solutions_4 = solve_n_queens(4)
    print(f"4 皇后问题共有 {len(solutions_4)} 个解：")
    for i, sol in enumerate(solutions_4):
        print(f"解 {i+1}:")
        for row in sol:
            print(row)
        print()
    
    # 测试 8 皇后
    solutions_8 = solve_n_queens(8)
    print(f"8 皇后问题共有 {len(solutions_8)} 个解")