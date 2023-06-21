<template>
    <div>
        <h2>New Candy</h2>
        <input type= "text" placeholder="name" ref="name_input"/>
         <input type= "text" placeholder="description" ref="description_input"/>
          <input type= "text" placeholder="image_url" ref="img_input"/>
          <button @click="post_candy">SUBMIT</button>

          <p>{{status}}</p>


    </div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return{
            status: undefined,

        };
    },

    methods: {
        post_candy() {
            axios.request({
                url: "http://127.0.0.1:5000/api/candy",
                method: "POST",
                data: {
                    name: this.$refs["name_input"].value,
                    image_url: this.$ref["img_input"].value,
                    description: this.$refs["description"].value,
                },
            }).then((response) =>{
                this.status = "New candy inserted"
        }).catch((error) =>{
            error;
        });
        },
    },

};
</script>

<style>
</style>