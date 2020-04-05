<template>
  <v-dialog v-model="dialog" max-width="600">

    <v-form v-model="formValid">
      <v-card>
        <v-card-title>
          <v-toolbar flat class="py-0">
            <span class="headline">
              Создание нового клиента
            </span>
            <v-spacer />
            <v-btn icon @click="closeDialog">
              <v-icon>
                mdi-close
              </v-icon>
            </v-btn>
          </v-toolbar>
        </v-card-title>
        <v-card-text>

          <workout-form
            :form="form"
          />

        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn text @click="closeDialog">
            Отмена
          </v-btn>
          <v-btn color="primary" :disabled="!formValid" @click="createWorkout">
            Создать
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>

  </v-dialog>
</template>

<script>
  import TrainersSelect from "./TrainersSelect";
  import WeekDaySelect from "../WeekDaySelect";
  import TimePicker from "../common/TimePicker";
  import WorkoutForm from "./WorkoutForm";
  import gql from 'graphql-tag';

  import requests from "../user/requests.js";

  export default {
    name: "CreateWorkoutDialog",
    components: {WorkoutForm, TimePicker, WeekDaySelect, TrainersSelect},
    data() {
      return {
        dialog: false,
        loading: false,
        form: {
          name: '',
          trainers: [],
          datetime: [{
            weekday: null,
            time: ''
          }]
        },
        formValid: false,
      }
    },
    methods: {
      openDialog() {
        this.dialog = true
      },
      closeDialog() {
        this.dialog = false
      },
      createWorkout() {

        requests.createWorkout(
          this.$apollo,
          {
            name: this.form.name,
            trainers: this.form.trainers,
            times: this.form.datetime
          }
        ).then(data => {
          this.$notify({
            group: 'notify',
            title: 'Вы успешно создали нового клиента',
            text: ''
          })
          this.$emit('created')
          this.loading = false
          this.closeDialog()

        }).catch(e => {
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при создание нового клиента',
            text: ''
          })
          this.loading = false
        })
      }
    }
  }
</script>

<style scoped>

</style>