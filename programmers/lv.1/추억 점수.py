#https://school.programmers.co.kr/learn/courses/30/lessons/176963

#사진에 나오는 인물마다 설정된 점수를 더한다

def solution(name, yearning, photos):
    answer = []
    
    for photo in photos:
        sum=0
        for pho in photo:
            if pho in name:
                sum+=yearning[name.index(pho)]
        answer.append(sum)
    return answer
