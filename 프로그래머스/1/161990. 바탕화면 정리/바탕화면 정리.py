def solution(wallpaper):
    
    minX = len(wallpaper[0])
    minY = len(wallpaper)
    maxX = -1
    maxY = -1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                if i <= minY:
                    minY = i
                if i >= maxY:
                    maxY = i
                if j <= minX:
                    minX = j
                if j >= maxX:
                    maxX = j
                    
    
    return [minY, minX, maxY+1, maxX+1]