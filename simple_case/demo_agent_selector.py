
from agent_selector_exercise2 import main_func


agent_list = [[True, 4, ['marketing', 'sales']], [False, 1, 'sales'],
              [True, 3, 'tech Support'], [True, 6, 'marketing'], [
                  True, 2, 'tech support'],
              [True, 4, 'sales'], [True, 5, 'marketing'], [
                  False, 3, 'tech support'],
              [True, 8, 'sales'], [False, 2, 'marketing']]


agent_sel_mode = int(input("""Please select the agent selection mode-
1)all selection mode
2)least busy mode
3)random mode \n"""))


if __name__ == "__main__":
    main_func(agent_list, agent_sel_mode)
