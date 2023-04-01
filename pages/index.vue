<!-- Write a front page for a stationary store with options for login, cart, items, catgories and offers, which can be linked with django-->
<template>
  <v-container>
      <v-row>
      <v-col cols="12">
          <v-card>
          <v-card-title>
              <h1 class="display-1">Welcome to the Stationary Store</h1>
          </v-card-title>
          <v-card-text>
            <p>
              A stationary store for all your stationery needs.
            </p>
          </v-card-text>
          </v-card>
      </v-col>
      </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'IndexPage'
}
</script>