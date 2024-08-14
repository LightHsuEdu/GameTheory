# -*- coding: utf-8 -*-

# 测试版本
# python 3.12.2
# pygambit-16.2.0

import pygambit 
import numpy as np

allGameModelList = []
htmlTextStr = ""

# Prisoner's Dilemma
p1_mtx = np.array([[-2, 0], [-10, -1]])
p2_mtx = np.array([[-2, -10], [0, -1]])
game = pygambit.Game.from_arrays(p1_mtx, p2_mtx, title = "Prisoner's Dilemma")
game.players[0].label = "Prisoner 1"
game.players["Prisoner 1"].strategies[0].label = "Betray"
game.players["Prisoner 1"].strategies[1].label = "Silent"
game.players[1].label = "Prisoner 2"
game.players["Prisoner 2"].strategies[0].label = "Betray"
game.players["Prisoner 2"].strategies[1].label = "Silent"
allGameModelList.append(game)

# Battle of the Sexes
p1_mtx = np.array([[2, 0], [0, 1]])
p2_mtx = np.array([[1, 0], [0, 2]])
game = pygambit.Game.from_arrays(p1_mtx, p2_mtx, title = "Battle of the Sexes")
game.players[0].label = "Wife"
game.players["Wife"].strategies[0].label = "Shopping"
game.players["Wife"].strategies[1].label = "Prize Fight"
game.players[1].label = "Husband"
game.players["Husband"].strategies[0].label = "Shopping"
game.players["Husband"].strategies[1].label = "Prize Fight"
allGameModelList.append(game)

# Example
p1_mtx = np.array([[9, 0], [8, 7]])
p2_mtx = np.array([[9, 8], [0, 7]])
game = pygambit.Game.from_arrays(p1_mtx, p2_mtx, title = "Example")
game.players[0].label = "PlayerA"
game.players["PlayerA"].strategies[0].label = "Up"
game.players["PlayerA"].strategies[1].label = "Down"
game.players[1].label = "PlayerB"
game.players["PlayerB"].strategies[0].label = "Left"
game.players["PlayerB"].strategies[1].label = "Right"
allGameModelList.append(game)

# Example 2020
p1_mtx = np.array([[9, 1, 6], [7, 3, 4], [8, 5, 2]])
p2_mtx = np.array([[1, 3, 2], [5, 4, 6], [9, 8, 7]])
game = pygambit.Game.from_arrays(p1_mtx, p2_mtx, title = "Example 2020")
game.players[0].label = "PlayerA"
game.players["PlayerA"].strategies[0].label = "Up"
game.players["PlayerA"].strategies[1].label = "Middle"
game.players["PlayerA"].strategies[2].label = "Down"
game.players[1].label = "PlayerB"
game.players["PlayerB"].strategies[0].label = "Left"
game.players["PlayerB"].strategies[1].label = "Center"
game.players["PlayerB"].strategies[2].label = "Right"
allGameModelList.append(game)

# Three person - Rock Paper Scissors
p1_mtx = np.array([[[ 0, -1, 1 ],[-1, -2, 0],[ 1, 0, 2]],   [[ 2, 1, 0 ],[ 1, 0, -1],[ 0, -1, -2]],   [[-2, 0, -1],[ 0, 2, 1],[ -1, 1, 0]]])
p2_mtx = np.array([[[ 0, -1, 1],[ 2, 1, 0],[ -2, 0, -1 ]],  [[ -1, -2, 0],[ 1, 0, -1 ],[ 0, 2, 1]],   [[ 1, 0, 2],[ 0, -1, -2],[ -1, 1, 0 ]]])
p3_mtx = np.array([[[ 0, 2, -2],[ -1, 1, 0],[ 1, 0, -1]],   [[ -1, 1, 0],[ -2, 0, 2 ],[ 0, -1, 1 ]],  [[ 1, 0, -1],[ 0, -1, 1],[ 2, -2, 0]]])
game = pygambit.Game.from_arrays(p1_mtx, p2_mtx, p3_mtx, title = "Three person - Rock Paper Scissors")
game.players[0].label = "PlayerA"
game.players["PlayerA"].strategies[0].label = "Rock"
game.players["PlayerA"].strategies[1].label = "Paper"
game.players["PlayerA"].strategies[2].label = "Scissors"
game.players[1].label = "PlayerB"
game.players["PlayerB"].strategies[0].label = "Rock"
game.players["PlayerB"].strategies[1].label = "Paper"
game.players["PlayerB"].strategies[2].label = "Scissors"
game.players[2].label = "PlayerC"
game.players["PlayerC"].strategies[0].label = "Rock"
game.players["PlayerC"].strategies[1].label = "Paper"
game.players["PlayerC"].strategies[2].label = "Scissors"
allGameModelList.append(game)

# solve and print

for _game in allGameModelList:
    print("\n==========  Game Model: ", _game.title, "\n")

    fileHtml = _game.write(format='html')

    htmlTextStr += fileHtml
    htmlTextStr += "<p>"
    htmlTextStr += '''<hr class="hr-dashed" style="width: 100%">'''
    htmlTextStr += "<p>"
    fileSgame = _game.write(format='sgame')

    try:
        nashResults = pygambit.nash.enumpure_solve(_game, use_strategic = True)
        print("==== enumpure_solve: Compute all pure-strategy Nash equilibria of game.\n")
        for item in nashResults.equilibria:
            print(item)
    except:
        pass
    
    try:
        nashResults = pygambit.nash.enummixed_solve(_game, use_lrs = False, rational=False)
        print("\n==== enummixed_solve: Compute all mixed-strategy Nash equilibria of a two-player game using the strategic representation.\n")
        for item in nashResults.equilibria:
            print(item)
    except:
        pass

    try:
        nashResults = pygambit.nash.lp_solve(_game, use_strategic = True, rational=False)
        print("\n==== lp_solve: Compute Nash equilibria of a two-player constant-sum game using linear programming.\n")
        for item in nashResults.equilibria:
            print(item)
    except:
        pass

    try:
        nashResults = pygambit.nash.lcp_solve(_game, use_strategic = True, rational=False)
        print("\n==== lcp_solve: Compute Nash equilibria of a two-player game using linear complementarity programming.\n")
        for item in nashResults.equilibria:
            print(item)
    except:
        pass

    try:
        nashResults = pygambit.nash.ipa_solve(_game)
        print("\n==== ipa_solve: Compute Nash equilibria of a game using iterated polymatrix approximation.\n")
        for item in nashResults.equilibria:
            print(item)
    except:
        pass

    try:
        nashResults = pygambit.nash.gnm_solve(_game)
        print("\n==== gnm_solve: Compute Nash equilibria of a game using a global Newton method.\n")
        for item in nashResults.equilibria:
            print(item)
    except:
        pass    

# 输出 html
htmlTextStr = htmlTextStr.replace("</center>", "").replace("<center>", "").replace("h1", "h2")
with open("Light_Gambit_Nash_Payoff_Matrix.html", "w", encoding="utf-8") as file_to_write:
    file_to_write.write(htmlTextStr)

print("\n---------- Game Over ----------")


