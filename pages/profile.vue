<!-- use v-avatar to create a simple profile page with the name of the user and avatar at top, followed by a list of orders they have made-->
<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="1">
        <v-avatar size="70" class="mx-auto">
          <img :src="user.avatar" />
        </v-avatar>
      </v-col>
      <v-col cols="12" md="8">
        <h1 class="text-h4">{{ user.name }}</h1>
        <p class="text-body-1">{{ user.email }}</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <h2 class="text-h5">Orders</h2>
        <v-list>
          <v-list-item v-for="order in orders" :key="order.id">
            <v-list-item-content>
              <v-list-item-title>{{ order.name }}</v-list-item-title>
              <v-list-item-subtitle>
                {{ order.price | currency }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: "ProfilePage",
  data() {
    return {
      user: {
        name: "John Doe",
        email: "johndoe@gmail.com",
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg"
      },
      orders: [
        {
          id: 1,
          name: "Staedtler Triplus Fineliner Pens",
          price: 9.99
        },
        {
          id: 2,
          name: "5x5 Canvas",
          price: 3.99
        },
        {
          id: 3,
          name: "Long Brush Pen",
          price: 4.99
        }
      ]
    };
  }
};
</script>