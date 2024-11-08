def ask_yes_no_question(question):
    """询问一个是或否的问题并获取用户输入"""
    while True:
        answer = input(question + " (想&不想): ")
        if answer == "想":
            return True
        elif answer == "不想":
            return False
        else:
            print("请输入'想'或'不想'。")

def ask_text_question(question, correct_answer):
    """询问一个文本问题并检查答案是否正确"""
    answer = input(question + " ")
    if answer == correct_answer:
        print(f"答对啦, {response()}")
        return True
    else:
        print(f"唔...答错了哟，小笨蛋~正确答案是: {correct_answer}")
        return False

def response():
    """根据不同情况返回相应的回应"""
    responses = ["奖励你一个...赞~", "奖励...咳咳给你...ruarua叭", "奖励你...可以对猫猫提一个条件qwq，唔...或者是，对猫猫做想做的事...？（捂脸）不要太过分~",
                 "奖励...rua猫猫...十分钟~", "奖励你一个...小红花...?还是给你rua一下叭~只许一下哟", "奖励你一个...揉揉脑袋~"]
    return responses[0]

def punishment():
    """根据不同情况返回相应的惩罚"""
    punishments = ["惩罚你晚上！当猫猫的抱枕叭！", "惩罚你...24小时内不许欺负猫猫！", "惩罚你...连续三天当猫猫抱枕！！", "就罚你！唔...给猫猫...做个全身按摩叭！",
                   "惩罚加重！伸出爪爪...挠你脚心！"]
    return punishments[0]

print('你好吖，这里是猫猫')
print('想...玩个游戏嘛')

if ask_yes_no_question("想玩游戏吗"):
    print("哎嘿~这就太好啦")
    print('那猫猫先考考你几个问题~')
    print("咳咳，听好啦！请问...你认为猫猫是不是笨蛋")
    if ask_text_question("(期待ing:)请输入你的答案叭~是&不是：", "不是"):
        print('哎嘿~谢谢啦，那么...接下来，就真正开始咯~')
        print('（挑选ing）就这个啦，这是很简单的叭qwq~')
        print('请说出π的小数点后八位~')
        if ask_text_question("请输入答案~：", "14159265"):
            print('呜哇，答对啦~' + response())
            print('哼哼，接下来就要加大难度咯~')
            print('（思考ing）找到啦，准备好了嘛~')
            print('被誉为诗鬼的人是...')
            if ask_text_question("请输入答案~：", "李贺"):
                print('恭喜！又答对啦')
                print('奖励...咳咳给你...ruarua叭，')
                print('嗯哼...今天就到这里叭（伸懒腰）猫猫要...睡觉惹...')
            else:
                print(punishment())
        else:
            print('不对不对~答案是...14159265')
            print('哎呀~答错了呀...' + punishment())
            print('好啦好啦~后面还有题qwq~')
            print('这次可要仔细想想哟')
            print('被誉为诗圣的是...')
            if ask_text_question("请输入答案~", "杜甫"):
                print('答对啦,嘿嘿，就知道你不会让猫猫失望哒~')
                print('唔...' + response())
                print('一段时间后')
                print('QAQ！坏蛋下手真重！不玩了！猫猫要去...趴一会......')
            else:
                print('哎呀呀...又不对捏...答案是杜甫呀~')
                print('呼呼~连续两错嘛~这次惩罚就得重点咯~')
                print('就罚你...连续三天当猫猫抱枕！！')
                print('咳咳...应该不过分叭...')
                print('哼哼，要洗香香再跟猫猫睡哟')
                print('猫猫先去洗澡咯~待会见~')
else:
    print('不想嘛...QAQ玩玩嘛~很好玩滴！！')
    if ask_yes_no_question("再考虑一下，想玩吗"):
        print('喵呜~，哎嘿，就知道你会同意的啦~那么...先问个问题！')
        print("咳咳，听好啦！请问...你认为猫猫是不是笨蛋")
        if ask_text_question("(期待ing:)请输入你的答案叭~是&不是：", "不是"):
            print('哎嘿~谢谢啦，那么...接下来，就真正开始咯~')
            print('（挑选ing）就这个啦，这是很简单的叭qwq~')
            print('请听题~99*99等于多少？')
            if ask_text_question("请输入答案~:", "9801"):
                print('哎嘿~，就知道你可以哒~')
                print('奖励一个...小红花...?还是给你rua一下叭~只许一下哟')
                print('嘿嘿，那么我们继续~')
                print('难度升级~')
                print('（寻找ing）这道应该可以...找到啦~')
                print('请问~被誉为诗仙的是~')
                if ask_text_question("请输入答案", "李白"):
                    print('恭喜吖，答对惹~')
                    print('还挺厉害的嘛~，唔...那就奖励你...可以对猫猫提一个条件qwq，唔...或者是，对猫猫做想做的事...？（捂脸）不要太过分~')
                    print('好啦好啦...猫猫累...（瘫软）今天就到这叭~再见吖')
                else:
                    print('嗯哼?在这里错了嘛...笨蛋~是李白啦')
                    print('错了嘛qwq~，那就...接受惩罚叭！！')
                    print('就罚你！唔...给猫猫...做个全身按摩叭！')
                    print('一段时间后，')
                    print('喵呜~（放松地伸懒腰）')
                    print('好...舒服，那么..就这样叭~猫猫也...累了...再见啦')
            else:
                print('qwq...错了啦，是9801...没关系没关系，还有一道题...再接再厉哟')
                print('这道题嘛...应该还算...简单叭')
                print('请问！兰亭集序是谁写滴？')
                if ask_text_question("请输入答案:", "王羲之"):
                    print('答对啦！就是他~')
                    print('呼呼...奖励你一个...揉揉脑袋~')
                    print('(把爪子伸过去rua~)')
                    print('哎嘿，真软~那么...今天就到这叭~猫猫也要休息啦~')
                else:
                    print('哎呀哎呀~两连错了哟~这样子的话..惩罚加重！')
                    print('伸出爪爪...挠你脚心！')
                    print('捏嘿~怎么样怎么样~')
                    print('唔...挠累了...困QAQ，瘫怀里....（zzzzzz）')
        else:
            print("唔？！怎么会这样认为！！QAQ不玩了！！")
    else:
        print('呜呜~那好吧那好吧QAQ，祝你今天愉快~')
