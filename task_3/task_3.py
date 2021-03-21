tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


def appearance(intervals):
    lesson_start = intervals['lesson'][0]
    lesson_end = intervals['lesson'][1]

    tutor = intervals['tutor']
    pupil = intervals['pupil']
    
    if len(pupil) < len(tutor):
        first = pupil
        second = tutor
    else:
        first = tutor
        second = pupil
    
    subtrahend = 0
    minuend = 0

    i, j = 0,0
    sum = 0
    a = False

    while True:
        if lesson_start > first[i] and lesson_start > first[i+1]:
            i += 2
            continue

        if lesson_start > second[j] and lesson_start > second[j+1]:
            j += 2
            continue

        if lesson_start > first[i] and lesson_start < first[i+1]:
            first[i] = lesson_start
            continue

        if lesson_start > second[j] and lesson_start < second[j+1]:
            second[j] = lesson_start
            continue

        if first[i+1] > lesson_end:
            first[i+1] = lesson_end
            continue

        if second[j+1] > lesson_end:
            second[j+1] = lesson_end
            a = True
            continue
        
        
        if second[j] > second[j-2] and second[j+1] < second[j-1]:
            second[j+1] = second[j-1]
            second[j] = second[j-2]
            
            j += 2

        if j > 0 and second[j] < second[j-1]:
            second[j] = second[j-1]

        elif (second[j] >= first[i] and second[j+1] <= first[i+1]):
            subtrahend = second[j]
            minuend = second[j+1]
            sum += minuend - subtrahend
            
            j += 2

            if j == len(second):
                break
            if a:
                break

        elif (second[j] < first[i] and second[j+1] <= first[i+1]):
            subtrahend = first[i]
            minuend = second[j+1]
            sum += minuend - subtrahend
            
            j += 2

            if j == len(second):
                break

        elif (second[j] >= first[i] and second[j+1] > first[i+1]):
            subtrahend = second[j]
            minuend = first[i+1]
            sum += minuend - subtrahend
            
            i += 2

            if i == len(second):
                break

        elif (second[j] > first[i] and second[j+1] < first[i+1]):
            subtrahend = first[i]
            minuend = first[i+1]
            sum += minuend - subtrahend
            
            i += 2

            if i == len(second):
                break

    return sum
        
if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'