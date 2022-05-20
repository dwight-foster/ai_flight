from mlagents_envs.environment import UnityEnvironment
env = UnityEnvironment(file_name="FlightSim/FlightSim.sln", seed=1, side_channels=[])
# Start interacting with the environment.
env.reset()
behavior_names = env.behavior_specs.keys()