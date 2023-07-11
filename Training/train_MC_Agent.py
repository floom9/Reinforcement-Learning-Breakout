def train_agent(agent, env, episodes, render=False):
    rewards = []

    for episode in range(episodes):
        # Reset environment and get initial state
        state = env.reset()
        done = False

        # Record the transitions
        transitions = []
        total_reward = 0

        while not done:
            # Choose action based on the agent's policy
            action = agent.act(state)

            # Execute the action in the environment
            next_state, reward, done = env.step(action)
            # Record the transition
            transitions.append((state, action, reward))

            total_reward += reward
            state = next_state

        # After each episode, update the agent's Q values
        agent.update_Q(transitions, total_reward)

        # Store the reward
        rewards.append(total_reward)

        # Reduce the epsilon (Exploration vs. Exploitation trade-off)
        agent.update_epsilon(episode)

        if render:
            env.render()

        if episode % 100 == 0:
            print(f'Episode {episode}/{episodes}: Reward {total_reward}')

    return rewards
