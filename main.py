import copy
import random
import math
import numpy as np
import pandas as pd

from patterns import apriori

DISCRETIZATION_FACTOR = 5


def discretizeData(df):
    totalFactor = math.ceil(max(df['TOTAL']) / (DISCRETIZATION_FACTOR))
    HPFactor = math.ceil(255/ (DISCRETIZATION_FACTOR))
    attackFactor = math.ceil(max(df['ATTACK']) / (DISCRETIZATION_FACTOR))
    defenseFactor = math.ceil(max(df['DEFENSE']) / (DISCRETIZATION_FACTOR))
    spattackFactor = math.ceil(max(df['SPECIAL ATTACK']) / (DISCRETIZATION_FACTOR))
    spdefenseFactor = math.ceil(max(df['SPECIAL DEFENSE']) / (DISCRETIZATION_FACTOR))
    speedFactor = math.ceil(max(df['SPEED']) / (DISCRETIZATION_FACTOR))
    print(spattackFactor)
    df['TOTAL'] = df['TOTAL'] // totalFactor + 1
    df['HP'] = df['HP'] // HPFactor + 1
    df['ATTACK'] = df['ATTACK'] // attackFactor + 1
    df['DEFENSE'] = df['DEFENSE'] // defenseFactor + 1
    df['SPECIAL ATTACK'] = df['SPECIAL ATTACK'] // spattackFactor + 1
    df['SPECIAL DEFENSE'] = df['SPECIAL DEFENSE'] // spdefenseFactor + 1
    df['SPEED'] = df['SPEED'] // speedFactor + 1

    return df

def cleanVariants(df):
    df['NAME'] = np.where(df['VARIANT (IF ANY)'] == 'None', df['NAME'], df['NAME'] + ' (' + df['VARIANT (IF ANY)'] + ')')
    return df

def mergeTypes(df):
    df['TYPE 1'] = np.where(df['TYPE 2 (IF ANY)'] == 'no second type', df['TYPE 1'],
                          df['TYPE 1'] + '-' + df['TYPE 2 (IF ANY)'])
    return df


if __name__ == "__main__":
    # Getting the data from the csv file
    df = pd.read_csv("pokedexCopy.csv")

    df = discretizeData(df)
    df = cleanVariants(df)
    df = mergeTypes(df)
    print(df)

    # Create an empty list
    data = []

    # Iterate over each row
    for index, rows in df.iterrows():
        # Create list for the current row
        my_list = [rows['ID'], rows['NAME'], rows['VARIANT (IF ANY)'], rows['TYPE 1'], rows['TYPE 2 (IF ANY)'],
                   rows['TOTAL'], rows['HP'], rows['ATTACK'], rows['DEFENSE'],
                   rows['SPECIAL ATTACK'], rows['SPECIAL DEFENSE'], rows['SPEED']]

        # append the list to the final list
        data.append(my_list)

    # Print the list
    print("printing out the full list with each object:")
    print(data)

    # parameters for the lloyd's function
    columns = [3, 11]

    data = [{row[c]} for c in columns for row in data]
    print("\nNew data with only the relevant columns...")
    print(data)


    apriori(data, 30/len(data))
