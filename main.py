import WS
import MoodAnalysis

if __name__ == "__main__":
    wsParam = WS.Ws_Param()
    print("请开始对话吧!!")

    txt = input("\n(输入-1结束对话)文案:")
    # 输入的txt中不可包含\n换行符!

    while txt != "-1":  # 机械的循环交互,但不知道长连接本身是否可支持
        # 情绪识别
        MoodAnalysis.MoodAnalysis.mood_analyze(txt)
        txt = input("\n(输入-1结束对话)文案:")
