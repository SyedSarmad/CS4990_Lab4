import copy
import random
import math
import numpy as np
import pandas as pd


if __name__ == "__main__":
    # Getting the data from the csv file
    df = pd.read_csv("pokedexCopy.csv")

    # Getting max values for all numerical attributes
    total_max = df['TOTAL'].max()
    hp_max = df['HP'].max()
    attack_max = df['ATTACK'].max()
    defense_max = df['DEFENSE'].max()
    speed_max = df['SPEED'].max()
    speed_attack_max = df['SPEED ATTACK'].max()
    speed_defense_max = df['SPEED DEFENSE'].max()

    # Getting min values for all numerical attributes
    total_min = df['TOTAL'].min()
    hp_min = df['HP'].min()
    attack_min = df['ATTACK'].min()
    defense_min = df['DEFENSE'].min()
    speed_min = df['SPEED'].min()
    speed_attack_min = df['SPEED ATTACK'].min()
    speed_defense_min = df['SPEED DEFENSE'].min()

    # Create an empty list
    row_list = []

    # Iterate over each row
    for index, rows in df.iterrows():
        # Normalization formula: zi = (xi – min(x)) / (max(x) – min(x))
        norm_total = (rows['TOTAL'] - total_min) / (total_max - total_min)
        norm_hp = (rows['HP'] - hp_min) / (hp_max - hp_min)
        norm_speed = (rows['SPEED'] - speed_min) / (speed_max - speed_min)
        norm_attack = (rows['ATTACK'] - attack_min) / (attack_max - attack_min)
        norm_defense = (rows['DEFENSE'] - defense_min) / (defense_max - defense_min)
        norm_speed_attack = (rows['SPEED ATTACK'] - speed_attack_min) / (speed_attack_max - speed_attack_min)
        norm_speed_defense = (rows['SPEED DEFENSE'] - speed_defense_min) / (speed_defense_max - speed_defense_min)

        # Create list for the current row
        my_list = [rows['ID'], rows['NAME'], rows['VARIANT (IF ANY)'], rows['TYPE 1'], rows['TYPE 2 (IF ANY)'],
                   norm_total, norm_hp, norm_attack, norm_defense,
                   norm_speed_attack, norm_speed_defense, norm_speed]

        # append the list to the final list
        row_list.append(my_list)

    # Print the list
    print("printing out the full list with each object:")
    print(row_list)

    # parameters for the lloyd's function
    columns_to_cluster = [7, 8]
    k_number_clusters = 3
    n = 10
    centers = None
    eps = None