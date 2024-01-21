positions = ['G','G','G','-','B','B','B']
print("Current status of the game:")
print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6]")
print(positions)

while True:
    pos = input("Press 'q' to quit . Enter position of the piece:")
    if pos.lower() == 'q':
        print("You Lose")
        break
    pos = int(pos)
    if pos<0 or pos>6:
        print("Invalid move")
        continue
    if positions[pos] == '-':
        print("Invalid Move")
        continue
    empty_index = 0
    if positions[pos] == 'G':
        if pos+1<=6 and positions[pos+1]=='-':
            empty_index= pos+1
        elif pos+2 <=6 and positions[pos+2]=='-':
            empty_index=pos+2
        else:
            print ("Invalid move")
            continue
    elif positions[pos]== 'B':
        if pos-1 >=0 and positions[pos-1]== '-':
            empty_index= pos-1
        elif pos-2 and positions[pos-2]=='-':
            empty_index= pos-2
        else:
            print(" Invalid Move")
            continue
    positions[pos], positions[empty_index]= positions[empty_index], positions[pos] 
    print ("[ 0,   1,   2,   3 ,  4 ,  5 ,  6 ]") 
    print (positions)
    if positions == ['B','B','B','-','G','G','G']:
        print ("YOU WIN")
        break
    if positions == ['G', 'G', 'B', 'B', 'B', 'G', '-']:
        print ("YOU LOSE")    
        break
    
    if positions == ['G', 'G', 'B', 'B', 'G', 'B', '-']:
        print ("YOU LOSE")    
        break
    if positions == ['-', 'B', 'G', 'G', 'G', 'B', 'B']:
        print ("YOU LOSE")    
        break
    if positions == ['-', 'G', 'G', 'G', 'B', 'B', 'B']:
        print ("YOU LOSE")    
        break