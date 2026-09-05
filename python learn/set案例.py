# 选修足球学生名单

football_set = {"王林", "曾牛", "徐立国", "通天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎鸣", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"通天", "天运子", "韩立", "虎鸣", "姜老道", "紫灵"}

# 找出同时选修了法语和艺术的学生
#方式一：
# fr_ar=french_set.intersection(art_set)
# print(fr_ar)
#方式二：& ---->交集
fr_ar = french_set & art_set
print(fr_ar)
# 找出同时选修了所有四门课程的学生
all_set = football_set & basketball_set & french_set & art_set
print(all_set)

# 找出选修了足球，但是没有选修篮球的学生
#方式一
# fot_set = football_set.difference(basketball_set)
# print(fot_set)

#方式二 - ----->差集
# fot_set = football_set - basketball_set
# print(fot_set)

#方式三：集合推导式 ---> 快速构建集合
fot_set = {i for i in football_set if i not in basketball_set}
print(fot_set)
# 统计每一个学生选修的课程数量
all_student = football_set | basketball_set | french_set | art_set
print(all_student)
all_list = [*football_set, *basketball_set, *french_set,*art_set]
for c in all_student:
    print(f"{c}选修了{all_list.count(c)}门课程")
