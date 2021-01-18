# 塔罗牌抽取工具

网络上的随机抽取塔罗牌程序大多会先在78张伟特牌中进行抽取，再对牌面进行一次随机正逆运算，这与纸牌的抽取规则不符。

纸牌在洗牌切牌完毕后，形成的是正逆随机的78张牌，因此程序也应该遵循这样的方式来抽取纸牌。

正确的抽取方式应该是在抽牌之前先生成正逆随机共包含78张牌的数组，同时还要确保一个牌型要在同一个数组中抽取，不可以每抽一张都重新洗牌。

### 工作逻辑

1. 使用随机值 0 或 1 填充一个包含78个元素的数组；
2. 元素值为 1 代表逆位，元素值为 0 代表正位；
3. 从该数组中一次性抽取指定数量且不重复的元素；

### 使用方法

克隆仓库到本地

```shell
$ git clone https://github.com/yuhr123/tarot-random.git
```

进入 pipenv 虚拟环境并安装程序

```shell
$ cd tarot-random
tarot-random $ pipenv install
```

在虚拟环境中运行程序

```shell
$ pipenv shell
(tarot-random) $ gunicorn home.wsgi:app
```

浏览器访问 [http://localhost:8000](http://localhost:8000)

### ❤ 感谢 Thanks！

本项目使用了 [Python](https://www.python.org/) 语言。

本项目使用了 [Flask](https://flask.palletsprojects.com) 框架。

本项目使用了 [Gunicorn](https://gunicorn.org/) 服务器。

本项目使用了 [jeremytarling/python-tarot](https://github.com/jeremytarling/python-tarot) 中的塔罗牌字典和塔罗牌图片。

本项目使用了 [UIKit](https://getuikit.com/) 前端框架。

本项目使用了 [pipenv](https://pipenv.pypa.io/en/latest/) Python 虚拟环境管理工具。

### 版权声明

本项目仅供个人非商业使用，项目中所使用的塔罗牌图片来自互联网，版权归原作者所有，如有冒犯，请联系删除。