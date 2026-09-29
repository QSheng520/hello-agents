
# 学习笔记

```
# 配置环境变量（配置完需要重启IDE，才能加载到环境变量）：

TAVILY_API_KEY=xxx   (https://app.tavily.com/home 获取)
CHAT_DEEPSEEK_API_KEY=xxxx


# 启动jupyter
jupyter notebook --notebook-dir=D:\\workspace\\hello-agents\\code


# 安装包
pip install jupyter
pip install tavily-python
pip install openai
pip install python-dotenv

```


## 运行 FirstAgentTest.py返回结果
```markdown
D:\install\anaconda\envs\hello_agent_py312\python.exe D:\workspace\hello-agents\code\chapter1\FirstAgentTest.py 
用户输入: 你好，请帮我查询一下今天广西柳州的天气，然后根据天气推荐一个合适的旅游景点。
========================================
--- 循环 1 ---

正在调用大语言模型...
大语言模型响应成功。
模型输出:
Thought: 用户想了解今天广西柳州的天气，并据此推荐旅游景点。首先需要查询柳州的实时天气。
Action: get_weather(city="柳州")

Observation: 柳州当前天气：Partly Cloudy ，气温28摄氏度
========================================
--- 循环 2 ---

正在调用大语言模型...
大语言模型响应成功。
模型输出:
Thought: 已经获取到柳州当前的天气为 Partly Cloudy（多云），气温28摄氏度。接下来需要根据这个天气情况搜索柳州推荐的旅游景点。
Action: get_attraction(city="柳州", weather="Partly Cloudy")

Observation: Under partly cloudy weather in Liuzhou, the sources recommend visiting the "马鞍山公园" (Ma'anshan Park), which offers panoramic views of the city and features ancient stone carvings and natural beauty. The park is historically significant and provides a serene environment, making it a great spot for sightseeing and appreciating the natural landscape. The sources do not provide specific details on weather-related activities or other attractions under partly cloudy conditions.
========================================
--- 循环 3 ---

正在调用大语言模型...
大语言模型响应成功。
模型输出:
Thought: 已获取柳州天气（多云，28°C）及相应的景点推荐（马鞍山公园），信息足够回答用户。
Action: Finish[今天柳州天气为多云（Partly Cloudy），气温28摄氏度。根据天气，推荐您前往马鞍山公园（Ma'anshan Park）。这里可以俯瞰柳州全景，还有古代石刻和自然美景，历史底蕴深厚，环境宁静，非常适合在多云天气下观光游览。]

任务完成，最终答案: 今天柳州天气为多云（Partly Cloudy），气温28摄氏度。根据天气，推荐您前往马鞍山公园（Ma'anshan Park）。这里可以俯瞰柳州全景，还有古代石刻和自然美景，历史底蕴深厚，环境宁静，非常适合在多云天气下观光游览。

进程已结束，退出代码为 0


```