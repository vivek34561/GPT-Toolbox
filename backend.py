from src.graphs.graph_builder import build_graph

# Build the graph and get chatbot instance
chatbot, checkpointer = build_graph()


def retrieve_all_threads():
    """Retrieve all thread IDs from the checkpointer"""
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id']) 

    return list(all_threads)


