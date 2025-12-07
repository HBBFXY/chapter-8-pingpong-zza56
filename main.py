import random

def simulate_round(server_ability):
    """
    模拟单个回合的比赛
    :param server_ability: 发球方的能力值（0-1）
    :return: True表示发球方赢得该回合，False表示交换发球权
    """
    # 生成0到1之间的随机回合概率值
    round_prob = random.random()
    # 发球方能力值高于随机值则赢回合，否则交换发球权
    return server_ability > round_prob

def simulate_game(ability_a, ability_b):
    """
    模拟一局完整的乒乓球比赛
    :param ability_a: 球员A的能力值
    :param ability_b: 球员B的能力值
    :return: 'A'表示A赢，'B'表示B赢
    """
    score_a = 0  # A的得分
    score_b = 0  # B的得分
    server = 'A'  # 初始发球方为A
    
    while True:
        # 模拟当前回合
        if server == 'A':
            round_win = simulate_round(ability_a)
        else:
            round_win = simulate_round(ability_b)
        
        # 根据回合结果更新得分或交换发球权
        if round_win:
            if server == 'A':
                score_a += 1
            else:
                score_b += 1
        else:
            # 交换发球权
            server = 'B' if server == 'A' else 'A'
        
        # 判断是否满足获胜条件（先到11分且领先至少2分）
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 'A' if score_a > score_b else 'B'

def main():
    """
    主函数：接收输入，模拟多场比赛，输出结果
    """
    # 接收用户输入（做了异常处理，确保输入有效）
    while True:
        try:
            ability_a = float(input("请输入球员A的能力值（0-1之间的小数）："))
            if not 0 <= ability_a <= 1:
                print("能力值必须在0到1之间，请重新输入！")
                continue
            
            ability_b = float(input("请输入球员B的能力值（0-1之间的小数）："))
            if not 0 <= ability_b <= 1:
                print("能力值必须在0到1之间，请重新输入！")
                continue
            
            match_count = int(input("请输入模拟比赛的场次："))
            if match_count <= 0:
                print("比赛场次必须是正整数，请重新输入！")
                continue
            break
        except ValueError:
            print("输入格式错误！请输入有效的数字。")
    
    # 初始化获胜场次
    win_a = 0
    win_b = 0
    
    # 模拟指定场次的比赛
    for _ in range(match_count):
        winner = simulate_game(ability_a, ability_b)
        if winner == 'A':
            win_a += 1
        else:
            win_b += 1
    
    # 计算胜率
    rate_a = (win_a / match_count) * 100
    rate_b = (win_b / match_count) * 100
    
    # 输出结果
    print(f"\n模拟比赛数量: {match_count}")
    print(f"球员A获胜场次: {win_a} ({rate_a:.1f}%)")
    print(f"球员B获胜场次: {win_b} ({rate_b:.1f}%)")

# 程序入口
if __name__ == "__main__":
    main()
