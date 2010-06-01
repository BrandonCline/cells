'''Genes in asexual reproduction.

Totally made-up, has no basis in genetic algorithms b/c I have no
background in that area.
'''

import random

class Gene(object):
  def __init__(self, parent):
    '''Clone this gene from the parent gene.'''
    self.val = parent.val

  def spawn(self):
    '''Copy this gene, introducing mutations probabilistically.'''
    new = self.__class__(self)
    new.mutate()
    return new

  def mutate(self):
    perturb = self.gen_perturb()
    val = self.val + perturb
    self.val = min(max(val, self.min_cap), self.max_cap)


def make_normally_perturbed_gene(sigma, minc=0, maxc=1):
  class NormallyPerturbedGene(Gene):
    min_cap = minc
    max_cap = maxc
    def gen_perturb(self):
      return random.gauss(0, sigma)
  return NormallyPerturbedGene


class InitializerGene(object):
  '''A fake gene, used to initialize things.'''
  def __init__(self, val):
    self.val = val
