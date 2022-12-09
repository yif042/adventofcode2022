# solve file for day02 problem 


def part1():
    # A Rock
    # B Paper
    # C Scissors

    # X Rock
    # Y Paper
    # Z Scissors

    wins = ["CX", "AY", "BZ"]
    draws = ["AX", "BY", "CZ"]
    loses = ["BX", "CY", "AZ"]

    outcome = {x:6 for x in wins} | {x:3 for x in draws} | {x:0 for x in loses}

    shapes = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3,
    }

    res = 0
    with open("input", "r") as f:
        for line in f.readlines():
            op, me = line.split()
            res += (shapes[me] + outcome[f"{op}{me}"])


    print("part1", res)

def part2():
    # A Rock
    # B Paper
    # C Scissors

    # X lose
    # Y draw
    # Z win
    outcome = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }

    rocks = ["BX", "AY", "CZ"]
    papers = ["CX", "BY", "AZ"]
    scissors = ["AX", "CY", "BZ"]

    shapes = {r:1 for r in rocks} | {p:2 for p in papers} | {s:3 for s in scissors}

    res = 0
    with open("input", "r") as f:
        for line in f.readlines():
            op, me = line.split()
            res += (outcome[me] + shapes[f"{op}{me}"])

    print("part2", res)







part1()
part2()


