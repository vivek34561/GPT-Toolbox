import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage 
import uuid


# ------------------------------ utility functions --------------------------------
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])     
    st.session_state['message_history'] = []
    
def add_thread(thread_id)    :
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)
    
def load_conversation(thread_id):
    return chatbot.get_state(config = {'configurable' : {'thread_id':thread_id}}).values['messages']

    
CONFIG = {'configurable':{'thread_id':'thread-1'}}
if 'message_history' not in st.session_state:
    st.session_state['message_history']   = []

if  'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
    
    
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads']  = []

add_thread(st.session_state['thread_id'])     
    
# {'role':'user' , 'content':'Hi'}
#{'role':'assistant' , 'content':'Hi'}
# -------------------------------------- sidebar ---------------------------------------
st.sidebar.title("LangGraph Chatbot")
if st.sidebar.button('New Chat'):
    reset_chat()
    
    
st.sidebar.header("My Conversation")
for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        temp_messages = []
        for msg in messages:
            if isinstance(msg , HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_messages.append({'role':role  ,'content': msg.content})    
        st.session_state['message_history'] = temp_messages
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("type here")
if user_input:
    st.session_state['message_history'].append({'role':'user' , 'content' : user_input})
    with st.chat_message('user'):
        st.text(user_input)
    
    CONFIG = {'configurable':{'thread_id' : st.session_state['thread_id']}}    
    
    with st.chat_message('assistant'):
        status_placeholder = st.empty()
        response_placeholder = st.empty()
        
        ai_message = ""
        current_node = None
        
        for chunk in chatbot.stream(
            {'messages': [HumanMessage(content=user_input)]}, 
            config=CONFIG, 
            stream_mode='updates'
        ):
            for node_name, node_data in chunk.items():
                if node_name == "tools":
                    if 'messages' in node_data:
                        for msg in node_data['messages']:
                            if hasattr(msg, 'name'):
                                if msg.name == "duckduckgo_search":
                                    status_placeholder.info("🔍 Searching the web...")
                                elif msg.name == "calculator":
                                    status_placeholder.info("🧮 Calculating...")
                                else:
                                    status_placeholder.info(f"🔧 Using tool: {msg.name}...")
                
                elif node_name == "chat_node":
                    status_placeholder.empty()
                    if 'messages' in node_data:
                        for msg in node_data['messages']:
                            if hasattr(msg, 'content') and msg.content:
                                ai_message = msg.content
                                response_placeholder.write(ai_message)
                
                elif node_name == "reflect":
                    status_placeholder.info("✨ Validating response...")
                    if 'messages' in node_data:
                        for msg in node_data['messages']:
                            if hasattr(msg, 'content') and msg.content:
                                ai_message = msg.content
                                response_placeholder.write(ai_message)
        
        status_placeholder.empty()
        
    st.session_state['message_history'].append({'role':'assistant' , 'content' : ai_message})    