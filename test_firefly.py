import numpy as np

from firefly import Firefly

def rosenbrock(param):
  f = 0

  for i in range(len(param) - 1):
    f += (100 * (param[i + 1] - param[i]**2)**2 + (1 - param[i])**2)

  return f


def test_init():
  swarm = Firefly(function = rosenbrock, population = 10, bounds= np.array([[-5,5],[-5,5]]), light_absorption = 0.5, randomisation_param = 0.5)
  expected_search_bounds = np.array([[0, 1], [0, 1]])
  expected_parameter_bounds = np.array([[-5, 5], [-5, 5]])

  for i in range(len(expected_search_bounds)):
    if expected_search_bounds[i][0] != swarm.bounds[i][0] or swarm.bounds[i][1] != swarm.bounds[i][1]:
      return "incorrect bounds on search space. recieved {}, expected {}".format(swarm.bounds, expected_search_bounds)

  for i in range(len(expected_parameter_bounds)):
    if expected_parameter_bounds[i][0] !=  swarm.limits[i][0] or expected_parameter_bounds[i][1] != swarm.limits[i][1]:
      return "incorrect bounds on parameter space. recieved {}, expected{}".format(swarm.limits, expected_parameter_bounds)

  return True


