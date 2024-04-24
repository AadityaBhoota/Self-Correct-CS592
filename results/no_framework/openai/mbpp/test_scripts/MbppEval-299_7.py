from collections import defaultdict

def max_aggregate(stdata):
    aggregate_scores = defaultdict(int)
    
    for name, score in stdata:
        aggregate_scores[name] += score

    max_name = max(aggregate_scores, key=aggregate_scores.get)
    max_score = aggregate_scores[max_name]
    
    return max_name, max_score

# Test cases




def check(candidate):
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
    assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)

check(max_aggregate)