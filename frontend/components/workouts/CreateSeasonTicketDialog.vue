<template>
  <v-dialog v-model="dialog" max-width="600">

    <v-form v-model="formValid">
      <v-card>
        <v-card-title>
          <v-toolbar flat class="py-0">
            <span class="headline">
              Создание абонемента
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

          <season-ticket-form
            :form="form"
          />

        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn :loading="loading" text @click="closeDialog">
            Отмена
          </v-btn>
          <v-btn :loading="loading" color="primary" :disabled="!formValid" @click="createSeasonTicket">
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
  import gql from 'graphql-tag';

  import requests from "../user/requests.js";
  import SeasonTicketForm from "./SeasonTicketForm";

  export default {
    name: "CreateSeasonTicketDialog",
    components: {SeasonTicketForm, TimePicker, WeekDaySelect, TrainersSelect},
    data() {
      return {
        dialog: false,
        loading: false,
        form: {
          clientId: null,
          workoutId: null,
          startDate: null,
          endDate: null
        },
        formValid: false
      }
    },
    methods: {
      openDialog() {
        this.dialog = true
      },
      closeDialog() {
        this.dialog = false
      },
      createSeasonTicket() {
        this.loading = true

        requests.createSeasonTicket(
          this.$apollo,
          {
            clientId: this.form.clientId,
            workoutId: this.form.workoutId,
            startDate: this.form.startDate,
            endDate: this.form.endDate,
          }
        ).then(data => {
          this.$notify({
            group: 'notify',
            title: 'Вы успешно создали новый абонемент',
            text: ''
          })
          this.$emit('created')
          this.loading = false
          this.closeDialog()

        }).catch(e => {
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при создание нового абонемента',
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