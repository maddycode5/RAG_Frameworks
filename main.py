pipeline =RAGPipeline()

pipeline.build()

while True:
    question = input("> ")
    answer= pipeline.query(question)
    print(answer)
    