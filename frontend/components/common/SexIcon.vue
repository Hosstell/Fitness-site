<template>
  <span>
    <v-icon  v-if="sex === 'M'" color="blue">
      mdi-human-male
    </v-icon>
    <v-icon v-else color="pink">
      mdi-human-female
    </v-icon>
  </span>
</template>

<script>
  export default {
    name: "SexIcon",
    props: {
      sex: String
    }
  }
</script>

<style scoped>

</style>