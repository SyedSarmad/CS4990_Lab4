import copy
import random
import math
import numpy as np
import pandas as pd


if __name__ == "__main__":
    # Getting the data from the csv file
    df = pd.read_csv("pokedexCopy.csv")

    # Create an empty list
    data = []

    # Iterate over each row
    for index, rows in df.iterrows():
        # Create list for the current row
        my_list = [rows['ID'], rows['NAME'], rows['VARIANT (IF ANY)'], rows['TYPE 1'], rows['TYPE 2 (IF ANY)'],
                   rows['TOTAL'], rows['HP'], rows['ATTACK'], rows['DEFENSE'],
                   rows['SPEED ATTACK'], rows['SPEED DEFENSE'], rows['SPEED']]

        # append the list to the final list
        data.append(my_list)

    # Print the list
    print("printing out the full list with each object:")
    print(data)

    # parameters for the lloyd's function
    columns = [3, 4, 11]

    data = [[row[c] for c in columns] for row in data]

    print("\nNew data with only the relevant columns...")
    print(data)

