<template>
  <v-dialog v-model="dialog" max-width="600">

    <v-form v-model="formValid">
      <v-card>
        <v-card-title>
          <v-toolbar flat class="py-0">
            <span class="headline">
              Создание события
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

          <event-form
            :form="form"
          />

        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn text @click="closeDialog">
            Отмена
          </v-btn>
          <v-btn color="primary" :disabled="!formValid" @click="createEvent">
            Создать
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>

  </v-dialog>
</template>

<script>
  import EventForm from "./EventForm";
  import requests from "../user/requests";

  export default {
    name: "CreateEvents",
    components: {EventForm},
    data() {
      return {
        dialog: false,
        loading: false,
        form: {},
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
      createEvent() {
        this.loading = true
        requests.createEvent(
          this.$apollo,
          {
            workoutId: this.form.workoutId,
            date: this.form.date,
            time: this.form.time,
            trainers: this.form.trainers,
            clients: this.form.clients
          }
        ).then(data => {
          this.$notify({
            group: 'notify',
            title: 'Вы успешно создали событие',
            text: ''
          })
          this.$emit('created')
          this.loading = false
          this.closeDialog()

        }).catch(e => {
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при создание события',
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