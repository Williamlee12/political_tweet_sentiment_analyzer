<template>
  <div id="app">
    <div class="container-fluid">
      <span class="d-block p-3 text-black bg-success"><h1><img class="logo" src="./assets/Twitter_Logo_Blue.png" width="7%">&nbsp&nbsp&nbsp&nbspPolitical Tweet Sentiment Analysis</h1></span>
    <br>
    <tweet_analyzer/>
    </div>
  </div>
</template>

<script>
import Tweet_analyzer from './components/Tweet_analyzer'

export default {
  name: 'app',
  components: {
    Tweet_analyzer
  }
}
</script>

<style lang="scss">
@import './styles/custom-bootstrap.scss';
@import '../node_modules/bootstrap/scss/bootstrap.scss';
</style>
