css = '''
<style>
.chat-message {
    padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;
}
.chat-message.user {
    background-color: #F3F6FC
}
.chat-message.bot {
    background-color: #F3F6FC
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  color: rgb(49, 51, 63);
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="message"><b>Answer:</b> {{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="message"><b>Question:</b> {{MSG}}</div>
</div>
'''
