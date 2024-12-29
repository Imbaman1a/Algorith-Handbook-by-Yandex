from collections import defaultdict
n = int(input())
words = [input().strip() for _ in range(n)]

word_counts = defaultdict(int)
mask_counts = defaultdict(int)

total_set = set()
ans = 0
visited = set()
length = len(words[0])
for word in words:
    
    temp_set = set()
    for i in range(length):
        mask = word[:i] + '_' + word[i+1:]
        temp_set.add(mask)
        
    for item in temp_set:
        
        if item in total_set:
        
            if word not in visited:
                ans += mask_counts[item]
            
            else:
                repeat = word_counts[word]
                ans += mask_counts[item] - repeat
                #маска повторного слова, нужно посчитать с учётом повтора
                
    
        mask_counts[item] += 1

        
        total_set.add(item)
            
    word_counts[word] += 1            
    visited.add(word)
    
    #total_set = temp_set | total_set
    
    

    
    
print(ans)    
