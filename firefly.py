import numpy as np

def convert_to_bounds(bounds, positions):
  values = np.zeros_like(positions)
  
  for i, pos in enumerate(positions):
    for j in range(len(bounds)):
      values[i][j] = bounds[j][0] + ((bounds[j][1] - bounds[j][0]) * pos[j])
  
  return values

class Firefly:

  def __init__(self,
    function,
    population,
    bounds,
    light_absorption,
    randomisation_param):

    self.function = function
    self.population = population
    self.limits = bounds
    self.bounds = np.array([[0,1]] * len(bounds))
    self.gamma = light_absorption
    self.alpha = randomisation_param
    self.position = None
    self.attractiveness = None
    self.g_fitness = None
    self.g_best = None
    self.cur_fitness = None
   
  def initialise_swarm(self):
    lower_bounds = self.bounds[:,0]
    upper_bounds = self.bounds[:,1]
    self.position = np.random.uniform(lower_bounds, upper_bounds, [self.population, len(lower_bounds)])
    params = convert_to_bounds(self.limits, self.position)
    self.attractiveness = np.array(list(map(self.function, params)))
    self.g_fitness = self.attractiveness.max
    self.g_best = self.position[np.argmin(self.attractiveness)]


    
