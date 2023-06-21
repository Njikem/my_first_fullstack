<template>
<div class = "candy_container">
    <article class ="candy" v-for="(candy, i) in candy" :key="i">
        <h4>{{candy["name"]}}</h4>
        <img :src="candy['image_url']" :alt="`candy ${candy['name']}`"/>
        <p>{{candy["description"]}}</p>

    </article>

</div>
</template>
<script>
import axios from "axios";
export default {
    data() {
        return{
            candy: [],
        };
    },

    methods: {
        get_candy() {
            axios.request({
                url: "http://127.0.0.1:5000/api/candy",
            }).then((response) =>{
               this.candy = response ["data"];
        }).catch((error) =>{
            error
        });

        },
    },

    mounted() {
        this.get_candy();
        this.$root.$on("new_candy", this.get_candy);
    },
};

</script>
<style>

</style>