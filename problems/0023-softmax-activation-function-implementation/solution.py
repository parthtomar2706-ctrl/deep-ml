import math
import numpy as np
def softmax(scores: list[float]) -> list[float]:
    # Your code here
    # scores=np.array(scores)
    # res=[]
    # b=0;
    # for j in range(len(scores)):
    #     b+=math.exp(scores[j])
    # for i in range(len(scores)):
    #     res.append(math.exp(scores[i])/b)
    # return res
    max_score = max(scores)

    exp_scores = [math.exp(x - max_score) for x in scores]

    total = sum(exp_scores)

    return [x / total for x in exp_scores]        
    pass