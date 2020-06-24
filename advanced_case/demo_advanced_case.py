from agent_selector import main_func

agent_list = [[True, 4, ['marketing', 'spanish']],
              [False, 1, ['sales', 'hindi']],
              [True, 3, ['support', 'english']],
              [True, 6, ['marketing', 'french']],
              [True, 2, ['support', 'hindi']],
              [True, 4, ['sales', 'english']],
              [True, 5, ['marketing', 'english']],
              [False, 3, ['support', 'french']],
              [True, 8, ['sales', 'french']],
              [True, 2, ['marketing', 'english']],
              ]

specialisation_list = ['marketing', 'support', 'sales']
language_list = ['spanish', 'hindi', 'english', 'french']

specialisation = int(input("""\nplease select the issue related department-
1)marketing
2)support
3)sales \n"""))

language = int(input("""\nplease select the issue related department-
1)spanish
2)hindi
3)english
4)french \n"""))

issue_roles = [specialisation_list[specialisation-1],
               language_list[language-1]]

agent_sel_mode = int(input("""\nplease select the agent selection mode-
1)all selection mode
2)least busy mode
3)random mode \n"""))

if __name__ == "__main__":
    output = main_func(agent_list, agent_sel_mode, issue_roles)
    print(output)
