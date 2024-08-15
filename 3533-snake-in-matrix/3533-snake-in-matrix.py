class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        a=j=0
        for command in commands:
            if command == 'RIGHT':
                j+=1
            elif command == 'LEFT':
                j-=1
            elif command == 'UP':
                a-=1
            elif command == 'DOWN':
                a+=1
        return a*n+j