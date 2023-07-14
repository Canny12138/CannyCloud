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
      longPollingId: null, // 存储长轮询 ID
    };
  },
  methods: {
    send() {
      let endpoint = process.env.VUE_APP_URL + "/api/chat"; // 指向您的后端 API 的 URL
      let longPollingEndpoint = process.env.VUE_APP_URL + `/api/chat/long-polling/${this.longPollingId}`; // 指向长轮询接口的 URL
      let body = {
        messages: [{ role: "user", content: this.text }],
        // 根据您的需求自定义请求体的内容
      };

      this.res = "请求中，请稍后...";
      let self = this;

      // 发送请求以获取长轮询 ID
      axios
        .post(endpoint, body, { withCredentials: true })
        .then((response) => {
          self.longPollingId = response.data.long_polling_id;

          // 发起长轮询请求
          const longPollingRequest = () => {
            axios
              .get(longPollingEndpoint, { withCredentials: true, responseType: "text" })
              .then((response) => {
                if (response.status === 200) {
                  // 逐步处理响应字段
                  self.res += response.data;

                  // 继续进行下一轮长轮询
                  longPollingRequest();
                }
              })
              .catch((error) => {
                console.error("请求错误:", error);
                self.res = "请求错误";
              });
          };

          // 发起第一次长轮询请求
          longPollingRequest();
        })
        .catch((error) => {
          console.error("请求错误:", error);
          self.res = "请求错误";
        });
    },
  },
};
</script>
