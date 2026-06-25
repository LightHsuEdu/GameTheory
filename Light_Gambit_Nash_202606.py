# -*- coding: utf-8 -*-

# python 3.12.10
# pygambit 16.6.0

import pygambit
from fractions import Fraction
import re

allGameModelList = []

htmlTextStr = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Nash Equilibria</title>
<style>
    body { font-family: Arial, sans-serif; width: 90%; max-width:1600px; margin: 30px auto; color: #333; }
    h2 { color: #000; border-bottom: 2px solid #ccc; padding-bottom: 10px; }
    .game-container { display: flex; align-items: flex-start; gap: 30px; margin-top: 20px; margin-bottom: 30px; }
    .matrix-panel { flex: 0 0 auto; overflow-x: auto; padding-top: 10px; }
    .matrix-panel table { border-collapse: collapse; width: auto; font-size: 1em; }
    .matrix-panel td { padding: 10px 15px; border: 1px solid #ccc; white-space: nowrap; } 
    .results-panel { flex: 1; min-width: 0; background: #f4f4f4; padding: 20px; border-radius: 4px; border: 1px solid #999; }
    .results-panel h3 { margin-top: 0; color: #000; font-size: 1.1em; }
    .results-panel h4 { margin: 10px 0 5px 0; color: #333; font-size: 0.95em; }
    .results-panel code { display: inline-block; }
    .results-panel .solver-desc{ font-size:1em; color: #000; margin-bottom:8px; }
    .hr-dashed { border-top: 1px dashed #999; margin: 40px 0; }
</style>
</head>
<body>
"""

def extractBiMatrix(matrix_BiMtx):
    def mtx_to_fraction(val):
        if isinstance(val, Fraction):
            return val
        if isinstance(val, int):
            return Fraction(val, 1)
        return Fraction(str(val)).limit_denominator()
    matrix1 = [[mtx_to_fraction(cell[0]) for cell in row] for row in matrix_BiMtx]
    matrix2 = [[mtx_to_fraction(cell[1]) for cell in row] for row in matrix_BiMtx]
    return matrix1, matrix2

def numberToFraction(_inputStr):
    result_str = re.sub(r'[-+]?\d*\.\d+', lambda x: str(Fraction(x.group()).limit_denominator()), _inputStr)
    return result_str

# Prisoner's Dilemma
bimatrix_PD = [[(-2, -2), (0, -10)],
               [(-10, 0), (-1, -1)]]                        
p1_mtx, p2_mtx = extractBiMatrix(bimatrix_PD)
print(p1_mtx)
print(p2_mtx)
game = pygambit.Game.from_arrays(p1_mtx, p2_mtx, title = "Prisoner's Dilemma")
game.players[0].label = "Prisoner 1"
game.players["Prisoner 1"].strategies[0].label = "Cooperate"
game.players["Prisoner 1"].strategies[1].label = "Defect"
game.players[1].label = "Prisoner 2"
game.players["Prisoner 2"].strategies[0].label = "Cooperate"
game.players["Prisoner 2"].strategies[1].label = "Defect"
allGameModelList.append(game)

# Battle of the Sexes
bimatrix_BoS = [[(2, 1), (0, 0)],
                [(0, 0), (1, 2)]]
p1_mtx, p2_mtx = extractBiMatrix(bimatrix_BoS)
print(p1_mtx)
print(p2_mtx)
game = pygambit.Game.from_arrays(p1_mtx, p2_mtx, title = "Battle of the Sexes")
game.players[0].label = "Wife"
game.players["Wife"].strategies[0].label = "Shopping"
game.players["Wife"].strategies[1].label = "Prize Fight"
game.players[1].label = "Husband"
game.players["Husband"].strategies[0].label = "Shopping"
game.players["Husband"].strategies[1].label = "Prize Fight"
allGameModelList.append(game)

# Example
bimatrix_Example = [[(9, 9), (0, 8)],
                    [(8, 0), (7, 7)]]
p1_mtx, p2_mtx = extractBiMatrix(bimatrix_Example)
print(p1_mtx)
print(p2_mtx)
game = pygambit.Game.from_arrays(p1_mtx, p2_mtx, title = "Example")
game.players[0].label = "PlayerA"
game.players["PlayerA"].strategies[0].label = "Up"
game.players["PlayerA"].strategies[1].label = "Down"
game.players[1].label = "PlayerB"
game.players["PlayerB"].strategies[0].label = "Left"
game.players["PlayerB"].strategies[1].label = "Right"
allGameModelList.append(game)

# Example 2020
bimatrix_Example2020 = [[(9, 1), (1, 3), (6, 2)],
                        [(7, 5), (3, 4), (4, 6)],
                        [(8, 9), (5, 8), (2, 7)]]
p1_mtx, p2_mtx = extractBiMatrix(bimatrix_Example2020)
print(p1_mtx)
print(p2_mtx)
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

# Three Person - Rock Paper Scissors
p1_mtx = [[[ 0, -1, 1 ],[-1, -2, 0],[ 1, 0, 2]],   [[ 2, 1, 0 ],[ 1, 0, -1],[ 0, -1, -2]],   [[-2, 0, -1],[ 0, 2, 1],[ -1, 1, 0]]]
p2_mtx = [[[ 0, -1, 1],[ 2, 1, 0],[ -2, 0, -1 ]],  [[ -1, -2, 0],[ 1, 0, -1 ],[ 0, 2, 1]],   [[ 1, 0, 2],[ 0, -1, -2],[ -1, 1, 0 ]]]
p3_mtx = [[[ 0, 2, -2],[ -1, 1, 0],[ 1, 0, -1]],   [[ -1, 1, 0],[ -2, 0, 2 ],[ 0, -1, 1 ]],  [[ 1, 0, -1],[ 0, -1, 1],[ 2, -2, 0]]]
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
    print("\n" + "-"*60)
    print("Game Model:  ", _game.title)
    print("-"*60)

    raw_fileHtml = _game.to_html()
    table_start_idx = raw_fileHtml.find("<table")
    matrix_html = raw_fileHtml[table_start_idx:] if table_start_idx != -1 else raw_fileHtml

    game_results_html = ""

    for __player in _game.players:
        print(__player)

    for __strategie in _game.strategies:
        print(__strategie)    

    try:
        nashResults = pygambit.nash.enumpure_solve(_game)
        print("\n➔ enumpure_solve: Compute all pure-strategy Nash equilibria of game.\n")
        if len(nashResults.equilibria) > 0:
            game_results_html += "<div class='solver-desc'>enumpure_solve: Compute all pure-strategy Nash equilibria of game.</div>"
            for item in nashResults.equilibria:
                _rst_val = numberToFraction(str(item))
                print(" "*10 + _rst_val)
                game_results_html += f"<code>{_rst_val}</code><br>"
            game_results_html += "<br>"
    except Exception:
        pass

    try:
        nashResults = pygambit.nash.enummixed_solve(_game, rational=False)
        print("\n➔ enummixed_solve: Compute all mixed-strategy Nash equilibria of a two-player game using the strategic representation.\n")    
        if len(nashResults.equilibria) > 0:
            game_results_html += "<div class='solver-desc'>enummixed_solve: Compute all mixed-strategy Nash equilibria of a two-player game using the strategic representation.</div>"
            for item in nashResults.equilibria:
                _rst_val = numberToFraction(str(item))
                print(" "*10 + _rst_val)
                game_results_html += f"<code>{_rst_val}</code><br>"
            game_results_html += "<br>"
    except Exception:
        pass

    try:
        nashResults = pygambit.nash.lp_solve(_game, use_strategic = True, rational=True)
        print("\n➔ lp_solve: Compute Nash equilibria of a two-player constant-sum game using linear programming.\n")
        if len(nashResults.equilibria) > 0:
            game_results_html += "<div class='solver-desc'>lp_solve: Compute Nash equilibria of a two-player constant-sum game using linear programming.</div>"
            for item in nashResults.equilibria:
                _rst_val = numberToFraction(str(item))
                print(" "*10 + _rst_val)
                game_results_html += f"<code>{_rst_val}</code><br>"
            game_results_html += "<br>"
    except Exception:
        pass

    try:
        nashResults = pygambit.nash.lcp_solve(_game, use_strategic = True, rational=True)
        print("\n➔ lcp_solve: Compute Nash equilibria of a two-player game using linear complementarity programming.\n")
        if len(nashResults.equilibria) > 0:
            game_results_html += "<div class='solver-desc'>lcp_solve: Compute Nash equilibria of a two-player game using linear complementarity programming.</div>"
            for item in nashResults.equilibria:
                _rst_val = numberToFraction(str(item))
                print(" "*10 + _rst_val)
                game_results_html += f"<code>{_rst_val}</code><br>"
            game_results_html += "<br>"
    except Exception:
        pass

    try:
        nashResults = pygambit.nash.logit_solve(_game)
        print("\n➔ logit_solve: Compute Nash equilibria of a game using the logit quantal response equilibrium correspondence.\n")
        if len(nashResults.equilibria) > 0:
            game_results_html += "<div class='solver-desc'>logit_solve: Compute Nash equilibria of a game using the logit quantal response equilibrium correspondence.</div>"
            for item in nashResults.equilibria:
                _rst_val = numberToFraction(str(item))
                print(" "*10 + _rst_val)
                game_results_html += f"<code>{_rst_val}</code><br>"
            game_results_html += "<br>"
    except Exception:
        pass

    try:
        nashResults = pygambit.nash.ipa_solve(_game)
        print("\n➔ ipa_solve: Compute Nash equilibria of a game using iterated polymatrix approximation.\n")
        if len(nashResults.equilibria) > 0:
            game_results_html += "<div class='solver-desc'>ipa_solve: Compute Nash equilibria of a game using iterated polymatrix approximation.</div>"
            for item in nashResults.equilibria:
                _rst_val = numberToFraction(str(item))
                print(" "*10 + _rst_val)
                game_results_html += f"<code>{_rst_val}</code><br>"
            game_results_html += "<br>"
    except Exception:
        pass

    try:
        nashResults = pygambit.nash.gnm_solve(_game)
        print("\n➔ gnm_solve: Compute Nash equilibria of a game using a global Newton method.\n")
        if len(nashResults.equilibria) > 0:
            game_results_html += "<div class='solver-desc'>gnm_solve: Compute Nash equilibria of a game using a global Newton method.</div>"
            for item in nashResults.equilibria:
                _rst_val = numberToFraction(str(item))
                print(" "*10 + _rst_val)
                game_results_html += f"<code>{_rst_val}</code><br>"
            game_results_html += "<br>"
    except Exception:
        pass    

    if not game_results_html:
        game_results_html = "<h4>No Nash equilibrium solution found.</h4>"

    htmlTextStr += f"<h2>{_game.title}</h2>\n"
    htmlTextStr += "<div class='game-container'>\n"

    htmlTextStr += f"""
    <div class='matrix-panel'>
        {matrix_html}
    </div>
    """

    htmlTextStr += f"""
    <div class='results-panel'>
        <h3>Nash Equilibrium Results:</h3>
        {game_results_html}
    </div>
    """
        
    htmlTextStr += "</div>\n"
    htmlTextStr += "<hr class='hr-dashed'>\n"

htmlTextStr += "</body>\n</html>"
with open("Light_Gambit_Nash_Payoff_Matrix_2026.html", "w", encoding="utf-8") as file_to_write:
    file_to_write.write(htmlTextStr)

print("\n\n---------- Game Over ----------")
