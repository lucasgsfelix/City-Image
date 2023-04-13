import numpy as np
import pandas as pd

def generate_gaussian_distribution(amount_classes):
    """


    """

    row = np.random.randint(0, amount_classes, 1)

    column = np.random.randint(0, amount_classes, 1)

    # matriz - category x category
    return row, column


if __name__ == '__main__':


    #df = pd.read_table()

    amount_classes, amount_instances = 10, 1000

    random_vists = np.zeros((amount_classes, amount_classes))

    for _ in range(0, amount_instances):

        ## generates gaussian distribution of visits
        row, column = generate_gaussian_distribution(amount_classes)

        random_vists[row, column] += 1

    # count the amount of transitions between one category and another
    # I have as input a matrix with the following format
    # category_from, category_to
    real_visits_frequency = np.zeros((amount_classes, amount_classes))

    users_mobility = np.random.randint(0, amount_classes, (amount_instances, 2))

    #print(users_mobility)

    #exit()

    for source, destiny in users_mobility:

        real_visits_frequency[source, destiny] += 1


    # montar a matriz da seguinte forma:
    # normalizing by min/max value
    # values that are bigger than 0 will have a bigger amount of visits
    # values that are smaller than 0 will have a smaller amount of visits
    # ((amount of real transitions ij)  - (amount of random transitions ij))
    # /
    # max(((amount of real transitions)  - (amount of random transitions)))

    substract_matrix = real_visits_frequency - random_vists

    heatmap_matrix = substract_matrix/np.max(substract_matrix)

    print(heatmap_matrix)


