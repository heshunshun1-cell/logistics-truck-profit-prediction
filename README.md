 # 物流卡车利润预测项目

## 项目简介

这是一个基于 Python 的物流卡车运营数据分析项目。

简单来说，本人这个项目想解决一个很现实的问题：

> 一趟运输到底赚不赚钱？  
> 哪辆车更能赚钱？  
> 哪条路线看起来很香，实际可能利润一般？  
> LNG 和柴油车的成本差距到底有多大？

作为一个和物流行业有实际接触的学生，我突发奇想吧学到的 Python、pandas、matplotlib 和机器学习，放到一个真实业务场景里练一练，满足下我的好奇心，因此耗费了我周五整整一天哈哈哈哈。  
主要是不希望代码永远停留在学校里做作业project的阶段，感觉多少有点对不起我的实习工作里做的项目。

---

## 使用工具

这个项目主要使用：

- Python
- pandas
- matplotlib
- scikit-learn

---

## 数据说明

本项目使用的是经过脱敏和处理后的物流运营数据，结构参考真实卡车运输业务场景。

为了保护商业隐私，数据做了以下处理：

- 车辆编号已匿名化，例如 `TRUCK_001`
- 路线只保留城市级别，例如 `Chongqing-Chengdu`
- 金额字段经过统一比例缩放处理
- 不包含客户名称
- 不包含司机姓名
- 不包含车牌号
- 不包含发票号
- 不包含具体地址

所以这个数据可以理解为：

> 有真实业务逻辑，但不是直接暴露真实公司原始数据。

数据仅用于学习、作品集展示和找实习时证明：“我真的会用 Python 分析一点业务问题。”

---

## 项目结构

```text
logistics-truck-profit-prediction/
│
├── data/
│   └── truck_operations_processed.csv
│
├── visuals/
│   ├── cost_per_km_by_fuel_type.png
│   ├── profit_by_route.png
│   └── profit_by_truck.png
│
├── main.py
├── model.py
├── README.md
└── requirements.txt
