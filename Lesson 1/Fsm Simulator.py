# FSM Simulation

edges = {(1, 'a'): 2,
         (2, 'a'): 2,
         (2, '1'): 3,
         (3, '1'): 3}

accepting = [3]


def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in edges:
            stage = edges[(current, letter)]
            return fsmsim(string[1:], stage, edges, accepting)
        else:
            return False
        # QUIZ: You fill this out!
        # Is there a valid edge?
        # If so, take it.
        # If not, return False.
        # Hint: recursion.


print(fsmsim("aaa111", 1, edges, accepting))
# >>> True

#  r"q*"
# edges = {
#     (1, "q"):1,
# }
#
# accepting = [1]


# r"[a-b][c-d]?"
# edges = {
#     (1,'a'):2,
#     (1,'b'):2,
#     (2,'c'):3,
#     (2,'d'):3
# }
# accepting = [2, 3]
