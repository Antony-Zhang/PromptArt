"""
    项目主文件
"""
from LLM.spark_desk import SparkDesk
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

if __name__ == "__main__":
    llm = SparkDesk()

    # test
    prompt_1 = PromptTemplate(
        input_variables=["lastname"],
        template="我的邻居姓{lastname}，他生了个儿子，给他儿子起个名字，只需要一个",
    )
    chain_1 = LLMChain(llm=llm,
                       prompt=prompt_1)
    # 创建第二条链
    prompt_2 = PromptTemplate(
        input_variables=["child_name"],
        template="邻居的儿子名字叫{child_name}，给他起一个小名",
    )
    chain_2 = LLMChain(llm=llm, prompt=prompt_2)

    # 链接两条链
    overall_chain = SimpleSequentialChain(chains=[chain_1, chain_2], verbose=True)

    # 执行链，只需要传入第一个参数
    catchphrase = overall_chain.run("王")
    print(catchphrase)
