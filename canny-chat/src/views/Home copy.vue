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
      // axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";
      // axios.defaults.headers.common["Access-Control-Allow-Methods"] =
      //   "GET, POST, OPTIONS";
      // axios.defaults.headers.common["Access-Control-Allow-Headers"] =
      //   "Content-Type, Authorization";
      // axios.defaults.headers.common["Access-Control-Allow-Credentials"] =
      //   "true";
      // axios.defaults.headers.common["Cache-Control"] = "no-cache";
      // axios.defaults.headers.common["Pragma"] = "no-cache";
      // axios.defaults.headers.common["Expires"] = "0";
      // 使用axios库发送请求
      axios
        .post(endpoint, body, { withCredentials: true })
        .then((response) => {
          // 在此处处理来自后端的响应结果
          console.log(response.data);
          self.res = response.data.choices[0].message.content;
        })
        .catch((error) => {
          // 处理请求错误
          console.error("请求错误:", error);
          self.res = "请求错误";
        });
    },
  },
  // methods: {
  //   send() {
  //     let endpoint = "https://api.openai.com/v1/chat/completions";
  //     let headers = {
  //       "Content-Type": "application/json",
  //       Authorization:
  //         process.env.VUE_APP_APIKEY, // 将YOUR_API_KEY替换为您自己的ChatGPT API密钥
  //     };
  //     let body = {
  //       model: "gpt-3.5-turbo",
  //       messages: [{ role: "user", content: this.text }],
  //       // 根据您的需求自定义请求体的内容
  //     };
  //     this.res = "请求中，请稍后..."
  //     let self = this;
  //     // 使用axios库发送请求
  //     axios
  //       .post(endpoint, body, { headers: headers })
  //       .then((response) => {
  //         // 在此处处理来自ChatGPT API的响应结果
  //         console.log(response.data);
  //         self.res = response.data.choices[0].message.content;
  //       })
  //       .catch((error) => {
  //         // 处理请求错误
  //         console.error("请求错误:", error);
  //         self.res = "请求错误"
  //       });
  //   },
  // },
};
</script>
