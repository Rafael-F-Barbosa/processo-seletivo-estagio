#     *       @file: mesa-redonda.py
#     *     @author: Rafael Fernandes Barbosa 
#     *@description: Problem "mesa-redonda" - OBI2019 - Sênior - Fase 3  


# Create chair a chair node class
class ChairNode:
    def __init__(self, chairIndex, nextChair):
        self.used = False
        self.chairIndex = chairIndex
        self.next = nextChair

class ChairList:
    def __init__(self, chair):
        self.head = chair
        self.initial = chair

# Initialize list
initialChair = ChairNode(0, None)
chairList = ChairList(initialChair)

# Fill list
numberOfChairs = 3 # In this problem we have three chairs
for x in range(1, numberOfChairs):
    newChair = ChairNode(x, None)

    # Close list
    newChair.next = chairList.initial

    # Add new chair
    chairList.head.next = newChair
    chairList.head = newChair



# Solve problem
def roundedTable(A, B):
    # Define Ana's chair
    chairSelectedAna = chairList.initial
    for _ in range(A):
        chairSelectedAna = chairSelectedAna.next
    chairSelectedAna.used = True
    # Define Beatriz's Chair
    chairSelectedBia = chairList.initial
    for _ in range(B):
        chairSelectedBia = chairSelectedBia.next
    if(chairSelectedBia.used):
        chairSelectedBia = chairSelectedBia.next
    chairSelectedBia.used = True
    
    # Define Carolina's Chair
    chairSelectedCarol = chairList.initial
    for _ in range(numberOfChairs):
        if(not chairSelectedCarol.used):
            break
        chairSelectedCarol = chairSelectedCarol.next
    
    # Return Carolina's chair
    return chairSelectedCarol.chairIndex


# Main
print("Carolina vai sentar na cadeira:", roundedTable(3, 9))
