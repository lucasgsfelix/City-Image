import numpy as np
import pandas as pd

def generate_gaussian_distribution(mean, stdev, amount_classes):
    """


    """

    # matriz - category x category
    return np.random.normal(mean, stdev, size=(amount_classes, amount_classes)).astype(int)


if __name__ == '__main__':


    #df = pd.read_table()

    # PRE-PROCESSING CONSTRAINTS
    # the transition must ocurr on the same social day - 05:00 AM to 05:00 AM
    # cannot be for the same place
    # the time interval between the transactions must be 4 hours


    # in the original paper the authors construct ten different random visits graphs
    # where the weight contains the same number of transations that are present in
    # the original G, which is the users mobility graph
    # after the random visits graphs are constructs it is verified if
    # the graphs weights distribution follows a normal distribution
    # if it follows, then we compute the mean and de std. dev. for the edges weight
    # based on this we calculate the
    # indifference interval:
    # (mean - 3 * std dev, mean + 3 * std dev)
    # which must contains 99.73% of the edges values, due to the normal distribution
    # rejection interval: (users does not make such transaction)
    # (-infitiy, mean - 3 * std dev)
    # favorites interval: (users are most likely to make suck transaction)
    # (mean + 3 * std dev, infinity)
    # Why do ten graphs? To ensure the randomness do not be a trouble our tests?


    amount_classes, amount_instances = 10, 1000000

    # defining the amount of executions to calculate the mean and std of the matrix
    amount_exe = amount_classes

    # count the amount of transitions between one category and another
    # I have as input a matrix with the following format
    # category_from, category_to
    real_visits_frequency = np.zeros((amount_classes, amount_classes))

    users_mobility = np.random.randint(0, amount_classes, (amount_instances, 2))

    for source, destiny in users_mobility:

        real_visits_frequency[source, destiny] += 1

    random_vists = np.array([generate_gaussian_distribution(np.mean(real_visits_frequency),
                                                            np.std(real_visits_frequency),
                                                            amount_classes)
                                                            for _ in range(0, amount_exe)])

    min_indifference = np.mean(random_vists) - 3 * np.std(random_vists)

    max_indifference = np.mean(random_vists) + 3 * np.std(random_vists)

    index_true = np.where(((real_visits_frequency >= min_indifference) &
                           (real_visits_frequency <= max_indifference)))

    real_visits_frequency[index_true] = 0


