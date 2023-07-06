<template>
  <div class="home" style="width: 60%; margin-left: 20%">
    <img alt="Vue logo" src="../assets/logo.png" />
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <p>{{ res }}</p>
    <input v-model="text" />
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
      text: "请输入...",
      res: "canny-chat-res",
    };
  },
  methods: {
    send() {
      let endpoint = "http://url:5000/api/chat"; // 指向您的后端 API 的 URL
      let body = {
        messages: [{ role: "user", content: this.text }],
        // 根据您的需求自定义请求体的内容
      };

      this.res = "请求中，请稍后...";
      let self = this;

      // 使用axios库发送请求
      axios
        .post(endpoint, body, { withCredentials: true, timeout: 30000 }) // 设置超时时间为5秒
        .then((response) => {
          // 在此处处理来自后端的响应结果
          console.log(response.data);
          self.res = response.data.choices[0].message.content;
        })
        .catch((error) => {
          // 处理请求错误
          if (error.response) {
            // 请求已发送，但服务器返回错误状态码
            console.error("请求错误:", error.response.data);
          } else if (error.request) {
            // 请求已发送，但没有接收到响应
            console.error("请求超时:", error.request);
          } else {
            // 其他错误
            console.error("请求错误:", error.message);
          }
          self.res = "请求错误";
        });
    },
  },
};
</script>