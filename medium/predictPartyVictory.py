class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        length = len(senate)
        senate_list = list(senate)
        if length == 1:
            return 'Radiant' if senate == 'R' else 'Dire'
        vic_flag = False
        i = 0
        while True:
            s = senate_list[i % length]
            if s:
                if vic_flag is True:
                    return 'Radiant' if s == 'R' else 'Dire'
                point_index = i + 1
                while point_index < length + i:
                    t_point = point_index % length
                    if senate_list[t_point] and senate_list[t_point] != s:
                        senate_list[t_point] = False
                        break
                    point_index += 1
                if point_index == length + i:
                    vic_flag = True
            i += 1


class SolutionB:
    def predictPartyVictory(self, senate: str) -> str:
        mapping = {'R': 'Radiant', 'D': 'Dire'}
        mapping_rd = {'R': 'D', 'D': 'R'}
        boss = senate[0]
        boss_attack = 0
        boss_defence = 0
        for s in senate:
            if s == boss:
                # 遇见同类boss是恢复点，恢复攻击力和防御力
                boss_attack += 1
                boss_defence += 1
            else:
                # 遇见挑战者
                if boss_attack > 0:
                    # boss有攻击力就主动攻击
                    boss_attack -= 1
                elif boss_defence > 0:
                    # boss没有攻击力，但是有防御力
                    boss_defence -= 1
                if boss_defence == 0 and boss_attack == 0:
                    # boss没有攻击力也没有防御力，挑战者挑战成功成为boss
                    # 挑战成功后，因为刚才主动攻击boss，攻击力为0，防御力为１
                    boss = mapping_rd[boss]
                    boss_attack = 0
                    boss_defence = 1

        return mapping[boss]


from collections import deque


class SolutionC(object):
    def predictPartyVictory(self, senate: str) -> str:
        mapping = {'R': 'Radiant', 'D': 'Dire'}
        senate_queue = deque(senate)  # 待行使权力议员列表
        handle_queue = deque()  # pk擂台列表
        while len(senate_queue) > 0:  # 无待行使权力议员则结束
            curr_party = senate_queue.popleft()
            if len(handle_queue) > 0:
                pre_party = handle_queue.pop()
                if curr_party != pre_party:  # 由于pk台最近议员是敌对党并且敌对党议员拥有先序，curr_party议员被禁用
                    senate_queue.append(pre_party)  # 重新添加到待行使权力议员列表
                else:  # 由于pk台最近议员是同党，不做处理，但是要重新添加回pk台
                    handle_queue.append(pre_party)
                    handle_queue.append(curr_party)
            else:
                handle_queue.append(curr_party)
            print('s_q: [%s] h_q: [%s]' % (' '.join(senate_queue), ' '.join(handle_queue)))
        return mapping[handle_queue[0]]


if __name__ == '__main__':
    sol = SolutionC()
    print(sol.predictPartyVictory('DDRRR'))
