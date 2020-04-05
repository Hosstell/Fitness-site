<template>
  <v-dialog v-model="dialog" max-width="600">

    <v-form v-model="formValid">
      <v-card>
        <v-card-title>

          <span :class="{'body-1': $vuetify.breakpoint.xs}">
            Редактирование клиента
          </span>
          <v-spacer/>
          <v-btn icon @click="closeDialog">
            <v-icon>
              mdi-close
            </v-icon>
          </v-btn>

        </v-card-title>
        <v-card-text>

          <client-form
            :client="form"
          />

        </v-card-text>
        <v-card-actions>
          <v-btn :loading="loading" @click="deleteClient" color="red" dark>
            <v-icon> mdi-delete </v-icon>
          </v-btn>
          <v-spacer/>
          <v-btn :loading="loading" text @click="closeDialog">
            Отмена
          </v-btn>
          <v-btn :loading="loading" color="primary" :disabled="!formValid" @click="saveClient">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>

  </v-dialog>
</template>

<script>
  import ClientForm from "./ClientForm";
  import gql from 'graphql-tag';

  export default {
    name: "EditClientDialog",
    components: {ClientForm},
    data() {
      return {
        dialog: false,
        loading: false,
        clientId: null,
        form: {

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
      editClient(clientId) {

        this.openDialog()
        this.clientId = clientId

        this.$apollo.query({
          query: gql`
            query($clientId: String!) {
              getClient(clientId: $clientId) {
                id
                firstName
                lastName
                birthDate
                sex
              }
            }`,
          variables: {
            clientId: this.clientId
          }
        }).then(data => {
          this.form = data.data.getClient
        })
      },
      saveClient() {
        this.loading = true

        this.$apollo.mutate({
          mutation: gql`
            mutation ($input: EditClientInput!) {
              editClient(input: $input) {
                status
              }
            }
          `,
          variables: {
            input: {
              id: this.clientId,
              firstName: this.form.firstName,
              lastName: this.form.lastName,
              birthDate: this.form.birthDate,
              sex: this.form.sex
            }
          }
        }).then(data => {
          this.loading = false
          this.$notify({
            group: 'notify',
            title: 'Вы успешно изменили данные клиента',
            text: ''
          })
          this.$emit('updated')
          this.closeDialog()
        }).catch(e => {
          this.loading = false
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при изменение данных клиента',
            text: ''
          })
        })
      },
      deleteClient() {
        this.loading = false

        this.$apollo.mutate({
          mutation: gql`
            mutation ($input: DeleteClientInput!) {
              deleteClient(input: $input) {
                status
              }
            }
          `,
          variables: {
            input: {
              clientId: this.clientId,
            }
          }
        }).then(data => {
          this.loading = false
          this.$notify({
            group: 'notify',
            title: 'Вы успешно удалили клиента',
            text: ''
          })
          this.$emit('deleted')
          this.closeDialog()
        }).catch(e => {
          this.loading = false
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при удаление клиента',
            text: ''
          })
        })
      }
    }
  }
</script>

<style scoped>

</style>