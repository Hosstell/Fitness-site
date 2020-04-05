<template>
  <div>
    <v-row>
      <v-col cols="12" md="6" class="pb-0">

        <private-data />

        <private-workouts />
      </v-col>


      <v-col cols="12" md="6">


        <private-workout-events />

      </v-col>

    </v-row>
  </div>
</template>

<script>
  import SexSelect from "../components/common/SexSelect";
  import DatePicker from "../components/common/DatePicker";
  import PrivateData from "../components/lk/PrivateData";
  import PrivateWorkouts from "../components/lk/PrivateWorkouts";
  import PrivateWorkoutEvents from "../components/lk/PrivateWorkoutEvents";
  export default {
    name: "lk",
    components: {PrivateWorkoutEvents, PrivateWorkouts, PrivateData, DatePicker, SexSelect}
  }
</script>

<style scoped>

</style>