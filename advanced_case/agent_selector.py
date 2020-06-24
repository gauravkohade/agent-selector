import random


def main_func(agent_list, agent_sel_mode, issue_roles):
    avail_agent_list = []
    least_busy_agent = []

    for x in agent_list:
        if x[0] == True and set(issue_roles).issubset(set(x[2])):
            avail_agent_list.append(x)
            if x[1] >= avail_agent_list[0][1]:
                least_busy_agent = x

    if len(avail_agent_list) == 0:
        return 'no agent found'

    if agent_sel_mode == 1:
        return avail_agent_list
    elif agent_sel_mode == 2:
        return least_busy_agent if len(least_busy_agent) else 'no agent found'
    elif agent_sel_mode == 3:
        return random.choice(avail_agent_list)
    else:
        return "Please Select an appropriate option!"
