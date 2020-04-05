<template>
  <v-autocomplete
    v-model="selectWorkouts"
    :items="workouts"
    :label="label"
    :required="required"
    :readonly="readonly"
    :clearable="clearable"
    ref="select"
    :multiple="multiple"
    :disabled="disabled"
    :hide-details="hideDetails"
    item-text="name"
    item-value="id"
    :chips="chips"
    :rules="rules"
  />
</template>

<script>
  import requests from "../user/requests.js"

  export default {
    name: "WorkoutSelect",
    props: {
      value: null,
      label: String,
      multiple: Boolean,
      required: Boolean,
      readonly: Boolean,
      hideDetails: Boolean,
      disabled: Boolean,
      clearable: Boolean,
      returnObject: Boolean,
      rules: {
        type: Array,
        default: () => []
      },
      chips: Boolean,
    },
    data() {
      return {
        selectWorkouts: this.value,
        workouts: []
      }
    },
    methods: {
      allWorkoutsRequest() {
        requests.getAllWorkouts(this.$apollo).then(({data}) => {
          this.workouts = data.getAllWorkouts
        })
      }
    },
    watch: {
      selectWorkouts: function (newVal) {
        this.$emit('input', newVal)
      },
      value: function (newVal) {
        this.selectWorkouts = newVal
      }
    },
    mounted() {
      this.allWorkoutsRequest()
    }
  }
</script>

<style scoped>

</style>