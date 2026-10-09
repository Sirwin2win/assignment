scores = [12, 15, 11, 18, 20, 14, 16, 13]
def describe(scores,display=True):
    # count
    count = len(scores)
    # mean
    total = 0
    i=0
    while(i<count):
        total += scores[i]
        i +=1

    mean = total/count
    # std
    mean_squares = 0
    j = 0
    while(j<count):
        mean_squares += (scores[j]-mean)**2
        j +=1
    variance = mean_squares/(count-1)
    std = variance**0.5
    #minimum
    minNumber = scores[0]
    k = 1
    while(k<count):
        if(scores[k]<minNumber):
            minNumber = scores[k]
    
        k +=1
    # maximum
    maxNumber = scores[0]
    l = 1
    while(l<count):
        if(scores[l]>maxNumber):
            maxNumber = scores[l]
        l +=1
    def percentile(scores, p):
        if not scores:
            return None
        if p < 0 or p > 100:
            raise ValueError("Percentile must be between 0 and 100")
        
        sorted_data = sorted(scores)
        k = (len(sorted_data) - 1) * (p / 100.0)
    
        f = int(k)
        c = k - f

        if f + 1 < len(sorted_data):
            return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
        else:
            return sorted_data[f]
    q75 = percentile(scores,75)
    q25 = percentile(scores,25)
    q50 = percentile(scores,50)
    results = {
    "count": count,
    "mean": mean,
    "std": std,
    "min": minNumber,
    "25%": q25,
    "50%": q50,
    "75%": q75,
    "max": maxNumber
    }

    if display:
        print("Summary Statistics")
        print("------------------")
        print(f"count    {count}")
        print(f"mean     {mean:.2f}")
        print(f"std      {std:.2f}")
        print(f"min      {minNumber:.2f}")
        print(f"25%      {q25:.2f}")
        print(f"50%      {q50:.2f}")
        print(f"75%      {q75:.2f}")
        print(f"max      {maxNumber:.2f}")

        return results
results = describe(scores)
print(results)