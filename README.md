# 外星人入侵游戏

**游戏背景介绍**

在未来的太空时代，地球突然遭受到了来自外星人的入侵威胁。这些外星生物带来了强大的战舰和先进的武器技术，它们的目标是摧毁地球上的一切，并占据我们的星球。

你是地球的最后一道防线，被派遣到一个重要的防御据点，你的任务是使用有限的资源和战舰，阻止外星人和他们的盟友，敌方战舰，占领地球。你必须聪明地部署战舰，合理利用资金，同时抵挡外星人的进攻。

你的决策和战术将决定地球的存亡。你能够成功阻止外星人的入侵并保卫地球吗？

## 游戏

这是一个命令行文本游戏，玩家需要在一个20x20的网格上部署战舰，抵御外星人和敌方战舰的入侵。游戏的目标是防止外星人和敌方战舰摧毁所有你的战舰并且占据一定比例的地盘。

## 游戏规则

1. 游戏网格大小为20x20。

2. 你拥有初始资金1000美元，可以用来购买不同类型的战舰。

3. 有三种不同类型的战舰可供购买：小战舰、中战舰和大战舰，每种战舰有不同的价格、攻击范围和攻击力。

4. 外星人会在游戏开始时随机出现在网格上的某个位置。

5. 敌方战舰也会在游戏开始时随机出现在网格上的某些位置。

6. 游戏会分为多个局，前两局不检查失败条件。第三局开始，如果地图上有一定比例的区域被敌方占据，你将失败。

7. 在每局中，你可以选择购买战舰、部署战舰、发起攻击或退出游戏。

8. 我们的战舰部署在网格上，并且可以攻击特定范围内的敌方战舰。当你攻击到敌方战舰时，会造成伤害并减少它们的生命值。

9. 外星人和敌方战舰也会定期攻击你的战舰，造成伤害。

10. 在每局结束时，你将获得一定数量的经费，可以用于购买更多的战舰。

11. 游戏继续进行，直到你的资金耗尽、所有敌方战舰被摧毁或者失败条件满足。

## 如何运行游戏

1. 确保你的Python环境已经安装。

2. 下载游戏代码文件 `game.py` 并将其保存到本地目录。

3. 在命令行终端中，进入游戏代码所在的目录。

4. 运行以下命令以启动游戏：


