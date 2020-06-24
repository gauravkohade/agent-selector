import random


def main_func(agent_list, agent_sel_mode):
    avail_agent_list = []
    max_duration = 0

    if agent_sel_mode == 1:
        for x in agent_list:
            if x[0] == True:
                avail_agent_list.append(x)

    elif agent_sel_mode == 2:
        for y in agent_list:
            if y[0] == True:
                if max_duration < y[1]:
                    max_duration = y[1]
        for a in agent_list:
            if a[0] == True and a[1] == max_duration:
                avail_agent_list.append(a)

    elif agent_sel_mode == 3:
        for z in agent_list:
            if z[0] == True:
                avail_agent_list.append(z)

        avail_agent_list = random.choices(avail_agent_list)

    else:
        print("Please  Select an appropriate option!")

    print(avail_agent_list)
