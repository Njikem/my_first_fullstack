<template>
    <div>
        <article class ="candy" v-for="(candy, id) in candy" :key="id">
            <h4>{{candy["name"]}}</h4>
            <h4>{{candy["description"]}}</h4>
            <button @click="delete_candy">Delete</button>


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
    delete_candy () {
        axios.request({
            url: "http://127.0.0.1:5000/api/candy",
            method: "Delete",
        }).then((reponse) => {
            reponse

    }).catch((error) => {
        error

    })

    

    }

    

}

}
</script>

<style>
</style>