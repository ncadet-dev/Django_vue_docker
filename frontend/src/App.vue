<template>
  <div>
    <h1>Test technique Popsink !</h1>
    <p>Le bouton <strong>API route public</strong> redirige vers une page générée par DRF où sera montré un json généré aléatoirement.</p>
    <p>Le bouton <strong>API route privée</strong> a la même fonction mais requiert une authentification avant la consultation.</p>
    <button class="btn btn-outline-primary" @click="redirectToPublicEndpoint">API route public</button>
    <button class="btn btn-outline-primary" @click="redirectToPrivateEndpoint">API route privée</button>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {}
  },
  methods: {
    redirectToPublicEndpoint() {
      window.open(process.env.VUE_APP_API_BASE_URL + 'public/', '_blank').focus()
    },
    redirectToPrivateEndpoint() {
      window.open(process.env.VUE_APP_API_BASE_URL + 'private/', '_blank').focus()
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
