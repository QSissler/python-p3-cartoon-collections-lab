def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i + 1}. {dwarves[i]}")

def summon_captain_planet(planeteer_calls):
    return [f"{planeteer_calls[index].capitalize()}!" for index in range(len(planeteer_calls))]

def long_planeteer_calls(calls):
    for i in range(len(calls)):
        if(len(calls[i]) > 4):
            return True

    return False

def find_the_cheese(words):
    for i in range(len(words)):
        if words[i] == 'cheddar' or words[i] == 'gouda' or words[i] == 'camembert':
            return words[i]

    return None