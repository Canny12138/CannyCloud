<template>
  <div class="home" style="width: 60%; margin-left: 20%;">
    <img alt="Vue logo" src="../assets/logo.png" />
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <p>{{ res }}</p>
    <input v-model="text">
    <button @click="send()">发送</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    HelloWorld,
  },
  data() {
    return {
      text:"请输入...",
      res: "canny-chat-res",
    };
  },
  methods: {
    send() {
      let endpoint = "https://api.openai.com/v1/chat/completions";
      let headers = {
        "Content-Type": "application/json",
        Authorization:
          process.env.VUE_APP_APIKEY, // 将YOUR_API_KEY替换为您自己的ChatGPT API密钥
      };
      let body = {
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: this.text }],
        // 根据您的需求自定义请求体的内容
      };
      this.res = "请求中，请稍后..."
      let self = this;
      // 使用axios库发送请求
      axios
        .post(endpoint, body, { headers: headers })
        .then((response) => {
          // 在此处处理来自ChatGPT API的响应结果
          console.log(response.data);
          self.res = response.data.choices[0].message.content;
        })
        .catch((error) => {
          // 处理请求错误
          console.error("请求错误:", error);
          self.res = "请求错误"
        });
    },
  },
};
</script>
