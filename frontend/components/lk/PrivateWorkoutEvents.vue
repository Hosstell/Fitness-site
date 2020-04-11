<template>
  <v-card>
    <v-card-title>
      Отработанные тренировки
    </v-card-title>
    <v-card-text>

      <v-list dense v-if="!loading">
        <v-list-item-group color="primary" v-if="workoutEvents.length">
          <v-list-item v-for="workoutEvent in workoutEvents">
            <v-list-item-icon>
              <v-icon> mdi-dumbbell </v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>
                {{ workoutEvent.workout.name }}
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ formatMonth(workoutEvent.date) }} | {{ workoutEvent.time.slice(0, 5) }}
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
  import utilsMixin from "../../utils/utils";

  export default {
    name: "PrivateWorkoutEvents",
    mixins: [utilsMixin],
    data() {
      return {
        loading: false,
        workoutEvents: []
      }
    },
    methods: {
      allWorkoutEventsOfUserRequest() {
        this.loading = true
        requests.getAllWorkoutEventsOfUser(this.$apollo)
        .then(({data}) => {
          this.workoutEvents = data.getAllWorkoutEventsOfUser
          this.loading = false
        })
      }
    },
    mounted() {
      this.allWorkoutEventsOfUserRequest()
    }
  }
</script>

<style scoped>

</style>