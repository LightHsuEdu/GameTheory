# -*- coding: utf-8 -*-

import numpy as np
from fractions import Fraction

def calculate_nash_equilibria(matrix1, matrix2):
    rows, cols = matrix1.shape
    nash_equilibria = []

    # pure strategy Nash equilibria
    for i in range(rows):
        for j in range(cols):
            if is_pure_nash_equilibrium(matrix1, matrix2, i, j, rows, cols):
                nash_equilibria.append(f'Pure strategy: ({Player1_Strategies[i]}, {Player2_Strategies[j]})')

    # mixed strategy Nash equilibrium ( 2x2 games only )
    if rows == 2 and cols == 2:
        mixed_equilibrium = calculate_mixed_equilibrium2x2(matrix1, matrix2)
        if mixed_equilibrium:
            nash_equilibria.append(f'Mixed strategy: {mixed_equilibrium}')

    return nash_equilibria

def is_pure_nash_equilibrium(matrix1, matrix2, row, col, rows, cols):
    for i in range(rows):
        if matrix1[i][col] > matrix1[row][col]:
            return False
    for j in range(cols):
        if matrix2[row][j] > matrix2[row][col]:
            return False
    return True

def calculate_mixed_equilibrium2x2(matrix1, matrix2):
    p = (matrix2[1, 1] - matrix2[1, 0]) / (matrix2[0, 0] - matrix2[0, 1] - matrix2[1, 0] + matrix2[1, 1])
    q = (matrix1[1, 1] - matrix1[0, 1]) / (matrix1[0, 0] - matrix1[1, 0] - matrix1[0, 1] + matrix1[1, 1])

    if np.isnan(p) or np.isnan(q) or p < 0 or p > 1 or q < 0 or q > 1:
        return None

    # return {:.4f} formats the number 
    #return f'{Player1}: ({Player1_Strategies[0]}: {p:.4f}, {Player1_Strategies[1]}: {(1-p):.4f}), {Player2}: ({Player2_Strategies[0]}: {q:.4f}, {Player2_Strategies[1]}: {(1-q):.4f})'

    # return fractions and simplify
    p_fraction = Fraction(str(float(p))).limit_denominator()
    q_fraction = Fraction(str(float(q))).limit_denominator()
    one_minus_p_fraction = Fraction(str(float(1-p))).limit_denominator()
    one_minus_q_fraction = Fraction(str(float(1-q))).limit_denominator()
    return f'{Player1}: ({Player1_Strategies[0]}: {p_fraction}, {Player1_Strategies[1]}: {one_minus_p_fraction}), {Player2}: ({Player2_Strategies[0]}: {q_fraction}, {Player2_Strategies[1]}: {one_minus_q_fraction})'

#########################################
# BoS

# 定义 Player
Player1 = "妻子"
Player2 = "丈夫"

# 定义 Strategy
Player1_Strategies = ['购物', '看比赛']
Player2_Strategies = ['购物', '看比赛']

matrix1 = np.array([[2, 0],
                    [0, 1]])
matrix2 = np.array([[1, 0],
                    [0, 2]])
nash_equilibriaBos = calculate_nash_equilibria(matrix1, matrix2)

print("\n* Battle of the Sexes:\n")
for item in nash_equilibriaBos:
    print(item)

#########################################    
# Example

# 定义 Player
Player1 = "参与人A"
Player2 = "参与人B"

# 定义 Strategy
Player1_Strategies = ['U', 'D']
Player2_Strategies = ['L', 'R']

matrix3 = np.array([[9, 0],
                    [8, 7]])
matrix4 = np.array([[9, 8],
                    [0, 7]])
nash_equilibria = calculate_nash_equilibria(matrix3, matrix4)

print("\n* Example:\n")
for item in nash_equilibria:
    print(item)
    
