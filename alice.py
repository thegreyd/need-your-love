from itertools import combinations_with_replacement

def find_sum_in_list(numbers, target):
    results = []
    for x in range(len(numbers)+1):
        results.extend(
            [   
                combo for combo in combinations_with_replacement(numbers ,x)  
                    if sum(combo) == target
            ]   
        )   

    return results

input_string="""
10 10 40
1 2 3 4 5 6 7 8 9 10
5 9 12.5 15.6 18.5 21.3 23.8 26.2 28.5 30.7 
"""

if __name__ == "__main__":
    
    s1=input_string.split()
    n,k,l=int(s1[0]),int(s1[1]),int(s1[2])
    s2=[int(x) for x in s1[3:3+k]]
    s3=[float(x) for x in s1[3+k:]]
    
    combo_list={}
    i=0
    while i<len(s2):
        combo_list[s2[i]]=s3[i]
        i+=1
    
    all_prices=[]
    for y in find_sum_in_list(s2,n):
        sum=0
        for i in y:
            sum+=combo_list[i]
        if sum<=l:
            all_prices.append(sum) 
    
    print(all_prices)
    
    if(all_prices):
        print("Profit is {}".format(max(all_prices)-min(all_prices)))
    else:
        print("Urgently Call Bob!")