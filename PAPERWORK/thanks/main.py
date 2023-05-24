from time import sleep


def thanks_parents():
    print('致父母：')
    print('感谢我的父母在本科四年一直以来的精神支持，'
          '义无反顾地信任我的每个判断和决定，让我随时充满自信；'
          '感谢我的父母在本科四年一直以来的经济支持，让我可以衣食无忧地专注于学业。'
          '我永远不会忘记你们的每一通电话的问候和每一箱寄来的水果。\n')


def thanks_soulmate():
    print('致文珩：')
    print('感谢我的伴侣在我的本科期间对我始终如一的勉励和信任，'
          '也感谢我们在2019年立下的约定。'
          '如果没有这个约定，我可能不会在每次计组实验那么卖力，'
          '可能不会在朋友们都去嗨皮的时候去联系科研机会。'
          '是这个约定支撑我翻过每一个看似不可逾越的大山，'
          '是你不变的陪伴激励我爆发出自己最大的可能性。'
          '虽然本科四年有一半以上的时间我们之间都隔着半个地球的距离，'
          '但是若心联结，殊途终会同归。'
          '回望四年，每一次分别和重逢，每一次欢喜和悲伤，都万分值得。\n')


def thanks_teachers():
    print('致老师：')

    teachers = ['王莉莉教授', 'Prof. Xing-Dong Yang', '李俊教授', 'Prof. Jian Zhao', '徐枫教授']
    institutions = ['北京航空航天大学', 
                    'Simon Fraser University', 
                    '北京师范大学', 
                    'University of Waterloo', 
                    '清华大学']

    teacher_dict = {i: t for i, t in zip(institutions, teachers)}

    for i, t in teacher_dict.items():
        print("我想对{0}的{1}致谢。".format(i, t), end='')
        print(
            '感谢王老师在我的漫漫求索中为我提供的莫大帮助和对我的研究能力的培育。'
            '在虚拟现实实验室的日子可以算是我本科最有意义的日子，'
            '因为我在这里确定了自己的兴趣方向。' 
            if t == '王莉莉教授' else
            '感谢Prof. Yang在几乎素不相识的情况下信任并接纳我进入他的人机交互实验室，'
            '并且总是像关切自己的学生一样询问我的近况和难处。'
            '这段经历使我充分坚定了出国深造的决心。' 
            if t == 'Prof. Xing-Dong Yang' else
            '感谢李老师在我的本科期间带领我发表了第一篇国际学术论文，'
            '让我体会到学术研究能够带给我的无限乐趣和成就感。' 
            if t == '李俊教授' else
            '感谢Prof. Zhao对我学术能力的认可，为我提供宝贵的研究生学习机会。'
            if t == 'Prof. Jian Zhao' else
            '感谢徐老师在我大一时慷慨地为我提供有关计算机视觉和图形学的教导；'
            '徐老师潜移默化教授给我的方法与理念影响了我整个本科的学习思路和历程。\n' 
            if t == '徐枫教授' else '')


def thanks_seniors():
    print('致前辈：')

    seniors = ['刘小龙博士', '徐哲尔博士']
    institutions = ['北京航空航天大学', 'Dartmouth College']

    senior_dict = {i: t for i, t in zip(institutions, seniors)}

    for i, t in senior_dict.items():
        print("我想对{0}的{1}致谢。".format(i, t), end='')
        print(
            '感谢小龙师兄在科研中对我的各种问题不厌其烦的解答。' 
            if t == '刘小龙博士' else
            '感谢哲尔师兄在暑期研究中带领我有条不紊地攻破一个个难点。\n' 
            if t == '徐哲尔博士' else '')


def thanks_music():
    print('致音乐：')
    print('感谢北航交响乐团，让我在本科四年时间里一直有机会坚持自己的爱好，'
          '让我可以在紧张忙碌的课业之余享受音乐、卸下负担。\n')


def thanks_opportunities():
    print('致机会：')
    print('感谢所有我遇到的机会，机会即是一切。\n')


def thanks_me():
    print('致自己：')
    print('感谢自己，从未放弃任何大小之事。\n')


if __name__ == '__main__':
    thanks_parents()
    sleep(5)
    thanks_soulmate()
    sleep(5)
    thanks_teachers()
    sleep(5)
    thanks_seniors()
    sleep(5)
    thanks_music()
    sleep(5)
    thanks_opportunities()
    sleep(5)
    thanks_me()
    