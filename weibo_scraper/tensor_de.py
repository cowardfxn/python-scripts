#!/usr/bin/python
# encoding: utf-8
# Author: fanxn
# Date: 2018/6/9

import tensorflow as tf
import tensorflow.contrib.eager as tfe
import numpy as np
import time

tfe.enable_eager_execution()

print("TensorFlow version: {}".format(tf.__version__))
print("Available GPUs: {}".format(tfe.num_gpus()))
print("Available CPUs: {}".format(tfe.num_cpus()))

# assert tfe.num_gpus() > 0, "You need a GPU with the CUDA etc to run this."


def run_differential_evolution(solution_size=5,
                               population_size=1000,
                               iteration_count=100,
                               print_results=False,
                               differential_weight=1.0,
                               crossover_probability=0.5,
                               lower=0.0,
                               upper=1.0
                               ):
    while population_size % 3 != 0:
        population_size += 1

    target_solution = np.zeros((solution_size))
    mean = np.mean([lower, upper])
    std = np.std([lower, upper])
    population = tf.random_normal(shape=[population_size, solution_size], mean=mean, stddev=std)

    for i in range(iteration_count):
        random_1 = np.arange(0, population_size)
        np.random.shuffle(random_1)
        random_2 = np.arange(0, population_size)
        np.random.shuffle(random_2)
        random_3 = np.arange(0, population_size)
        np.random.shuffle(random_3)

        random_trio_1 = tf.reshape(tf.gather(population, random_1), shape=[-1, 3, solution_size])
        random_trio_2 = tf.reshape(tf.gather(population, random_2), shape=[-1, 3, solution_size])
        random_trio_3 = tf.reshape(tf.gather(population, random_3), shape=[-1, 3, solution_size])

        mutation_trios = tf.concat([random_trio_1, random_trio_2, random_trio_3], axis=0)
        vectors_1, vectors_2, vectors_3 = tf.unstack(mutation_trios, axis=1, num=3)
        doners = vectors_1 + differential_weight * (vectors_2 - vectors_3)

        crossover_probabilities = tf.random_uniform(minval=0, maxval=1, shape=[population_size, solution_size])

        trial_population = tf.where(crossover_probabilities < crossover_probability, x=doners, y=population)
        trial_fitness = tf.sqrt(tf.reduce_mean(tf.square(tf.subtract(trial_population, target_solution)), axis=1))
        og_fitness = tf.sqrt(tf.reduce_mean(tf.square(tf.subtract(population, target_solution)), axis=1))
        if print_results:
            print(tf.gather(og_fitness, tf.argmin(og_fitness)))

        population = tf.where(trial_fitness < og_fitness, x=trial_population, y=population)


tf.reset_default_graph()
with tf.device("/cpu:0"):
    run_differential_evolution(iteration_count=50,
                               solution_size=5,
                               crossover_probability=0.1,
                               print_results=True
                               )
