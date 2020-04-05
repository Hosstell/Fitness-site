<template>
  <v-dialog v-model="dialog" max-width="600">

    <v-form v-model="formValid">
      <v-card>
        <v-card-title>
          <v-toolbar flat class="py-0">
            <span class="headline">
              Редактирование абонемента
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
          <v-btn :loading="loading" @click="deleteSeasonTicket" color="red" dark>
            <v-icon> mdi-delete </v-icon>
          </v-btn>
          <v-spacer/>
          <v-btn :loading="loading" text @click="closeDialog">
            Отмена
          </v-btn>
          <v-btn :loading="loading" color="primary" :disabled="!formValid" @click="saveSeasonTicket">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>

  </v-dialog>
</template>

<script>
  import requests from "../user/requests";
  import SeasonTicketForm from "./SeasonTicketForm";

  export default {
    name: "EditSeasonTicket",
    components: {SeasonTicketForm},
    data() {
      return {
        dialog: false,
        seasonTicketId: '',
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
      editSeasonTicket(seasonTicketId) {
        this.seasonTicketId = seasonTicketId
        this.openDialog()
        this.loadSeasonTicket()
      },
      loadSeasonTicket() {
        console.log('loadSeasonTicket')
        requests.getCurrentSeasonTicket(this.$apollo, this.seasonTicketId)
        .then(({data}) => {
          console.log(data)
          this.form = {
            clientId: data.getCurrentSeasonTicket.client.id,
            workoutId: data.getCurrentSeasonTicket.workout.id,
            startDate: data.getCurrentSeasonTicket.startDate,
            endDate: data.getCurrentSeasonTicket.endDate
          }
        })
      },
      saveSeasonTicket() {
        this.loading = true

        requests.saveSeasonTicket(
          this.$apollo,
          {
            seasonTicketId: this.seasonTicketId,
            clientId: this.form.clientId,
            workoutId: this.form.workoutId,
            startDate: this.form.startDate,
            endDate: this.form.endDate,
          }
        ).then(data => {
          this.$notify({
            group: 'notify',
            title: 'Вы успешно отредактировали абонемент',
            text: ''
          })
          this.$emit('updated')
          this.loading = false
          this.closeDialog()

        }).catch(e => {
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при редактировании нового абонемента',
            text: ''
          })
          this.loading = false
        })
      },
      deleteSeasonTicket() {
        this.loading = true

        requests.deleteSeasonTicket(this.$apollo, this.seasonTicketId)
          .then(({data}) => {
            this.loading = false
            this.closeDialog()
            this.$notify({
              group: 'notify',
              title: 'Вы успешно удалили абонемент',
              text: ''
            })
            this.$emit('deleted')
          }).catch(e => {
          this.loading = false
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при удаление абонемента',
            text: ''
          })
        })
      }
    }
  }
</script>

<style scoped>

</style>