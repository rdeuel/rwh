# FSM Simulation

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        # QUIZ: You fill this out!
        # Is there a valid edge?
        # If so, take it.
        # If not, return False.
        # Hint: recursion.
        try:
            newNode = edges[(current, letter)]
            return fsmsim(string[1:], newNode, edges, accepting)
        except KeyError:
            return False


print (fsmsim("aaa111",1,edges,accepting))
print (fsmsim("111aaa",1,edges, accepting))


