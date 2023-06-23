import WS

if __name__ == "__main__":
    wsParam = WS.Ws_Param()

    print("请开始对话吧!!")
    txt = input("\n(输入-1结束对话)文案:")
    # 机械的循环交互,但不知道长连接本身是否可支持
    while txt != "-1":
        Prompt = f'''
        [任务]

        [格式]

        [示例]

        [输入]
        {txt}
        [输出]

        '''
        WS.main(wsParam, Prompt)
        txt = input("\n(输入-1结束对话)文案:")