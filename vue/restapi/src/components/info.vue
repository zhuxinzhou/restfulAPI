<template>
  <div id="info">
    <h1>{{info[0].realname}}</h1>
    <h2>ID:{{info[0].id}} </h2>
    <h3>登录名：{{info[0].name}}</h3>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'info',
  data () {
    return {
      info: null
    }
  },
  mounted: function () {
    var str = location.href // 取得整个地址栏
    var num = str.indexOf('?')
    str = str.substr(num + 1) // 取得所有参数   stringvar.substr(start [, length ]

    var url = `http://127.0.0.1:5000/api/member/info`
    axios
      .get(url + '?' + str)
      .then(response => (this.info = response.data.data.member_list))
  }
}
</script>

<style scoped>

</style>
