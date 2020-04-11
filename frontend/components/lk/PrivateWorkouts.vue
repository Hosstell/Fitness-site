<template>
  <v-card class="mt-3">
    <v-card-title>
      Тренировки
    </v-card-title>

    <v-card-text>
      <v-list dense v-if="!loading">
        <v-list-item-group color="primary" v-if="workouts.length">
          <v-list-item v-for="workout in workouts">

            <v-list-item-icon>
              <v-icon> mdi-dumbbell </v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>
                {{ workout.name }}
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ workout.weekday }} {{ workout.time.slice(0, 5) }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>

        <div v-else>
          У Вас нет прикрепленных тренировок
        </div>
      </v-list>

      <v-row v-else justify="center">
        <v-progress-circular
          :size="50"
          color="primary"
          indeterminate
        ></v-progress-circular>
      </v-row>

    </v-card-text>
  </v-card>
</template>

<script>
  import requests from "../user/requests";

  export default {
    name: "PrivateWorkouts",
    data() {
      return {
        loading: false,
        workouts: []
      }
    },
    methods: {
      allWorkoutOfUserRequest() {
        this.loading = true
        requests.getWorkoutOfUser(this.$apollo)
        .then(({data}) => {
          this.workouts = []
          data.getAllWorkoutOfUser.forEach(workout => {
            workout.datetime.forEach(datetime => {
              this.workouts.push({
                name: workout.name,
                weekday: datetime.weekday,
                time: datetime.time
              })
            })
          })
          this.loading = false
        })
      }
    },
    mounted() {
      this.allWorkoutOfUserRequest()
    }
  }
</script>

<style scoped>

</style>