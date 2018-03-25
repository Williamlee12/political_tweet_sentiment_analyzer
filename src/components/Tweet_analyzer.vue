<style scoped>



</style>

<template>

<div class="tweet_analyzer">

    <div v-if="display_entry">

        <div class="input-group">
            <textarea v-model="tweets" class="form-control" placeholder="tweets (seperated by newline character)" name="tweets" rows="10"></textarea>
        </div>
        <br>
        <span><button @click="Loading(); SubmitTweets()" type="button" class="btn btn-primary">Submit!</button>&nbsp&nbsp{{loading}}</span>
        <br>
        <br>
        <div class="input-group">
            <input type="text" class="form-control" placeholder="twitter handle" v-model="twitter_handle" />
        </div>
        <br>
        <span><button @click="Loading1(); SubmitHandle()" type="button" class="btn btn-primary">Submit!</button>&nbsp&nbsp{{loading1}}</span>
        <br>
    </div>


    <div v-if="display_results">
        <table class="table table-striped table-hover table-sm">
            <thead>
                <tr>
                    <th class="w-90">
                        Tweet
                    </th>
                    <th class="w-10">
                        Sentiment
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="tweet in raw_ml_data">
                    <td>
                        {{tweet[0]}}
                    </td>
                    <td>
                        {{tweet[2]}}
                    </td>
                </tr>
            </tbody>
        </table>

    </div>

</div>

</template>

<script>

import axios from 'axios';

export default {
    data() {
            return {
                display_entry: true,
                display_results: false,
                tweets: "",
                loading: "",
                loading1: "",
                raw_ml_data: "",
                twitter_handle: "",

            }
        },
        watch: {
            raw_ml_data: function() {
                if (this.raw_ml_data.length != 0) {
                    this.display_entry = false
                    this.display_results = true
                }
            }
        },
        methods: {
            Loading: function() {
                this.loading = "Loading..."
            },
            Loading1: function() {
                this.loading1 = "Loading..."
            },
            SubmitTweets: function() {
                var app = this
                axios({
                        method: 'post',
                        // url: 'http://localhost:8000/sentiment_api/',
                        url: 'https://pol-tweet-sentiment-analysis.herokuapp.com/sentiment_api/',
                        data: {
                            tweets: this.tweets.split("\n")
                        }
                    })
                    .then(function(response) {
                        app.raw_ml_data = response.data
                    });

            },
            SubmitHandle: function() {
                var app = this
                axios({
                        method: 'post',
                        // url: 'http://localhost:8000/sentiment_api/twitter/',
                        url: 'https://pol-tweet-sentiment-analysis.herokuapp.com/sentiment_api/twitter/',
                        data: {
                            twitter_handle: this.twitter_handle
                        }
                    })
                    .then(function(response) {
                        app.raw_ml_data = response.data
                    });

            },
        }

}

</script>
