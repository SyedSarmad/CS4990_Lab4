import copy
import random
import math
import numpy as np
import pandas as pd

DISCRETIZATION_FACTOR = 5


def discretizeData(df):
    totalFactor = math.ceil(max(df['TOTAL'])/ (DISCRETIZATION_FACTOR + 1))
    HPFactor = math.ceil(255/ (DISCRETIZATION_FACTOR + 1))
    attackFactor = math.ceil(max(df['ATTACK'])/ (DISCRETIZATION_FACTOR + 1))
    defenseFactor = math.ceil(max(df['DEFENSE']) / (DISCRETIZATION_FACTOR + 1))
    spattackFactor = math.ceil(max(df['SPECIAL ATTACK']) / (DISCRETIZATION_FACTOR + 1))
    spdefenseFactor = math.ceil(max(df['SPECIAL DEFENSE']) / (DISCRETIZATION_FACTOR + 1))
    speedFactor = math.ceil(max(df['SPEED']) / (DISCRETIZATION_FACTOR + 1))
    df['TOTAL'] = df['TOTAL'] // totalFactor
    df['HP'] = df['HP'] // HPFactor
    df['ATTACK'] = df['ATTACK'] // attackFactor
    df['DEFENSE'] = df['DEFENSE'] // defenseFactor
    df['SPECIAL ATTACK'] = df['SPECIAL ATTACK'] // spattackFactor
    df['SPECIAL DEFENSE'] = df['SPECIAL DEFENSE'] // spdefenseFactor
    df['SPEED'] = df['SPEED'] // speedFactor

    return df

def cleanVariants(df):
    df['NAME'] = np.where(df['VARIANT (IF ANY)'] == 'None', df['NAME'], df['NAME'] + ' (' + df['VARIANT (IF ANY)'] + ')')
    return df


if __name__ == "__main__":
    # Getting the data from the csv file
    df = pd.read_csv("pokedexCopy.csv")

    df = discretizeData(df)
    df = cleanVariants(df)
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
    columns = [3, 4, 11]

    data = [{row[c] for c in columns} for row in data]

    print("\nNew data with only the relevant columns...")
    print(data)

