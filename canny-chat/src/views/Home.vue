<template>
  <div class="home" style="width: 60%; margin-left: 20%">
    <img alt="Vue logo" src="../assets/logo.png" />
    <p>{{ res }}</p>
    <input v-model="text" />
    <button @click="send()">发送</button>
  </div>
</template>

<script>
import io from "socket.io-client";
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      text: "请输入...",
      res: "canny-chat-res",
      socket: null,
    };
  },
  created() {
    this.socket = io(process.env.VUE_APP_URL);
    this.socket.on("chat_response", this.handleChatResponse);
  },
  methods: {
    send() {
      this.res = "请求中，请稍后...";
      this.socket.emit("chat", this.text);
    },
    handleChatResponse(response) {
      // 处理聊天响应
      this.res = response;
    },
  },
};
</script>
