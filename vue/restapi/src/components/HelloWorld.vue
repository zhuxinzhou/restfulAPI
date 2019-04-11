<template>
  <div class="warp">
    <div class="main">
      <div class="header">
        <div class="left">
          <router-link to="/home"><i class="iconfont icon-iconfanhui"></i></router-link>
        </div>
        <div class="center"><h1>登录</h1></div>
      </div>
      <div class="lmian">
        <div class="login-main">
          <form class="form-horizontal">
            <div class="form-group">
              <div class="col-sm-8">
                <input type="text" ref="name" class="form-control" placeholder="手机号">
              </div>
            </div>
            <div class="form-group">
              <div class="col-sm-8">
                <input type="password" ref="pwd" class="form-control" placeholder="密码">
              </div>
            </div>
            <div class="form-group">
              <div class="col-sm-8 inptext">
                <button type="button" class="btn btn-danger btn-lg btn-block" @click="add">登录</button>
              </div>
            </div>
          </form>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'

export default {
  name: 'Login',
  data () {
    return {
      visibility: false,
      list: []
    }
  },
  methods: {
    add: function () {
      var user = this.$refs.name.value
      var pwd = this.$refs.pwd.value
      console.log(user, pwd)
      if (user === '') {
        alert('用户名不能为空')
      } else if (pwd === '') {
        alert('密码不能为空')
      } else {
        // cellphone=13918763344(手机号)
        // passwrod=123456(密码)
        var url = `http://127.0.0.1:5000/api/member/login`
        axios.post(url, qs.stringify({
          name: user,
          password: pwd
        })).then((res) => {
          // console.log(res.data.message[0].pwd)
          if (res.data.code === 200) {
            console.log(res)
            alert('登陆成功')
            location.href = '/#/info?id=' + res.data.data
          } else {
            alert(res.data.msg)
          }
        })
      }
    }
  }
}
</script>

<style scoped>
  .h1, h1 {
    line-height: 1.5rem;
  }

  .header {
    width: 100%;
    line-height: 1.5rem;
    display: flex;
    border-bottom: 1px solid #D6D6D6;
  }

  .header .left {
    flex: 1;
  }

  .header .center {
    flex: 9;
    font-size: 20px;
    font-weight: normal;
  }

  .heder .center h1 {
    line-height: 1.5rem;
  }

  .form-control {
    display: block;
    width: 97%;
    height: 34px;
    padding: 6px 12px;
    font-size: 14px;
    line-height: 1.42857143;
    color: #555;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  .lmian {
    flex: 1;
  }

  .col-sm-8 {
    position: relative;
    min-height: 1px;
    /* padding-right: 15px; */
    /* padding-left: 15px; */
  }

  .btn-block {
    width: 90%;
    margin-left: 5%;
  }

  .login-base {
    width: 90%;
    height: 0.5rem;
    margin-left: 5%;
    overflow: hidden;
  }

  .login-base-le {
    float: left;
    font-size: 0.2rem;
    color: #666666;
  }

  .login-base-ri {
    float: right;
    font-size: 0.2rem;
    color: #666666;
  }

  .form-horizontal .form-group {
    margin: 27px;
  }
</style>
