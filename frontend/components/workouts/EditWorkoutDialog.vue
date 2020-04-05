<template>
  <v-dialog v-model="dialog" max-width="600">

    <v-form v-model="formValid">
      <v-card>
        <v-card-title>
          <v-toolbar flat class="py-0">
            <span class="headline">
              Изменение тренировки
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
          <v-btn :loading="loading" @click="deleteWorkout" color="red" dark>
            <v-icon> mdi-delete </v-icon>
          </v-btn>
          <v-spacer/>
          <v-btn text @click="closeDialog">
            Отмена
          </v-btn>
          <v-btn color="primary" :disabled="!formValid" @click="saveWorkout">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>

  </v-dialog>
</template>

<script>
  import WorkoutForm from "./WorkoutForm";
  import requests from "../user/requests";

  export default {
    name: "EditWorkoutDialog",
    components: {WorkoutForm},
    data() {
      return {
        dialog: false,
        loading: false,
        workoutId: null,
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
      editWorkout(workoutId) {
        this.workoutId = workoutId
        this.loadWorkout()
        this.openDialog()
      },
      loadWorkout() {
        requests.getCurrentWorkout(this.$apollo, this.workoutId)
        .then(({data}) => {
          console.log(data)
          let trainers = data.getCurrentWorkout.trainers.map(x => x.id)
          this.form = data.getCurrentWorkout
          this.form.trainers = trainers

        })
      },
      saveWorkout() {
        this.loading = true

        let times = this.form.datetime.map(datetime => {
          return {
            weekday: datetime.weekday,
            time: datetime.time
          }
        })

        requests.editWorkout(
          this.$apollo,
          {
            id: this.workoutId,
            name: this.form.name,
            trainers: this.form.trainers,
            times: times
          }
        ).then(({data}) => {
          this.loading = false
          this.closeDialog()
          this.$notify({
            group: 'notify',
            title: 'Вы успешно изменили тренировку',
            text: ''
          })
          this.$emit('updated')
        }).catch(e => {
          this.loading = false
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при измение тренировки',
            text: ''
          })


        })
      },
      deleteWorkout() {
        this.loading = true
        requests.deleteWorkout(this.$apollo, this.workoutId)
        .then(({data}) => {
          this.loading = false
          this.closeDialog()
          this.$notify({
            group: 'notify',
            title: 'Вы успешно удалили тренировку',
            text: ''
          })
          this.$emit('deleted')
        }).catch(e => {
          this.loading = false
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при удаление тренировки',
            text: ''
          })
        })
      }
    }
  }
</script>

<style scoped>

</style>