import numpy as np

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
    self.g_fitness = None
    self.g_best = None
    self.cur_fitness = None
   
    
