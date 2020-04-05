<template>
  <v-dialog v-model="dialog" max-width="600">

    <v-form v-model="formValid">
      <v-card>
        <v-card-title>

          <span :class="{'body-1': $vuetify.breakpoint.xs}">
            Создание нового клиента
          </span>



          <v-spacer />
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
          <v-spacer/>
          <v-btn text @click="closeDialog" :loading="loading">
            Отмена
          </v-btn>
          <v-btn :loading="loading" color="primary" :disabled="!formValid" @click="createClient">
            Создать
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>

  </v-dialog>
</template>

<script>
  import DatePicker from "../common/DatePicker";
  import ClientForm from "./ClientForm";
  import gql from 'graphql-tag';

  export default {
    name: "CreateClientDialog",
    components: {ClientForm, DatePicker},
    data() {
      return {
        dialog: false,
        loading: false,
        form: {
          firstName: '',
          lastName: '',
          birthDate: '',
          sex: ''
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
      createClient() {
        this.loading = true

        this.$apollo.mutate({
          mutation: gql`
            mutation ($birthDate: String!, $firstName: String!, $lastName: String!, $sex: String!) {
              createClient(birthDate: $birthDate, firstName: $firstName, lastName: $lastName, sex: $sex) {
                status
              }
            }
          `,
          variables: {
            firstName: this.form.firstName,
            lastName: this.form.lastName,
            birthDate: this.form.birthDate,
            sex: this.form.sex
          }
        }).then(data => {
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