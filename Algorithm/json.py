# <question> find survivor


돌의내구도 = [1, 2, 1, 4]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

# print specific key's values with comprehension
# 각 key별로 출력하기
print([i["이름"] for i in 독])
print([i["점프력"] for i in 독])
print([i["몸무게"] for i in 독])

# solve with function because of need values of survivor(answer)
# 리턴값으로 생존자를 출력해야해서 함수로 문제 풀이
def find_survivor(독, 돌의내구도):
    answer = [i["이름"] for i in 독]
    # print(answer)
    for i in 독:
        독의위치 = 0

        # It was wrong code from lecture. I found it!
        # 의문이 안풀려 강의게시판에 질문했는데 잘못된 코드였다.
        # while 독의위치 < len(돌의내구도)-1:
        while 독의위치 <= len(돌의내구도):
            독의위치 += int(i["점프력"])

            # minus 1 because 돌의내구도 starts from 0
            # 돌의내구도는 0부터 시작하기 때문에 -1 한다.
            돌의내구도[독의위치-1] -= int(i["몸무게"])
            if 돌의내구도[독의위치-1] <0:
                # (1) replace value to fail
                answer[answer.index(i["이름"])] = "fail"
                # (2) delete value in list
                # remove = O(n), del = 0(1)    => use del
                del answer[answer.index(i["이름"])]
                break

    # (1) return answer except fail
    return [i for i in answer if i!= "fail"]
    # (2) return answer
    return answer

print(find_survivor(독.copy(), 돌의내구도.copy()))






