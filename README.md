# agent-selector
This project is an assignment submission for the Python Developer Internship by Support Genie.

# Problem Statement for the Assignment
Agent selector
You are given the following data for agents 
agent
is_available
available_since (the time since the agent is available)
roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.) 

When an issue comes in we need to present the issue to 1 or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. In “all available mode” the issue is presented to all agents so they pick the issue if they want. In least busy the issue is presented to the agent that has been available for the longest. In random mode we randomly pick an agent. An issue also has one or many roles (sales/support e.g.). Issues are presented to agents only with matching roles.

Please write a function that takes an input the list of agents with their data, agent selection mode and returns a list of agents the issue should be presented to.  

Note - We have had many people asking questions if the function needs one more argument. In the simple case no, but in a real implementation yes it will need an issues list or an existing issues queue. Please do add a queue of issues to the function if you want to implement the advanced case.

Also note that is_available is a boolean value.


# Basic scenario solution and how to run the demo
We have created the main function as requested in `simple_case/agent_selector.py`.
You can run `simple_case/demo_agent_selector.py` to see a demo with sample data

# Advanced scenario solution and how to run the demo
We have created the main function as requested in `advanced_case/agent_selector.py`.
You can run `advanced_case/demo_agent_selector.py` to see a demo with sample data